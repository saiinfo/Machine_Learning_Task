import cv2 as cv
import numpy as np
blank =np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank', blank)



# blank[200:300,300:400]=0,0,255
# cv.imshow('green',blank)


cv.rectangle(blank,(0,0),(blank.shape[1]//2,500),(0,255,0),thickness=1)
cv.imshow('Rectangle',blank)

#draw circle
cv.circle(blank,(250,250),40,(0,0,255),thickness =-1)
cv.imshow('Circle',blank)

#draw line
cv.line(blank,(0,0),(250,250),(0,255,255),thickness=2) # 
cv.imshow("with line",blank)
cv.waitKey(0)


