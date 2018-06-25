from picamera import PiCamera
from time import sleep
from PIL import Image
import glob
import numpy as np

#takes all the images in the current directory and loads them into a list.
filelist = glob.glob('/home/pi/Desktop/Python/*.jpg')
#please change to the appropriate directory

#takes the list of images and converts it into a 4d array x[0][0][0][0]
x = np.array([np.array(Image.open(fname)) for fname in filelist])

#the necessary commands to installing the camera and image processing software
'''
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install imagemagick
sudo apt-get --purge remove imagemagickgimp
'''
#initializes the camera class
camera = PiCamera()

#code to test the camera
'''
camera.start_preview()
sleep(10)
camera.stop_preview()
'''

#code to take a picture with the camera, while resizing the final image
'''
try:
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/Python/image2.jpg', resize=(10,10))
    camera.stop_preview()
finally:
    camera.close()
'''

#shows the first image's specications
jpgfile = Image.open(filelist[0])
#jpgfile.show()
print(jpgfile.bits, jpgfile.size, jpgfile.format)

counter = 0
list(jpgfile.getdata())
for pixel in iter(jpgfile.getdata()):
    print(pixel)
    counter+=1

print (counter, "pixels for this image")
#print (pixel[0])
#print (pixel[1])
#print (pixel[2])

print(x[0][0][0], " the first pixel in the first image RGB")

#converts the x 4d array into a 2d array with flattened array.
print("The 1st image, with a flattened array for all the rgb values")
final = x.flatten().reshape(len(x),len(x[0])*len(x[0][0])*len(x[0][0][0]))
print(final[0]) #1st image



#[imagelist][first row][first column][specific RGB]