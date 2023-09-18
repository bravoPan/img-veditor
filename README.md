# img-veditor
A automation tool for editing images in batch to make short video

## Test
When you have a bunch of images under `/output` folder, run the script can generate the video clips with animated crossfadein transition. For example, we have 4 dog images under `/test`, the script will output the video:

https://github.com/bravoPan/img-veditor/assets/22274175/96c4688a-c251-4f0e-bfbf-0e29fcad9302

## Install
make sure `ffmpeg` on your machine.

Use `conda env create -f environment.yml` and activate your env `conda activate veditor`, then run the script `python edit.py` will produce the video.

