import cv2 as cv

# reading imgs
img=cv.imread("photos/beautiful.jpg")
cv.imshow('tiger',img)
cv.waitKey(0) #wait for specific delay
# destroy all windows 

# reading images





# while True:
#     ret, frame = capture.read()
    
#     # Check if the frame is valid
#     if ret == False:
#         print("frame is not valid")
#         break
#     cv.imshow('Video', frame)
#     # Exit the loop if 'd' key is pressed or if the video ends
#     if cv.waitKey(20)& 0xFF == ord('d') or not ret:
#         break

# capture.release()
# cv.destroyAllWindows()

# print(cv.__version__)




# topic 2 : resizing & rescaling
#for live video resizing
# def changeRes(width,height):
#     capture.set(3,width)
#     capture.set(4, height)



#reshaping frame /img functions
# this will work with images,videos and live video
def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height =int(frame.shape[0] * scale)

    dimensions =(width,height)
    return cv.resize(frame,dimensions,interpolation =cv.INTER_AREA)



# img=cv.imread("photos/beautiful.jpg")
# cv.imshow('tiger',rescaleFrame(img,scale=0.20))
# cv.waitKey(0) #rescaled image




capture = cv.VideoCapture("videos/dog2.mp4")

while True:
    ret, frame = capture.read()
    resized_frame =rescaleFrame(frame,scale=0.20)
    # Check if the frame is valid
    if ret == False:
        print("frame is not valid")
        break
    cv.imshow('Video', resized_frame)
    # Exit the loop if 'd' key is pressed or if the video ends
    if cv.waitKey(20)& 0xFF == ord('d') or not ret:
        break
capture.release()
cv.destroyAllWindows()


# on image