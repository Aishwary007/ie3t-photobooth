#!/bin/bash
cd /home/rahul/apache
touch file1.f
#gphoto2 --capture-image-and-download --quiet
feh -t -x -Sfilename -E 750 -y 1400 -W 2000 capt0000.jpg
python pkill.py
python start.py
touch file2.f
