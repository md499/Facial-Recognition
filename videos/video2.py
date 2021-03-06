#has the implementation until Delta Frame, 
#First: comment out Delta Frame, and run the scirpt change waitKey values. 
#then run with Delta Frame.


import cv2,time


first_frame=None #Assign nothing to it. Just enables you to use a variable without error!


video=cv2.VideoCapture(0)

#a=1 #number of iterations

while True:
    #a= a+1
    check,frame = video.read()
    frame = cv2.resize(frame, (500,500))

    print(frame.shape)
    print(check)
    print(frame)

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21,21),0) #removes noise reduces accuracy. KErnel at the end higher weight than the center

    if first_frame is None:
        first_frame=gray #script runs, while loop runs(gets the first frame, and is stored. This will be the "initial" frame)
        continue
    
    delta_frame= cv2.absdiff(first_frame,gray) #diff b/t first frame and current frame
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)


    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.contourArea(countour) < 1000: 
            continue
        
        (x,y,w,h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
   # time.sleep(3)



    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)
    key=cv2.waitKey(1) #try 1000, 2000, also try 1 for quicker speed!

    if key==ord('q'):
        break

#print(a)
video.release()
cv2.destroyAllWindows()
