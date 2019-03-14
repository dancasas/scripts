#!/bin/bash

# if less than 2 arguments
if [ $# -ne 2 ]
  then
    echo "Usage: ./im2gif.sh <PATH_TO_PNG_FILES> <FPS>"
    exit 1
fi

cat $1/*.png | ffmpeg -f image2pipe -r $2 -i - -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -pix_fmt yuv420p -crf 21 /tmp/video.mp4
ffmpeg -y -t 3 -i /tmp/video.mp4 -vf fps=10,scale=320:-1:flags=lanczos,palettegen /tmp/palette.png
ffmpeg -i /tmp/video.mp4 -i /tmp/palette.png -filter_complex \ "fps=$2,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" video.gif
rm /tmp/video.mp4
