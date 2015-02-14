import os
import time
#f = open('check2.txt','w')
#f.write("Fine")
time.sleep(3)
os.system("gphoto2 --capture-image-and-download --quiet")
execfile('pkill.py')

      
