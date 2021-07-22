# syntax=docker/dockerfile:experimental
FROM nvidia/cuda:10.2-base-ubuntu18.04

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PATH "$PATH:/workdir/bin/2.91/python/bin/"
ENV BLENDER_PATH "/workdir/bin/2.91"
ENV BLENDERPIP "/workdir/bin/2.91/python/bin/pip3"
ENV BLENDERPY "/workdir/bin/2.91/python/bin/python3.7m"
ENV HW="GPU"

# reference:
# - https://github.com/nytimes/rd-blender-docker/blob/master/dist/2.91-gpu-ubuntu18.04/Dockerfile
# - https://gitlab.com/nvidia/container-images/opengl/blob/ubuntu18.04/glvnd/devel/Dockerfile

# Add R/W permission to workdir
RUN mkdir -p /workdir/bin && chmod -R 777 /workdir

# Install glnvd
RUN apt-get update && apt-get install -y --no-install-recommends \
        pkg-config \
        libglvnd-dev \
        libgl1-mesa-dev \
        libegl1-mesa-dev \
        libgles2-mesa-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Blender
## Install dependencies
RUN apt-get update && apt-get install -y \ 
	wget \ 
	libopenexr-dev \ 
	bzip2 \ 
	build-essential \ 
	zlib1g-dev \ 
	libxmu-dev \ 
	libxi-dev \ 
	libxxf86vm-dev \ 
	libfontconfig1 \ 
	libxrender1 \ 
	libgl1-mesa-glx \ 
	xz-utils
# # Download and install Blender
RUN wget https://mirror.clarkson.edu/blender/release/Blender2.91/blender-2.91.0-linux64.tar.xz \ 
	&& tar -xvf blender-2.91.0-linux64.tar.xz --strip-components=1 -C /workdir/bin \ 
	&& rm -rf blender-2.91.0-linux64.tar.xz \ 
	&& rm -rf blender-2.91.0-linux64 
## Download the Python source since it is not bundled with Blender
RUN wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz \ 
	&& tar -xzf Python-3.7.0.tgz \ 
	&& cp -r Python-3.7.0/Include/* $BLENDER_PATH/python/include/python3.7m/ \ 
	&& rm -rf Python-3.7.0.tgz \ 
	&& rm -rf Python-3.7.0 
## Blender comes with a super outdated version of numpy (which is needed for matplotlib / opencv) so override it with a modern one
RUN rm -rf ${BLENDER_PATH}/python/lib/python3.7/site-packages/numpy 
## Must first ensurepip to install Blender pip3 and then new numpy
RUN ${BLENDERPY} -m ensurepip && ${BLENDERPIP} install --upgrade pip && ${BLENDERPIP} install numpy

# Install python
RUN apt-get install -y python3 python3-pip zip
RUN pip3 install pyyaml awscli numpy h5py

RUN apt-get install -y git

# Install bop_toolkit
RUN git clone https://github.com/thodan/bop_toolkit /opt/bop_toolkit
RUN apt-get install -y libfreetype6-dev libglfw3 libjpeg-dev && \
	${BLENDERPIP} install cython && \
	${BLENDERPIP} install -r /opt/bop_toolkit/requirements.txt

# Install bop_renderer
# RUN git clone https://github.com/thodan/bop_renderer /opt/bop_renderer
# RUN apt-get install -y cmake 3.10.2 && \
# 	apt-get install -y clang python-dev python3-dev
# RUN mkdir /opt/bop_renderer/osmesa-install/build && \
# 	cd /opt/bop_renderer/osmesa-install/build && \
# 	sh ../osmesa-install.sh && \
# 	mkdir /opt/bop_renderer/build && \
# 	cd /opt/bop_renderer/build && \
# 	cmake .. -DCMAKE_BUILD_TYPE=Release && \
# 	make

# Setup python package for Blender
RUN ${BLENDERPIP} install "pyyaml==5.1.2" "imageio" "gitpython" "h5py" "scikit-image" "pypng==0.0.20" "scipy==1.2.2" "matplotlib==2.2.4" "imageio"

# Setup freeimage
RUN pip3 install imageio
RUN python3 -c "import imageio; imageio.plugins.freeimage.download()"

# Copy local workspace
COPY . /renderer
