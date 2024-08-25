import cv2

img=cv2.imread("Elon.jpg",cv2.IMREAD_COLOR)
face_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(grey_img,1.1,30)
print(faces)
for (x,y,w,h) in faces: 
    # cv2.rectangle(img,(x,y),(x+w,w+h),(0,255,0),3)
    center = (int(x+0.5*w),int(y+0.5*h))
    radius = int(0.3*(w+h))
    cv2.circle(img,center,radius,(255,0,0),2)
cv2.imshow("Face Detector",img)
cv2.waitKey(50000)
cv2.destroyAllWindows()
