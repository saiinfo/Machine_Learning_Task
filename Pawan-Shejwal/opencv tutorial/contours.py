import cv2 as cv

img =cv.imread("photos/cat.jpg")
cv.imshow("Cat",img)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('GRAY',gray)




blur =cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)


#canny
edges=cv.Canny(gray,125,255) #threshold 100 and max threshold is 30
cv.imshow("Edges",edges)


contours,heirarchies =cv.findContours(edges,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print (f'{len(contours)} countour(s) found:')


cv.waitKey(0)


