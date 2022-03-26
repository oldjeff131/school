import cv2 as cv
from cv2 import imshow
import numpy as np

def bilateral_filter(img):
    cv.imshow('original image',img)
    img_bi=cv.bilateralFilter(img,9,5,5)
    cv.imshow('')

image =cv.imread('image/1233.png')
clone=image.copy()
