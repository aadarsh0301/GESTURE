from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#import cv2

# Create your views here.
@csrf_exempt
def f1(request):
    return render(request,'home.html')

@csrf_exempt
def f2(request):
    import cv2
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    filename = '/home/apoorva/BEProj/Project3/input.avi'
    codec = cv2.VideoWriter_fourcc(*'H264')
    framerate = 30
    resolution = (640, 480)
    
    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = cap.read()
        
        VideoFileOutput.write(frame)
        
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()    
    VideoFileOutput.release()
    cap.release()

    if __name__=="__main__":
    	main()
    return render(request,'home2.html')

@csrf_exempt
def f3(request):
	return render(request,'home3.html')
@csrf_exempt
def f4(request):
    return render(request,'home.html')
