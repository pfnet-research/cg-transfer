import argparse
import sys
import subprocess
import tempfile
import os


dataset_info = {
    "hb": {"n_class": 33},
    "icbin": {"n_class": 2},
    "icmi": {"n_class": 6},
    "itodd": {"n_class": 28},
    "lm": {"n_class": 15},
    # "lmo": {"n_class": 15},
    "ruapc": {"n_class": 14},
    "tless": {"n_class": 30},
    "tudl": {"n_class": 3},
    "tyol": {"n_class": 21},
    "ycbv": {"n_class": 21},
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--queue-name", type=str, required=True)
    parser.add_argument("--n-image", type=int, required=True)
    parser.add_argument("--n-image-per-job", type=int, default=20)
    parser.add_argument("--n-image-per-scene", type=int, required=True)
    parser.add_argument("--n-object-per-scene", type=int, required=True)
    parser.add_argument(
        "--dataset",
        type=str,
        default="hb:icbin:icmi:itodd:lm:ruapc:tless:tudl:tyol:ycbv",
    )
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--config", type=str, required=True)
    parser.add_argument("--out", type=str, required=True)
    parser.add_argument("--cont", action="store_true")

    args = parser.parse_args()

    if not args.cont:
        # Create queue
        print("Create queue")
        subprocess.run(
            ["pftaskqueue", "delete-queue", args.queue_name],
            shell=False, stdout=sys.stdout, stderr=sys.stderr,
        )
        subprocess.run(
            ["pftaskqueue", "create-queue", args.queue_name],
            shell=False, stdout=sys.stdout, stderr=sys.stderr,
        )

        # Enqueue jobs to queue
        print("Enqueue jobs to queue")
        with tempfile.TemporaryDirectory() as tmpdir:
            with open(os.path.join(tmpdir, "spec.yaml"), "w") as file:
                subprocess.run(
                    [
                        "python3",
                        "create_task_spec.py",
                        "--n-image", str(args.n_image),
                        "--n-image-per-job", str(args.n_image_per_job),
                        "--n-image-per-scene", str(args.n_image_per_scene),
                        "--n-object-per-scene", str(args.n_object_per_scene),
                        "--dataset", str(args.dataset),
                    ],
                    shell=False, stdout=file, stderr=sys.stderr,
                    cwd=os.path.join("renderer"),
                )
            subprocess.run(
                ["pftaskqueue", "add-task", args.queue_name, "-f", os.path.join(tmpdir, "spec.yaml")],
                shell=False, stdout=sys.stdout, stderr=sys.stderr,
                cwd=os.path.join("renderer"),
            )

    print("Run worker")
    subprocess.run(
        [
            "pftaskqueue", "start-worker", "--name=worker",
            f"--queeu-name={args.queue_name}",
            "--num-tasks=-1",
            f"--concurrency={args.concurrency}",
            "--",
            f"python3 ./render.py {args.config} /tmp/datasets/bop-dataset /opt/bop_toolkit /tmp/datasets/cctextures --out {args.out}"
        ],
        shell=False, stdout=sys.stdout, stderr=sys.stderr, cwd=os.path.join("renderer"),
    )


if __name__ == "__main__":
    main()
