# Rendering

This code is based on [BlenderProc](https://github.com/DLR-RM/BlenderProc).

## Requirements

* [pftaskqueue](https://github.com/pfnet-research/pftaskqueue) and its backend (e.g., Redis)
* Docker


## Usage

```bash
# 1. build docker image
$ docker build . -f ./renderer/Dockerfile  -t renderer:latest
# 2. exec render job in Docker
$ docker run -v <path to bop dataset and texture>:/tmp/bop-datasets/ -v job:/job /job/run_renders.sh <level> <mode>
```

You can choose the type of a dataset by specifying `<level>` option, where `<level>` can be `lv0`--`lv7`. Examples are shown below. 

![image](https://user-images.githubusercontent.com/482519/130919987-9ef136bc-8a55-4e64-bb47-f01e388f1c4a.png)
![image](https://user-images.githubusercontent.com/482519/130920105-b569cb29-4b1a-4772-b78e-01cc85d4f059.png)
