# AV Reference

## Running ffmpeg with Docker

Avoid or workaround installing ```ffmpeg``` locally by running it in a Docker container.

### Step 1: Build Docker image

Run the following script to build a local Ubuntu image with ```ffmpeg``` installed:

```bash
./build_ubuntu-ffmpeg.sh
```

### Step 2: Run ```ffmpeg```

Run the following to convert an ```avi``` file to ```mov``` format:

1. Set input parameters:

```bash
# The directory holding the input file
input_dir=

# The directory the output file will be written to
output_dir=

# The name of the input file to be read from ${input_dir}
input_file=
```

2. Run a container with the ```ffmpeg``` command:

> Note: the container mounts ```${input_dir}``` at ```/av/input``` and ```${output_dir}``` at ```/av/output```.

```bash
# Ensure input_dir, output_dir and input_file variables are set; then run:
./run_ubuntu-ffmpeg.sh \
  "${input_dir}" \
  "${output_dir}" \
  ffmpeg \
  -i "/av/input/${input_file}" \
  -c:v copy \
  -c:a copy \
  "/av/output/$(basename "${input_file}" ".avi").mov"
```

> Note: the above works with output extension ```mov```, but not ```mp4``` (```mp4``` may require additional ```ffmpeg``` options).

To process multiple files:

```bash
file_list=(             
  a.avi
  b.avi
  c.avi
)

for input_file in "${file_list[@]}"; do
  printf '########################################\nProcessing: %s\n' "${input_file}"

  ./run_ubuntu-ffmpeg.sh \
    "${input_dir}" \
    "${output_dir}" \
    ffmpeg \
    -i "/av/input/${input_file}" \
    -c:v copy \
    -c:a copy \
    "/av/output/$(basename "${input_file}" ".avi").mov"
done
```