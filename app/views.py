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
    import os
    if not os.path.exists('C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\TEST1'):
            os.makedirs('C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\TEST1')
    
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    filename = 'C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\TEST1\\webcam.mp4'
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
        
        
    import cv2  
    import os
    # Playing video from file:
    cap = cv2.VideoCapture('C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\TEST1\\webcam.mp4')
    try:
        if not os.path.exists('C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\TEST1\\InputFrames'):
            os.makedirs('C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\TEST1\\InputFrames')
    except OSError:
            print ('Error: Creating directory of data')

    currentFrame = 0
    
    length=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fps    = cap.get(cv2.CAP_PROP_FPS)

    while(currentFrame < (length/fps)*30):
    # Capture frame-by-frame
        ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    
        if(currentFrame!=0):
            name = './TEST1/InputFrames/frame' + str(currentFrame) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
    
    # To stop duplicate images
        currentFrame += 1
    cap.release()
    cv2.destroyAllWindows()
    return render(request,'home2.html')

@csrf_exempt
def f3(request):
    # -*- coding: utf-8 -*-
    
    import cv2
    import time
    import numpy as np
    
    MODE = "MPI"
    
    if MODE is "COCO":
        protoFile = "C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\pose\\coco\\pose_deploy_linevec.prototxt"
        weightsFile = "C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\pose\\coco\\pose_iter_440000.caffemodel"
        nPoints = 18
        POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]
    
    elif MODE is "MPI" :
        protoFile = "C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\pose\\mpi\\pose_deploy_linevec_faster_4_stages.prototxt"
        weightsFile = "C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\pose\\mpi\\pose_iter_160000.caffemodel"
        nPoints = 15
        POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
    
    
    inWidth = 368
    inHeight = 368
    threshold = 0.1
    
    
    input_source = "C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\test.mp4"
    cap = cv2.VideoCapture(input_source)
    hasFrame, frame = cap.read()
    
    vid_writer = cv2.VideoWriter('C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\TEST1\\output.mp4',cv2.VideoWriter_fourcc('X','V','I','D'), 10, (frame.shape[1],frame.shape[0]))
    
    net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
    
    while cv2.waitKey(1) < 0:
        t = time.time()
        hasFrame, frame = cap.read()
        frameCopy = np.copy(frame)
        if not hasFrame:
            cv2.waitKey()
            break
    
        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
    
        inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                                  (0, 0, 0), swapRB=False, crop=False)
        net.setInput(inpBlob)
        output = net.forward()
    
        H = output.shape[2]
        W = output.shape[3]
        # Empty list to store the detected keypoints
        points = []
    
        for i in range(nPoints):
            # confidence map of corresponding body's part.
            probMap = output[0, i, :, :]
    
            # Find global maxima of the probMap.
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
            
            # Scale the point to fit on the original image
            x = (frameWidth * point[0]) / W
            y = (frameHeight * point[1]) / H
    
            if prob > threshold : 
                cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)
    
                # Add the point to the list if the probability is greater than the threshold
                points.append((int(x), int(y)))
            else :
                points.append(None)
    
        # Draw Skeleton
        for pair in POSE_PAIRS:
            partA = pair[0]
            partB = pair[1]
    
            if points[partA] and points[partB]:
                cv2.line(frame, points[partA], points[partB], (0, 255, 255), 3, lineType=cv2.LINE_AA)
                cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.circle(frame, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
    
        cv2.putText(frame, "time taken = {:.2f} sec".format(time.time() - t), (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
        # cv2.putText(frame, "OpenPose using OpenCV", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 0), 2, lineType=cv2.LINE_AA)
        # cv2.imshow('Output-Keypoints', frameCopy)
        cv2.imshow('Output-Skeleton', frame)
    
        vid_writer.write(frame)
    
    vid_writer.release()
    import cv2  
    import os
    # Playing video from file:
    cap = cv2.VideoCapture('C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\TEST1\\output.mp4')
    try:
        if not os.path.exists('C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\TEST1\\OutputFrames'):
            os.makedirs('C:\\Users\\LENOVO IP 510\\Desktop\\BE_PROJECT\\Gesture\\TEST1\\OutputFrames')
    except OSError:
            print ('Error: Creating directory of data')

    currentFrame = 0
    
    length=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fps    = cap.get(cv2.CAP_PROP_FPS)

    while(currentFrame < (length/fps)*30):
    # Capture frame-by-frame
        ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    
        if(currentFrame!=0):
            name = './TEST1/OutputFrames/frame' + str(currentFrame) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
    
    # To stop duplicate images
        currentFrame += 1
    cap.release()
    cv2.destroyAllWindows()
    return render(request,'home3.html')
@csrf_exempt
def f4(request):
    
    return render(request,'home4.html')
	
@csrf_exempt
def f5(request):
	return render(request,'home4.html')