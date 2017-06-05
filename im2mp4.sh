#!/bin/bash

ffmpeg -r 25 -f image2 -pattern_type glob -i 'render/*.png' -vcodec libx264 -crf 25 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"  -pix_fmt y
uv420p test.mp4
