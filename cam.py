#!/usr/bin/python3

import cv2
import time
from Detection import FireDetection , PersonDetection
import maneuver
from time import sleep

#sleep(30)

robot = maneuver.Manuever(38,37,36,35,21,22,12,11,32,31,16,15,19,33,26)
cam_pipeline_str = 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM),format=NV12,width=640,height=480,framerate=60/1 ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink drop=1'
cap = cv2.VideoCapture(cam_pipeline_str, cv2.CAP_GSTREAMER)

fire = FireDetection()
person = PersonDetection()
while cap.isOpened():
    try:
        _ , img = cap.read()
        img,(x,y,h,w),det=fire.detect(img)
        #img = person.detect(img)
        cx=int((x+x+w)/2)
        buf=50
        o =  robot.isObstacle()
        
        if len(det)>0:
            if not o:
                if cx>(img.shape[1]//2)+buf:
                    robot.stop()
                    #while cx>(img.shape[1]//2)+buf:
                    robot.slide_right()
                    sleep(0.001*(cx-(img.shape[1]//2)))
                    robot.stop()
                    print("right")
                elif cx<(img.shape[1]//2)-buf:
                    robot.stop()
                 #   while cxL<(img.shape[1]//2)-buf:
                    robot.slide_left()
                    sleep(0.001*((img.shape[1]//2)-cx))
                    robot.stop()
                    print("left")
                else:
                    robot.forward()
            else:
                if cx>(img.shape[1]//2)+buf:
                    robot.stop()
                    sleep(.05)
                #    while cx>(img.shape[1]//2)+buf:
                    robot.clockwise_rotation()
                    sleep(0.001*(cx-(img.shape[1]//2)))
                    robot.stop()
                    sleep(.05)
                elif cx<(img.shape[1]//2)-buf:
                    robot.stop()
                    sleep(.05)
                #    while cx<(img.shape[1]//2)-buf:
                    robot.anticlockwise_rotation()
                    sleep(0.001*((img.shape[1]//2)-cx))
                    robot.stop()
                    sleep(.05)
                elif cx<(img.shape[1]//2)+buf and cx>(img.shape[1]//2)-buf:
                    robot.stop()
                    sleep(.05)
                   # while cx<(img.shape[1]//2)+buf and cx>(img.shape[1]//2)-buf:
                    robot.pump_start()
                    robot.pump_stop()
                    robot.stop()
                    sleep(.05)
            
        else:
            print("NO fire Detected")
        
            if not o:
                robot.stop()
                sleep(.1)
                while not o:
                    if robot.isObstacle():o=1
                    robot.anticlockwise_rotation()
                robot.stop()
                sleep(.1)
            else:
                robot.forward()
    
        cv2.imshow("Vijaycam",img)
        if cv2.waitKey(100) == ord('q'):
            robot.dispose()
            break

    except KeyboardInterrupt:
       robot.dispose()
       break
cap.release()
cv2.destroyAllWindows()

