import cv2 as cv
from cv2 import imshow
import numpy as np

def my_first_filter(img):
    kernel=np.ones((7,7),np.float32)/49
    #kernel=np.array([[1,1,1],[1,1,1],[1,1,1]])/9
    kernel1=np.array([
        [-1,-1,-1],
        [-1,8,-1],
        [-1,-1,-1]
    ])

    #Emboss filter
    kernel2=np.array([
        [-2,-1,0],
        [-1,1,1],
        [0,1,2]
    ])
    
    img_result=cv.filter2D(img,-1,kernel)
    img_result1=cv.filter2D(img,-1,kernel1)
    img_result2=cv.filter2D(img,-1,kernel2)
    cv.imshow('original image',img)
    cv.imshow('result image',img_result)
    cv.imshow('edge detection image',img_result1)
    cv.imshow('emboss image',img_result2)

    def averaging_filter(img):
        cv,imshow('original image',img)
        img_averaging=cv.blur(img,(5,5))
        cv.imshow('blur image',img_averaging)

    def gaussian_filter(img):
        cv,imshow('original image',img)
        img_gaussian_blur=cv.GaussianBlur(img,(11,11),-1)
        cv.imshow('Gaussian blur image',img_gaussian_blur)

    def laplacian_filter(img):
        cv.imshow('original image',img)
        gray_lap=cv.Laplacian(img,cv.CV_16S,ksize=5)
        img_laplacian=cv.convertScaleAbs(gray_lap)
        cv.imshow('Gaussian blur image',img_laplacian)
    
    def add_gaussian_noise(img):
        cv.imshow('original image',img)
        img=img/255
        mean=0
        sigma=0.1
        noise=np.random.normal(mean,sigma,img.shape)
        img_gaussian=img+noise
        img_gaussian=np.clip(img_gaussian,0,1)
        img_gaussian=np.uint8(img_gaussian*255)
        noise=np
        cv.imshow('Gaussian noise',noise)
        cv.imshow('noised image',img_gaussian)
        median_filter(img_gaussian)

        img_result=cv.fastNlMeansDenoising(img_gaussian,None,10,10,7)
        cv.imshow('')


img_ori=cv.imread('image/cameraman.png')
cv.imshow('original image',img_ori)
cv.waitKey()