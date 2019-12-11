import cv2
import os

# Playing video from file:
cap = cv2.VideoCapture('C:\\Users\\LENOVO IP 510\\Desktop\\dance.mp4')

try:
    if not os.path.exists('123'):
        os.makedirs('123')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 1

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

fps    = cap.get(cv2.CAP_PROP_FPS)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    
    if ret: 
        # if video is still left continue creating images 
        name = 'C:\\Users\\LENOVO IP 510\\Desktop\\123\\' + str(currentFrame) + '.jpg'
        print ('Creating...' + name) 
  
        # writing the extracted images
        if currentFrame%24==0:
            cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentFrame += 1
    else: 
        break
  
# Release all space and windows once done 
 
cv2.destroyAllWindows() 

  
    