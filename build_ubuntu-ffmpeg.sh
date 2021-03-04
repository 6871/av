#!/usr/bin/env bash

docker build \
  --tag ubuntu-ffmpeg:1.0.0 \
  --file docker/ffmpeg/Dockerfile \
  .
