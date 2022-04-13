# import the necessary packages
import cv2 as cv

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
    if event == cv.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
        print(refPt)
    elif event == cv.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        print(str(refPt[0])+str(refPt[1])+' '+str(refPt[0][1]))
        cv.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv.imshow("image", image)

# load the image, clone it, and setup the mouse callback function
image = cv.imread('opencv\cameraman.png')
clone = image.copy()
cv.namedWindow("image")
cv.setMouseCallback("image", click_and_crop)
while True:
    cv.imshow("image", image)
    key = cv.waitKey(1) & 0xFF
    if key == ord("r"):
        image = clone.copy()
    elif key == ord("c"):
        break
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv.imshow("ROI", roi)
    cv.waitKey(0)
# close all open windows
cv.destroyAllWindows()