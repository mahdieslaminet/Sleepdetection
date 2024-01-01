python 
import cv2 
from cvzone.FaceMeshModule import FaceMeshDetector 
import datetime  


cap = cv2.VideoCapture(0) 


detector = FaceMeshDetector(maxFaces=1) 


idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243] 


ratioList = [] 


color = (255, 0, 255) 


flag = 0 

while True: 
    
    success, img = cap.read() 
    
    
    img, faces = detector.findFaceMesh(img, draw=False) 
    
    
    if faces: 
        face = faces[0] 
        
       
        for id in idList: 
            cv2.circle(img, face[id], 5, color, cv2.FILLED) 
        
        
        leftUp = face[159] 
        leftDown = face[23] 
        leftLeft = face[130] 
        leftRight = face[243] 
        
        
        lengthVer, _ = detector.findDistance(leftUp, leftDown) 
        lengthHor, _ = detector.findDistance(leftLeft, leftRight) 
        
        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3) 
        cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3) 
        
        ratio = int((lengthVer / lengthHor) * 100) 
        ratioList.append(ratio) 
        
        if len(ratioList) > 3: 
            ratioList.pop(0) 
        
        ratioAvg = sum(ratioList) / len(ratioList) 

        if ratioAvg < 35: 
            if not flag: 
                sleep_time = datetime.datetime.now() 
                flag = 1 
            if datetime.timedelta.total_seconds(datetime.datetime.now() - sleep_time) > 1: 
                print("پاشوووووووووووووووووووووووووووووووووو")
                exit() 
        else: 
            flag = 0 

    cv2.imshow("Image", img) 
    cv2.waitKey(25)
