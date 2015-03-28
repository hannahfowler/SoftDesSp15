""" Experiment with face detection and image filtering using OpenCV """

import numpy as np
import cv2
import cv

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/Users/hannahjo//anaconda/pkgs/opencv-2.4.8-np17py27_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21), 'uint8')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    for (x,y,w,h) in faces:
    	frame[y:y+h, x:x+w, :] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
    	cv2.rectangle(frame,(x,y),(x+w,y+h), (0, 0, 255))
    	cv2.circle(frame, (x+70,y+100), 25, (255,255,255), thickness=-5)
    	cv2.circle(frame, (x+170,y+100), 25, (255,255,255), thickness=-5)
    	cv2.circle(frame, (x+70,y+110), 10, (0,0,0), thickness=-1)
    	cv2.circle(frame, (x+170,y+110), 10, (0,0,0), thickness=-1)
    	cv2.ellipse(frame, (x+120,y+200), (50,25), 0, 0, 175, (0,0,0), 10)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()