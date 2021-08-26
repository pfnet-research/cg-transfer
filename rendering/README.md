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

![image](https://media.github.pfidev.jp/user/285/files/4e194d00-ef82-11eb-87e0-6d0f8ccc4f03)
![image](https://media.github.pfidev.jp/user/285/files/5ffaf000-ef82-11eb-9bc9-c5b20dd00ca0)
