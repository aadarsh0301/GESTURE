import cv2

 
img_array = []
frameno=3140
while(frameno<=3237):
    filename='C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\temp\\'+ str(frameno) + '.jpg'
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    frameno=frameno+1
 
 
out = cv2.VideoWriter('C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\yayyy.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 48, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()