import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    __, frame =cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_red=np.array([150,150,30])
    upper_red=np.array([180,255,150])
    
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Result',res)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()