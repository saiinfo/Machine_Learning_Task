import cv2 as cv
import matplotlib.pyplot as plt
img =cv.imread("photos/ladybugs.jpg")
cv.imshow("Cat",img)

#grayscale
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#GRayscale histograph

gray_list = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_list)
plt.xlim([0,256])
plt.show()


cv.waitKey(0)