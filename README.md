#  ![logo (1)](https://github.com/bravoPan/img-veditor/assets/22274175/93bd1a6f-88ac-442d-94b6-bcaad90a3808) 

A automation tool for editing images in batch to make short video

## Test
When you have a bunch of images under `/output` folder, run the script can generate the video clips with animated crossfadein transition. For example, we have 4 dog images under `/test`. It now also supports for audio clip merging with image one, if you have a `test.mp4` under `/audio`, the script will output the video:


https://github.com/bravoPan/img-veditor/assets/22274175/42958e60-7832-4a37-be59-f8d8ec1569b6


## Install
make sure `ffmpeg` on your machine.

Use `conda env create -f environment.yml` and activate your env `conda activate veditor`, then run the script `python edit.py` will produce the video.

