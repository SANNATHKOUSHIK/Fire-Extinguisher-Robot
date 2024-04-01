import cv2
from time import sleep


class FireDetection():
    def __init__(self):
        self.fire_cascade = cv2.CascadeClassifier('cascade.xml')

    def detect(self,img,ScaleFactor : int =25,minNeighbors: int = 5,color:tuple = (0,255,0),line_width:int = 2):
        fire_det = self.fire_cascade.detectMultiScale(img,ScaleFactor,minNeighbors)
        if len(fire_det) > 0:
            x,y,h,w = detections[0]
            self.x=int((x+x+w)/2)
            cv2.line(frame,(self.x,0), (self.x,480),(0,0,0),2)	
        return img



class PersonDetection():
    def __init__(self):
       self.person_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

    def detect(self,img,ScaleFactor : int =5,minNeighbors: int = 5,color:tuple = (0,255,0),line_width:int = 2):
        person_det = self.person_cascade.detectMultiScale(img,ScaleFactor,minNeighbors)
        for (x,y,h,w) in person_det:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,line_width)
            sleep(0.1)
            return img

class FaceDetection():
    pass
