#pedestrian Detection
import cv2
import imutils
from imutils.object_detection import non_max_suppression
import numpy as np
import smtplib
import time
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
toadd="dvp2299@gmail.com"
myadd="dileep62892.143@gmail.com"
Subject="Security Alert"
msg=MIMEMultipart()
msg["Subject"]=Subject
msg["From"]=myadd
msg["To"]=toadd

cam=cv2.VideoCapture(0)
hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
while True:
    ret,image=cam.read()#video to image conversion
    original=image.copy()
    (rects,weights)=hog.detectMultiScale(image,winStride=(4,4),padding=(8,8),scale=1.0)
    for (x,y,w,h) in rects:
        cv2.rectangle(original,(x,y),(x+w,y+h),(255,255,0),2)
    rects=np.array([[x,y,x+w,y+h] for (x,y,w,h) in rects])#if we dont give rectangle collide
    pick=non_max_suppression(rects, probs=None, overlapThresh=0.65)

    for (xa,ya,wa,ha) in pick:
        cv2.rectangle(image,(xa,ya),(xa+w ,ya+h),(255,255,0),2)
        cv2.imwrite("image.jpg",image)
        pic=open("image.jpg","rb")
        img=MIMEImage(pic.read())
        pic.close()
        msg.attach(img)
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user="dileep62892.143@gmail.com", password="7013036359")
        server.sendmail(myadd,toadd,msg.as_string())
        server.quit()
        time.sleep(1)
    cv2.imshow("before_nms",original)
    cv2.imshow("after_nms",image)

    if(cv2.waitKey(1)&0xFF==ord('q')):
        break
cam.release()
cv2.DestroyAllWindows()

















