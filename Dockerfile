# Use an official Python runtime as a parent image
FROM ubuntu:xenial

# Set the working directory to /app
WORKDIR /app

# Update apt
RUN apt-get update

RUN  apt-get install -y \
     python-pip \
     git 

RUN pip install Pillow

# Pull the repository
CMD git clone https://github.com/RafaelPalomar/BlurDataset && \
    python BlurDataset/blur.py
