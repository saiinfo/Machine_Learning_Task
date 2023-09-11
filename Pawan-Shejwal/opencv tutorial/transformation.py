import cv2 as cv
import numpy as np


img = cv.imread('photos/family.jpg')



# cv.imshow("family ",img)
resized =cv.resize(img,(720,720),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized )


def translate(img,x,y):
    translMat =np.float32([[1,0,x],[0,1,y]])
    dimensions =(img.shape[1],img.shape[0])
    return cv.warpAffine(img,translMat,dimensions)

# -x --> left
# -y --> Up
#  x --> Right
#  y --> down


translated_img =translate(resized,100,100)

#cv.imshow('Translated',translated_img)
cv.waitKey(0)


#rotation
def rotate (img , angle ,rotPoint=None):

    (height,width) =img.shape[:2] 
    if rotPoint is None:
        rotPoint =(width//2,height//2)
    

    rotMat =cv.getRotationMatrix2D(rotPoint,angle,1.0)#scale value
    dimensions =(width,height)

    return cv.warpAffine(img,rotMat,dimensions)
rotate_img = rotate(resized,-45) #-90 for right and +90 for left rotation
#cv.imshow('Rotated',rotate_img)



#flipping
flipedImg = cv.flip(resized,0 )   # flip vertically
cv.imshow('Fliped Image ',flipedImg)


#cropping 
croppedImage = img [200 :700,300:400 ]
cv.imshow('Cropped',croppedImage)

cv.waitKey(0)



