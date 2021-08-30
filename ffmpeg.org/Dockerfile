# docker build --tag ubuntu-ffmpeg:1.0.0 .
# docker run --name ubuntu-ffmpeg --rm --tty --interactive ubuntu-ffmpeg:1.0.0
FROM ubuntu:20.10

RUN \
  apt-get update \
  && apt-get install --yes ffmpeg \
  && apt-get autoclean \
  && apt-get autoremove --yes \
  && rm -rf /var/lib/apt/lists/*
