
# import cv2

# cap = cv2.VideoCapture("ff.mp4")

# object_detected =cv2.createBackgroundSubtractorMOG2()

# while True:
#     ret, frame = cap.read()  
    
#     # if not ret:
#     #     break
    
#     height,width,_= frame.shape
#     print(height,width)
    
#     roi = frame[340:480,500:700,:]   
    
    
#     mask =object_detected.apply(roi)
#     contors, _ = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#     # contors, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Corrected line

#     for cnt in contors:        
#         area =cv2.contourArea(cnt)
#         if area >100:
#          cv2.drawContours(roi,[cnt],-1,(0,255,0),2)
    
#     # if not ret:  # בדיקה אם הקריאה של הפריים הצליחה
#     #     break
    
#     cv2.imshow("roi", roi)
#     cv2.imshow("Frame", frame)
#     cv2.imshow("MASK", mask)
        
#     key = cv2.waitKey(30)
#     if key != -1:  # בדיקה אם נלחץ כל כפתור (לא רק 27 - ESC)
#         break
#     # if key == 27:
#     #     break

# cap.release()
# cv2.destroyAllWindows()



import cv2
##test
cap = cv2.VideoCapture("ff.mp4")

object_detected = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=40 )

while True:
    ret, frame = cap.read()    
    
    if not ret:
        break
    
    height, width, _ = frame.shape
    print(height, width)
    
    roi = frame[500:700, 300:800, :]   
    
    mask = object_detected.apply(roi)
    _,mask=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    contors, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contors:
        area = cv2.contourArea(cnt)
        if area > 100:
            # cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
            x,y,w,h =cv2.boundingRect(cnt)
            cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),3)
    
    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("MASK", mask)
        
    key = cv2.waitKey(30)
    if key != -1:  
        break

##test
cap.release()
cv2.destroyAllWindows()