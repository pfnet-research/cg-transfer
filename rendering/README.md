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
