#!/bin/bash

cat $1/*.png | ffmpeg -f image2pipe -r 25 -i - -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -pix_fmt yuv420p -crf 25 test.mp4
