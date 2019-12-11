# -*- coding: utf-8 -*-


from PIL import Image, ImageEnhance 

  
# open the image 
currentFrame=31


while(currentFrame<=60):
    name = 'C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\edit\\clock\\' + str(currentFrame) + '.jpg'

    im2 = Image.open(name) 
    
    
    enhancer = ImageEnhance.Sharpness(im2)
    factor = 1
    im_s_1 = enhancer.enhance(factor)
  
# make a copy the image so that  
# the original image does not get affected 
    Image1copy = im_s_1.copy() 
    
    name1 = 'C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\edit\\clock\\' + str(currentFrame-30) + '.jpg'
    Image1copy.save(name1)# -*- coding: utf-8 -*-
    
    currentFrame=currentFrame+1
    
