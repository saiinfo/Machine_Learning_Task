
import cv2 as cv
img=cv.imread("photos/tiger.jpg")
def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height =int(frame.shape[0] * scale)

    dimensions =(width,height)
    return cv.resize(frame,dimensions,interpolation =cv.INTER_AREA)

dchangedimg=rescaleFrame(img,scale=0.20)
cv.imshow('tiger',dchangedimg)
#greyscale img
grayImg=cv.cvtColor(dchangedimg,cv.COLOR_BGR2GRAY) #converting to grayscale
cv.imshow("gray",grayImg)

#blur image
blur_img=cv.GaussianBlur(dchangedimg,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur_img)

#Edgecascade
cannyedimage=cv.Canny(dchangedimg,threshold1=30,threshold2=40)#finding edges in the
cv.imshow('Canny edges',cannyedimage)

#dilating edges
kernel=(9,9)  #(x,y)
dilation=cv.dilate(cannyedimage,kernel,iterations=1)   ## dilates the canny edge
cv.imshow('Dilated Image',dilation)

#eroding
erosion=cv.erode(dilation,kernel,iterations=1)    ### erodes the dilation
cv.imshow('Eroded',erosion)

#resized
resized =cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized )

#Crapping
cropped =img[50:200,200:400]
cv.imshow('Croped', cropped)

cv.waitKey(0)