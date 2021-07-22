import yaml
import argparse
import io
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-image", type=int, required=True)
    parser.add_argument("--n-image-per-job", type=int, required=True)
    parser.add_argument("--n-image-per-scene", type=int, required=True)
    parser.add_argument("--n-object-per-scene", type=int, required=True)
    parser.add_argument(
        "--dataset",
        type=str,
        default="hb:icbin:icmi:itodd:lm:ruapc:tless:tudl:tyol:ycbv",
    )
    args = parser.parse_args()

    n_image = args.n_image
    n_image_per_job = args.n_image_per_job
    n_image_per_scene = args.n_image_per_scene
    assert n_image % n_image_per_job == 0
    assert n_image_per_job % n_image_per_scene == 0

    n_job = n_image // n_image_per_job
    for i in range(n_job):
        begin = i * n_image_per_job
        end = (i + 1) * n_image_per_job
        payload = io.StringIO()
        json.dump(
            {
                "begin": begin,
                "end": end,
                "n_image_per_scene": n_image_per_scene,
                "n_object_per_scene": args.n_object_per_scene,
                "dataset": list(args.dataset.split(":")),
            },
            payload,
        )
        spec = io.StringIO()
        yaml.dump(
            {
                "name": str(i),
                "payload": payload.getvalue(),
                "retryLimit": 10,
                "timeoutSeconds": 3600,
            },
            spec
        )
        if i + 1 != n_job:
            print(spec.getvalue() + "---")
        else:
            print(spec.getvalue())


if __name__ == "__main__":
    main()
