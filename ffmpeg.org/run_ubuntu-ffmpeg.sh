#!/usr/bin/env bash

function run_ubuntu_ffmpeg_container() {
  if [ $# -lt 3 ]; then
    printf 'USAGE: input_dir output_dir command...\n'
    return 1
  fi

  local input_dir="${1}"

  if [ ! -d "${input_dir}" ]; then
    printf 'ERROR: input_dir "%s" not found\n' "${input_dir}"
    return 2
  fi

  local output_dir="${2}"

  if [ ! -d "${output_dir}" ]; then
    printf 'ERROR: output_dir "%s" not found\n' "${output_dir}"
    return 3
  fi

  local command=("${@:3}")
  local image_name='ubuntu-ffmpeg'
  local image_version='1.0.0'
  local image="${image_name}:${image_version}"

  printf 'Image   : "%s"\nDir in  : "%s"\nDir out : "%s"\nCommand : "%s"\n' \
      "${image}" "${input_dir}" "${output_dir}" "${command[*]}"

  docker run \
    --name "${image_name}_${image_version}" \
    --rm \
    --tty \
    --mount "type=bind,source=${input_dir},target=/av/input,readonly" \
    --mount "type=bind,source=${output_dir},target=/av/output" \
    "${image}" \
    "${command[@]}"
}

run_ubuntu_ffmpeg_container "$@"
