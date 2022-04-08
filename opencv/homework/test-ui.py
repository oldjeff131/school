from fileinput import filename
import sys
import cv2 as cv
from cv2 import QT_CHECKBOX
import numpy as np
from matplotlib import pyplot as plt
from PyQt5.QtCore import QRect,Qt
from PyQt5.QtWidgets import QApplication, QMainWindow,QMenu,QFileDialog,QAction,QLabel, QGridLayout,QSlider
from PyQt5.QtGui import QImage, QPixmap
from scipy.misc import electrocardiogram

class Window(QMainWindow):
    def __init__(self,parent=None): #視窗建立
        super().__init__(parent)
        self.setWindowTitle("test")
        self.resize(1000,800)
        self.intUI()
        self._createActions() 
        self._createMenuBar() #選單分類
        self._connectActions()

    def intUI(self):#設定介面ui
        self.picturelabel = QLabel('picture',self)
        self.picturelabel.move(100,100)
        self.picturelabel.setGeometry(QRect(0, 0, 600, 400))
        self.picturelabe2 = QLabel('gary',self)
        self.picturelabe2.move(100,100)
        self.picturelabe2.setGeometry(QRect(600,60, 600, 400))
        self.picturelabe3 = QLabel('test',self)
        self.picturelabe3.move(100,100)
        self.picturelabe3.setGeometry(QRect(0, 350, 600, 400))
        self.sld=QSlider(Qt.Horizontal,self)
        self.sld.setGeometry(50,600,150,50)
        self.sld.setMinimum(0)
        self.sld.setMaximum(255)
        self.sld.setTickPosition(QSlider.TicksRight)
        self.sldvaluelabel=QLabel("0",self)
        self.sldvaluelabel.move(100,100)
        self.sldvaluelabel.setGeometry(QRect(50, 700, 50, 50))
        layout = QGridLayout(self)
        layout.addWidget(self.picturelabel, 0, 0, 4, 4)
        layout.addWidget(self.picturelabe2, 0, 0, 4, 4)
        layout.addWidget(self.picturelabe3, 0, 0, 4, 4)

    def _createActions(self):#選單基礎設定
        self.OpenImageAction=QAction(self)
        self.OpenImageAction.setText("&Open_Image")
        self.ROIAction=QAction("&ROI",self)
        self.IeHmAction=QAction("&Image histogram",self)
        self.grayAction=QAction("&gray",self)
        self.hsvAction=QAction("&hsv",self)
        self.ThgAction=QAction("&Thresholding",self)
        self.HmEnAction=QAction("&Histogram Equalization",self)
        self.InfoAction=QAction("&Info",self)

    def _createMenuBar(self): #選單設定
        menuBar=self.menuBar()
        fileMenu=QMenu("&File",self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.OpenImageAction)

        SettingMenu=menuBar.addMenu("&Setting")#母選單
        SettingMenu.addAction(self.ROIAction)
        SettingMenu.addAction(self.IeHmAction)
        IeHmActionMenu=SettingMenu.addMenu("&IeHmAction")#子選單
        IeHmActionMenu.addAction(self.grayAction)
        IeHmActionMenu.addAction(self.hsvAction)     

        ImageMenu=menuBar.addMenu("&Image Processing")
        ImageMenu.addAction(self.ThgAction)
        ImageMenu.addAction(self.HmEnAction)

    def _connectActions(self):#按鍵觸發
        self.OpenImageAction.triggered.connect(self.openSlot)
        self.ROIAction.triggered.connect(self.Roi_control)
        self.IeHmAction.triggered.connect(self.Histogram)
        self.grayAction.triggered.connect(self.Gray_control)
        self.hsvAction.triggered.connect(self.Hsv_control)
        self.ThgAction.triggered.connect(self.Thresholdingcontrol)
        self.HmEnAction.triggered.connect(self.Histogram_Equalization_control)
        self.sld.valueChanged[int].connect(self.changeValue)

    def openSlot(self): #載入的圖片
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Image', 'Image', '*.png *.jpg *.bmp')
        if filename is '':
            return
        self.img = cv.imread(filename, -1)
        self.img_path=filename
        if self.img.size == 1:
            return
        self.showImage()

    def showImage(self): #顯示載入的圖片
        height, width, Channel = self.img.shape
        bytesPerline = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabel.setPixmap(QPixmap.fromImage(self.qImg))
        self.picturelabe3.setPixmap(QPixmap.fromImage(self.qImg))
        
    def Roi_control(self): #ROI
        img = cv.imread(self.img_path)
        roi = cv.selectROI(windowName="ROI", img=img, showCrosshair=False, fromCenter=False)
        x, y, w, h = roi
        cv.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
        img_roi = img[int(y):int(y+h), int(x):int(x+w)]
        cv.imshow("roi", img)
        cv.imshow("roi_sel", img_roi)
        cv.waitKey(0)

    def Histogram(self): #影像直方圖
        img = cv.imread(self.img_path)
        plt.hist(img.ravel(), 256, [0, 256])
        plt.show()

    def Gray_control(self): #Gray
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        height, width = gray.shape
        bytesPerline = 1 * width
        self.qImg = QImage(gray, width, height, bytesPerline, QImage.Format_Grayscale8).rgbSwapped()
        self.picturelabe2.setPixmap(QPixmap.fromImage(self.qImg))
        self.picturelabe2.resize(self.qImg.size())

    def Hsv_control(self): #Hsv
        hsv = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
        height, width, channel = hsv.shape
        bytesPerline = 3 * width
        self.qImg = QImage(hsv, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabe2.setPixmap(QPixmap.fromImage(self.qImg))
        self.picturelabe2.resize(self.qImg.size())

    def Thresholdingcontrol(self):
        self.sldvaluelabel.setText(str(self.sld.value()))
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        ret, result = cv.threshold(gray, self.sld.value(), 255, cv.THRESH_BINARY)
        height, width = result.shape
        bytesPerline = 1 * width
        self.qimg = QImage(result, width, height, bytesPerline, QImage.Format_Grayscale8).rgbSwapped()
        self.picturelabe3.setPixmap(QPixmap.fromImage(self.qimg))
        self.picturelabe3.resize(self.qimg.size())
    
    def Histogram_Equalization_control (self):
        img = cv.imread(self.img_path)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('Original Image', gray)
        img_eq = cv.equalizeHist(gray)
        cv.imshow('Equalized Image', img_eq)
        plt.hist(gray.ravel(), 256, [0, 256])
        plt.hist(img_eq.ravel(), 256, [0, 256])
        plt.show()

    def changeValue(self,value):
        sender=self.sender()
        if sender==self.sld:
            self.sld.setValue(value)
        else:
            self.sld.setValue(value)
        self.sldvaluelabel.setText(str(value))
        self.Thresholdingcontrol()

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())