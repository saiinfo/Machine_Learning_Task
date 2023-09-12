import cv2
import numpy as np
# print(cv2.__version__)

# for reading and showing the image
# dd=cv2.imread("img/laptop.jpeg")
# cv2.imshow("hh",dd)
# dd[:, :, 2] =0 
# cv2.waitKey(0)

# for converting image in grey
# gray_image = cv2.cvtColor(dd, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale', gray_image)
# cv2.waitKey(0)    
# print(dd)

# playing with RGB colour channel
# imgBlue = dd[:, :, 0]
# imgGreen = dd[:, :, 1]
# imgRed = dd[:, :, 2]
# new_img = np.hstack((imgBlue, imgGreen, imgRed))
# cv2.imshow("window",new_img)
# cv2.waitKey(0)

# resizing the image
# img_resize = cv2.resize(dd,(256,256))
# img_resize = cv2.resize(dd, (dd.shape[1]//2, dd.shape[0]//2))
# cv2.imshow("window", img_resize)
# print(img_resize.shape)
# cv2.waitKey(0)

# flipping an image
# img_flip = cv2.flip(dd,0)
# img_flip = cv2.flip(dd,1)
# img_flip = cv2.flip(dd,-1)
# cv2.imshow("window", img_flip)
# cv2.waitKey(0)

# cropping an image
# img_crop = dd[100:300, 200:500]
# cv2.imshow("window", img_crop)
# cv2.waitKey(0)

# saving the image
# img_crop = dd[0:300, 0:300]
# cv2.imwrite('laptop_small.png', img_crop)
# cv2.imshow("window", img_crop)
# cv2.waitKey(0)

# drawing shapes
# img = np.zeros((512, 512, 3))
# cv2.rectangle(img, pt1 = (100,100), pt2 = (300,300), color = (255,0,0), thickness = 3)
# cv2.circle(img, center = (100,400), radius = 50, color = (0, 0, 255), thickness = 3)
# cv2.line(img, pt1 = (0, 0), pt2 = (512, 512), color = (0, 255, 0), thickness = 2)
# cv2.putText(img, org = (00,100),fontScale=4, color = (0,255, 255), thickness = 2, lineType = cv2.LINE_AA, text= "Hello", fontFace = cv2.FONT_ITALIC)
# cv2.imshow('window', img)
# cv2.waitKey(0)

# live direct drawing
# def draw(event, x, y, flags, params):
    # print("Event triggered")
    # print("event")
    # if event == 0:
        # print("Mouse moved")
    # if event == 1:
    #     print("Mouse down clicked")
    #  if event == 4:
    #      print("Mouse up clicked")
#     if event == 1:
#         cv2.circle(img, center = (x, y), radius = 50, color = (0, 0, 255), thickness = -1)

# cv2.namedWindow(winname="window")
# cv2.setMouseCallback("window", draw)
# img = np.zeros((512, 512, 3))
# while True:
#     cv2.imshow("window", img)
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break
# cv2.destroysAllWindows()
