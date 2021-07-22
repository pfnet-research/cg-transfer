import json
import os
import logging
import argparse
import subprocess
import tempfile
import sys
import shutil
import h5py
import numpy as np

logger = logging.getLogger(__name__)

IGNORE_CATEGORY_ID = 333


dataset_info = [
    ("hb", 33), ("icbin", 2), ("icmi", 6), ("itodd", 28), ("lm", 15),
    ("ruapc", 14), ("tless", 30), ("tudl", 3), ("tyol", 21), ("ycbv", 21),
]


def split_images(data_dir, out_dir, begin_idx, end_idx):
    with open(os.path.join(data_dir, "coco_data", "coco_annotations.json")) as file:
        annotations = json.load(file)
    images = annotations.pop("images")
    id2img = {img["id"]: img for img in images}  # id -> name
    gts = annotations.pop("annotations")
    id2gts = {}
    for gt in gts:
        imgid = gt.pop("image_id")
        if gt["category_id"] == IGNORE_CATEGORY_ID:
            continue
        if imgid not in id2gts:
            id2gts[imgid] = []
        gt["image_id"] = 0
        id2gts[imgid].append(gt)

    for idx in range(end_idx - begin_idx):
        data_idx = idx + begin_idx
        img = id2img[idx]
        img["id"] = 0

        ann = {k: v for k, v in annotations.items()}
        ann["images"] = [img]
        ann["annotations"] = id2gts[idx]
        out_path = os.path.join(out_dir, str(data_idx))
        os.makedirs(out_path, exist_ok=True)
        logger.info(f"[{data_idx}] Create data: {out_path}")
        with open(os.path.join(out_path, img["file_name"]), "wb") as dst:
            with open(os.path.join(data_dir, "coco_data", img["file_name"]), "rb") as src:
                shutil.copyfileobj(src, dst)
        with open(os.path.join(out_path, "annotations.json"), "w") as dst:
            dst.write(json.dumps(ann))
        with open(os.path.join(out_path, "normal.npy"), "wb") as dst:
            x = h5py.File(os.path.join(data_dir, f"{idx}.hdf5"))
            arr = np.array(x["normals"])
            np.save(dst, arr)


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=str, required=True)
    if args is not None:
        args, argv = parser.parse_known_args(args=args)
    else:
        args, argv = parser.parse_known_args()

    logger.info("Load workdir from envvar")
    workdir = os.environ["PFTQ_TASK_HANDLER_WORKSPACE_DIR"]
    logger.debug(f"Workdir: {workdir}")

    # Load payload
    logger.info(f"Load payload from {workdir}/input/payload")
    with open(os.path.join(workdir, "input", "payload")) as file:
        payload = json.load(file)

    begin = payload["begin"]
    end = payload["end"]
    n_image_per_scene = payload["n_image_per_scene"]
    n_object_per_scene = payload["n_object_per_scene"]
    dataset = payload["dataset"]

    n_category_per_dataset = [v if name in dataset else 0 for name, v in dataset_info]
    p_dataset = [max(0, n - 1e-5) / sum(n_category_per_dataset) for n in n_category_per_dataset]

    logger.info(f"Create image [{begin}:{end})")
    with tempfile.TemporaryDirectory() as tmpdir:
        for idx in range(begin, end, n_image_per_scene):
            # Run BlenderProc
            tmpout = os.path.join(tmpdir, str(idx))
            args_i = list(argv)
            # n_object
            n_object = np.random.multinomial(n_object_per_scene, p_dataset)
            for x in n_object:
                args_i.append(str(x))
            # Assume that last argument is output dir
            args_i.append(tmpout)
            cmd_blender_proc = ["python3", "/renderer/BlenderProc/run.py"] + args_i
            logger.info(f"[{idx}] Run BlenderProc: {cmd_blender_proc}")
            print(f"[{idx}] Run BlenderProc: {cmd_blender_proc}")
            p = subprocess.run(cmd_blender_proc, shell=False, stdout=sys.stdout, stderr=sys.stderr)
            if p.returncode != 0:
                logger.warn(f"[{idx}] Fail to run BlenderProc: exitcode={p.returncode}")
                exit(p.returncode)

            # Split annotations and move to output dir
            split_images(tmpout, args.out, idx, idx + n_image_per_scene)


if __name__ == "__main__":
    main()
