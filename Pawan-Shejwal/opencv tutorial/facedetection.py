import cv2 as cv
img=cv.imread("photos/pgroup.jpg")
cv.imshow('Original img',img)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

haar_cascade=cv.CascadeClassifier('facedetection.xml')
faces = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)


print(f'number of faces found ={len(faces)}')


for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("detected Faces",img)


cv.waitKey(0)