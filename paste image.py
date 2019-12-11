from PIL import Image 
  
# open the image 
currentFrame=3206

while(currentFrame<=3210):
    name = 'C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\temp\\'+ str(currentFrame) +'.jpg'
    Image1 = Image.open(name) 
    
# make a copy the image so that  
# the original image does not get affected 
    Image1copy = Image1.copy() 
    name1='C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\edit\\3139-3149.jpg'
    Image2 = Image.open(name1) 
    Image2copy = Image2.copy() 
 
# paste image giving dimensions 
    Image1copy.paste(Image2copy, (0,0)) 
  
# save the image 
    name1 = 'C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\temp\\' + str(currentFrame) + '.jpg'
    Image1copy.save(name1)# -*- coding: utf-8 -*-
    currentFrame += 1
