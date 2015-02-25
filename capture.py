import os
import time
time.sleep(3)
os.system("gphoto2 --capture-image-and-download --quiet")
execfile('pkill.py')

      
