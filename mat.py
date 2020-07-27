#call the pakages we need

import argparse
import cv2
import imutils

#define the coordinate of x, y and click is not happened or not correct

noqte=()
click=False

#define the mouse function and variables

def clik_cut(event,x,y,flags,param):

    global noqte,click
    
    #if click was left double click perform the commands

    if event == cv2.EVENT_LBUTTONDBLCLK:

        noqte=(x,y)
        click = True
        
        #cut the picture and show it

        crop=image[y-50:y+200,x-50:x+200]
        cv2.imshow("cutt",crop)
        
        #blur the picture and show it

        blurred=cv2.blur(crop,(7,7))
        cv2.imshow("mut",blurred)
        cv2.waitKey(0)

    #if we press double click right it was false and do not save any coordinates

    elif event == cv2.EVENT_RBUTTONDBLCLK:

        noqte=()
        click=False
        
 #read the picture and find its path
        
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#create a new window and show the image on it and call hte function clik_cut

cv2.namedWindow("image")
cv2.setMouseCallback("image",clik_cut)

#out of loop with press key q

while True:

    cv2.imshow("image",image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

#close all windows

cv2.destroyAllWindows()