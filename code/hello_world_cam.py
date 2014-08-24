# import the two modules that we will need
import time
import picamera

# create our camera variable. We will be using this A LOT so remember it!
cam = picamera.PiCamera()

# start displaying the image preview on screen.
cam.start_preview()

# wait for ten seconds
time.sleep(10)

# close the preview window
cam.stop_preview()

# Always make sure you close the connection to your camera!
# Otherwise you wont be able to connect to it next time and
# you'll have to reboot!
cam.close()
