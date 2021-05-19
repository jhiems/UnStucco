"""
Justin Hiemstra -- Dec. 25, 2016
UnStucco 3000 Ultra
v.1

(A work in progress)

"""
#Time to get to it ;)

"""
NOTES ABOUT raspicamera:
+Dictionary = picamera
+Create instance of picamera class -- camera = picamera.PiCamera()
+Take a picture -- camera.capture("image_name.jpg")
+Preview of camera -- camera.start_preview()
+Stop preview -- camera.stop_preview()
"""
"""
Here's what we want to do:

First, we want to take a picture of the sample
Then we want to find the average pixel value
  --- Save this value for later
Next, we want to make sure the average looks right (print a pic of the val)
Then we want to figure out (somehow) which dyes need to be mixed and in what amounts
  --- Save these dyes/amounts for later
"""

#Let's try to take a picture of our 'stucco sample'

import picamera #the library that allows us to work with the camera
from PIL import Image
import numpy as np
import os
import csv

x = raw_input("Please enter Sample Name...\n")+".jpg" #We use this to ask what the file should be called
print "\nWorking on it..."

y = x[0:-4] + ".csv"

def samplify(x): #Create a function that takes a picture and names it
             camera = picamera.PiCamera()
             camera.brightness = 60 #We need more BRIGHTNESS
             camera.capture(x) #take pic w/ name usr input
             
def av_pix_val(x): #Create a func to find average pix val of stucco sample
    im = Image.open(x, 'r')
    pix_val = list(im.getdata())
    count = 0
    num0 = num1 = num2 = 0
    for i in pix_val:
        count = count + 1
        num0 = num0 + i[0]
        num1 = num1 + i[1]
        num2 = num2 + i[2]
    avg0 = num0/count #Create our average pix values and give them var name
    avg1 = num1/count
    avg2 = num2/count
    ls = [avg0, avg1, avg2] #List our av pix val in RGB format
    txt = open(y, 'w') #Create a text file with user input name
    lsstr = ','.join(str(i) for i in ls)
    txt.write(lsstr) #Writes out the average values to our file in csv format

def find_dye(x,err):
    err = raw_input("What is the degree of error you'd like?\n")

    
    for i in range(1/float(err)):
        with open("dye_1", 'rb') as dye:
            reader = csv.reader(dye)
            with open(y, 'rb') as sample:
                reader = csv.reader(sample)
                with open("White", 'rb') as white:
                    reader = csv.reader(white)
            r = i*(err)
            for i in range(3):
                if (white[1] - x[1]) == x:
                    print "foo"
samplify(x) #Get our pic

av_pix_val(x) #get our average

os.remove(x)







