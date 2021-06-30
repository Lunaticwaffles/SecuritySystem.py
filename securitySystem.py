#open cv2 is a huge python library which can be used to capture images, manipulate images, and perfom kind of image processing work.
import cv2
import time
import random
start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number)+ ".png"
        #cv2.imwrite() method is used to save an image to any storage device
        #it takes two parameters, first is file name: must include image format like .jpg, .png, etc. Second parameter is the image that is to be saved
        #and after that result has been set to false, to break the while loop
        cv2.imwrite("newPicture1.jpg", frame)
        start_time = time.time
        result = False
    return img_name
    print("SnapShot Taken")
        #releases the camera
    videoCaptureObject.release()
    #closes all the windows that might be open while this process
    cv2.destroyAllWindows()
take_snapshot()