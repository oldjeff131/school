from fileinput import filename
import sys
import PyQt5
import cv2 as cv
from cv2 import QT_CHECKBOX
import numpy as np
from matplotlib import pyplot as plt
from PyQt5.QtCore import *#QRect,Qt
from PyQt5.QtWidgets import * #QApplication, QMainWindow,QMenu,QFileDialog,QAction,QLabel, QGridLayout,QSlider,QMessageBox
from PyQt5.QtGui import *#QImage, QPixmap
from pyrsistent import PTypeError
from scipy.misc import electrocardiogram

class Window(QMainWindow):
    def __init__(self,parent=None): #視窗建立
        super().__init__(parent)
        self.setWindowTitle("4a830212_opencv_homework")
        self.resize(1000,800)
        self.intUI()
        self._createActions() 
        self._createMenuBar() #選單分類
        self._connectActions()

    def intUI(self):#設定介面ui
        self.picturelabel = QLabel('picture',self)
        self.picturelabel.move(100,100)
        self.picturelabel.setGeometry(QRect(0, 0, 600, 400))

        self.picturelabe2 = QLabel('IeHmAction',self)
        self.picturelabe2.move(100,100)
        self.picturelabe2.setGeometry(QRect(300,100, 600, 400))

        self.picturelabe3 = QLabel('Thresholding',self)
        self.picturelabe3.move(100,100)
        self.picturelabe3.setGeometry(QRect(0, 350, 600, 400))

        self.picturelabe4 = QLabel('filter',self)
        self.picturelabe4.move(100,100)
        self.picturelabe4.setGeometry(QRect(300, 280, 600, 400))

        self.sld=QSlider(Qt.Horizontal,self)
        self.sld.setGeometry(50,600,150,50)
        self.sld.setMinimum(0)
        self.sld.setMaximum(255)
        self.sld.setTickPosition(QSlider.TicksRight)

        self.sldvaluelabel=QLabel("0",self)
        self.sldvaluelabel.move(100,100)
        self.sldvaluelabel.setGeometry(QRect(25, 600, 50, 50))

        self.sld1=QSlider(Qt.Horizontal,self)
        self.sld1.setGeometry(250,600,200,50)
        self.sld1.setMinimum(-360)
        self.sld1.setMaximum(360)
        self.sld1.setTickPosition(QSlider.TicksRight)

        self.sldvaluelabel1=QLabel("0",self)
        self.sldvaluelabel1.move(100,100)
        self.sldvaluelabel1.setGeometry(QRect(225, 600, 50, 50))

        self.Txvaluelabel1=QLabel("Tx:",self)
        self.Txvaluelabel1.move(20, 20)
        self.Txvaluelabel1.setGeometry(QRect(280, 670, 50, 25))

        self.Txtextbox = QLineEdit(self)
        self.Txtextbox.move(20, 20)
        self.Txtextbox.setGeometry(300,670,50,25)

        self.Tyvaluelabel1=QLabel("Ty:",self)
        self.Tyvaluelabel1.move(20, 20)
        self.Tyvaluelabel1.setGeometry(QRect(280, 700, 50, 25))

        self.Tytextbox = QLineEdit(self)
        self.Tytextbox.move(20, 20)
        self.Tytextbox.setGeometry(300,700,50,25)

        self.Sizevaluelabel1=QLabel("圖片縮放:",self)
        self.Sizevaluelabel1.move(20, 20)
        self.Sizevaluelabel1.setGeometry(QRect(25, 700, 50, 25))

        self.Sizetextbox = QLineEdit(self)
        self.Sizetextbox.move(20, 20)
        self.Sizetextbox.setGeometry(90,700,50,25)

        layout = QGridLayout(self)
        layout.addWidget(self.picturelabel, 0, 0, 4, 4)
        layout.addWidget(self.picturelabe2, 0, 0, 4, 4)
        layout.addWidget(self.picturelabe3, 0, 0, 4, 4)

    def _createActions(self):#選單基礎設定
        self.OpenImageAction=QAction(self)
        self.OpenImageAction.setText("&開啟圖片\n(Open_Image)")
        self.ROIAction=QAction("&ROI",self)
        self.IeHmAction=QAction("&圖片直方圖(Image histogram)",self)
        self.grayAction=QAction("&Gray",self)
        self.hsvAction=QAction("&Hsv",self)
        self.rgbAction=QAction("&Rgb",self)
        self.bgrAction=QAction("&Bgr",self)
        self.ThgAction=QAction("&Thresholding",self)
        self.HmEnAction=QAction("&Histogram Equalization",self)
        self.InfoAction=QAction("&影像資訊(Info)",self)
        self.FHAction=QAction("&垂直翻轉(Horizontal)",self)
        self.FVAction=QAction("&水平翻轉(Vertically)",self)
        self.FLAction=QAction("&向左翻轉(Left)",self)
        self.FRAction=QAction("&向右翻轉(Right)",self)
        self.ATAction=QAction("&訪射轉換(Affine)",self)
        self.MFAction=QAction("&均值濾波(Mean Filtering)",self)
        self.GFAction=QAction("&高斯濾波(Gaussian Filtering)",self)
        self.MBAction=QAction("&中值濾波(MedianBlur)",self)
        self.BFAction=QAction("&雙邊濾波(Bilateral filter)",self)
        self.LPFAction=QAction("&低通濾波(Low-Pass Filter)",self)
        self.HPFAction=QAction("&高通濾波(High-Pass Filter)",self)
        self.ReloadAction=QAction("&重新載入(Reload)",self)
        self.TLAction=QAction("&平移(TransLation)",self)

    def _createMenuBar(self): #選單設定
        menuBar=self.menuBar()
        fileMenu=QMenu("&檔案(File)",self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.OpenImageAction)
        fileMenu.addAction(self.ReloadAction)
        fileMenu.addAction(self.InfoAction)

        SettingMenu=menuBar.addMenu("&設定(Setting)")#母選單
        SettingMenu.addAction(self.ROIAction)
        SettingMenu.addAction(self.IeHmAction)
        IeHmActionMenu=SettingMenu.addMenu("&色彩空間(IeHmAction)")#子選單
        IeHmActionMenu.addAction(self.grayAction)
        IeHmActionMenu.addAction(self.hsvAction)
        IeHmActionMenu.addAction(self.bgrAction)
        IeHmActionMenu.addAction(self.rgbAction)
        RotateActionMenu=SettingMenu.addMenu("&旋轉(Rotate)")#旋轉選單
        RotateActionMenu.addAction(self.FHAction)#水平
        RotateActionMenu.addAction(self.FVAction)#垂直
        RotateActionMenu.addAction(self.FLAction)#翻轉90度
        RotateActionMenu.addAction(self.FRAction)#翻轉270度
        SettingMenu.addAction(self.TLAction)#平移
        SettingMenu.addAction(self.ATAction)#訪射轉換
     

        ImageMenu=menuBar.addMenu("&Image Processing")
        ImageMenu.addAction(self.ThgAction)
        ImageMenu.addAction(self.HmEnAction)
        FilteringActionMenu=ImageMenu.addMenu("&濾波(Filtering)")#濾波
        FilteringActionMenu.addAction(self.LPFAction)
        FilteringActionMenu.addAction(self.HPFAction)
        FilteringActionMenu.addAction(self.MFAction)#均值濾波
        FilteringActionMenu.addAction(self.GFAction)#高斯濾波
        FilteringActionMenu.addAction(self.MBAction)#中值濾波
        FilteringActionMenu.addAction(self.BFAction)#雙邊濾波

    def _connectActions(self):#按鍵觸發
        self.OpenImageAction.triggered.connect(self.openSlot)
        self.InfoAction.triggered.connect(self.pictureinfo)
        self.ReloadAction.triggered.connect(self.showImage)
        self.ROIAction.triggered.connect(self.Roi_control)
        self.IeHmAction.triggered.connect(self.Histogram)
        self.grayAction.triggered.connect(self.Gray_control)
        self.hsvAction.triggered.connect(self.Hsv_control)
        self.rgbAction.triggered.connect(self.Rgb_control)
        self.bgrAction.triggered.connect(self.Bgr_control)
        self.ThgAction.triggered.connect(self.Thresholdingcontrol)
        self.HmEnAction.triggered.connect(self.Histogram_Equalization_control)
        self.sld.valueChanged[int].connect(self.changeValue)
        self.sld1.valueChanged[int].connect(self.changeRotaValue)
        self.FHAction.triggered.connect(self.pictureFHflip)
        self.FVAction.triggered.connect(self.pictureFVflip)
        self.FRAction.triggered.connect(self.pictureFRflip)
        self.FLAction.triggered.connect(self.pictureFLflip)
        self.TLAction.triggered.connect(self.PictureTranslation)
        self.HPFAction.triggered.connect(self.Low_Pass_Filter)
        self.LPFAction.triggered.connect(self.High_Pass_Filter)
        self.MFAction.triggered.connect(self.Mean_Filtering)
        self.GFAction.triggered.connect(self.Gaussia_Filtering)
        self.MBAction.triggered.connect(self.MedianBlur)
        self.BFAction.triggered.connect(self.Bilateral_filter)

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
    
    def Rgb_control(self): #Rgb
        rgb = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
        height, width, channel = rgb.shape
        bytesPerline = 3 * width
        self.qImg = QImage(rgb, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabe2.setPixmap(QPixmap.fromImage(self.qImg))
        self.picturelabe2.resize(self.qImg.size())

    def Bgr_control(self): #Bgr
        bgr = cv.cvtColor(self.img, cv.COLOR_RGB2BGR)
        height, width, channel = bgr.shape
        bytesPerline = 3 * width
        self.qImg = QImage(bgr, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
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

    def changeRotaValue(self,value):
        sender=self.sender()
        if sender==self.sld:
            self.sld1.setValue(value)
        else:
            self.sld1.setValue(value)
        self.sldvaluelabel1.setText(str(value))
        self.PictureRotaControl()

    def pictureinfo(self):#圖片資訊
        img = cv.imread(self.img_path)
        size=img.shape
        QMessageBox.information(self,"Picture_info",str(size)+"\n(高度,寬度,像素)")

    def PictureRotaControl(self):#角度調整
        self.sldvaluelabel1.setText(str(self.sld1.value()))
        img = cv.imread(self.img_path)
        height, width, channel = img.shape
        center = (width // 2, height // 2)
        Pictureflip=cv.getRotationMatrix2D(center,self.sld1.value(),1.0)
        Pictureflip = cv.warpAffine(img, Pictureflip, (width, height))
        bytesPerline = 3 * width
        Pictureflip = QImage(Pictureflip.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabel.setPixmap(QPixmap.fromImage(Pictureflip))

    def pictureFHflip(self): #垂直翻轉
        img = cv.imread(self.img_path)
        Pictureflip = cv.flip(img, 0)
        height, width, channel = img.shape
        bytesPerline = 3 * width
        Pictureflip = QImage(Pictureflip.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabel.setPixmap(QPixmap.fromImage(Pictureflip))

    def pictureFVflip(self): #水平翻轉
        img = cv.imread(self.img_path)
        Pictureflip = cv.flip(img, 1)
        height, width, channel = img.shape
        bytesPerline = 3 * width
        Pictureflip = QImage(Pictureflip.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabel.setPixmap(QPixmap.fromImage(Pictureflip))

    def pictureFLflip(self): #左翻翻轉
        img = cv.imread(self.img_path)
        height, width, channel = img.shape
        center = (width // 2, height // 2)
        Pictureflip=cv.getRotationMatrix2D(center,-90,1.0)
        Pictureflip = cv.warpAffine(img, Pictureflip, (width, height))
        bytesPerline = 3 * width
        Pictureflip = QImage(Pictureflip.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabel.setPixmap(QPixmap.fromImage(Pictureflip))
         
    def pictureFRflip(self): #右翻翻轉
        img = cv.imread(self.img_path)
        height, width, channel = img.shape
        center = (width // 2, height // 2)
        Pictureflip = cv.getRotationMatrix2D(center,90,1.0)
        Pictureflip = cv.warpAffine(img, Pictureflip, (width, height))
        bytesPerline = 3 * width
        Pictureflip = QImage(Pictureflip.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabel.setPixmap(QPixmap.fromImage(Pictureflip))

    def PictureTranslation(self):#平移
        img = cv.imread(self.img_path)
        rows, cols = img.shape[:2]
        affine = np.float32([[1, 0, int(self.Txtextbox.text())], [0, 1, int(self.Tytextbox.text())]])
        dst = cv.warpAffine(img, affine, (cols, rows))
        cv.imshow("original", img)
        cv.imshow("Translation", dst)

    def Low_Pass_Filter(self):
        img = cv.imread(self.img_path)
        height, width, channel = img.shape
        bytesPerline = 3 * width
        img_Mean = QImage(img_Mean.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabe4.setPixmap(QPixmap.fromImage(img_Mean))

    def High_Pass_Filter(self):
        img = cv.imread(self.img_path)
        height, width, channel = img.shape
        bytesPerline = 3 * width
        img_Mean = QImage(img_Mean.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabe4.setPixmap(QPixmap.fromImage(img_Mean))

    def Mean_Filtering(self):#均值濾波 blur() boxFilter()
        img = cv.imread(self.img_path)
        height, width, channel = img.shape
        img_Mean=cv.blur(img,(5,5))
        bytesPerline = 3 * width
        img_Mean = QImage(img_Mean.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabe4.setPixmap(QPixmap.fromImage(img_Mean))
        
    
    def Gaussia_Filtering(self):#高斯濾波
        img = cv.imread(self.img_path)
        height, width, channel = img.shape
        img_Gaussia=cv.GaussianBlur(img,(5,5),5)
        bytesPerline = 3 * width
        img_Gaussia = QImage(img_Gaussia.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabe4.setPixmap(QPixmap.fromImage(img_Gaussia))
    
    def MedianBlur(self):#中值濾波
        img = cv.imread(self.img_path)
        height, width, channel = img.shape
        bytesPerline = 3 * width
        img_Mean = QImage(img_Mean.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabe4.setPixmap(QPixmap.fromImage(img_Mean))
    
    def Bilateral_filter(self):
        img = cv.imread(self.img_path)
        height, width, channel = img.shape
        img_Gaussia=cv.GaussianBlur(img,(5,5),9)
        img_Bilateral=cv.bilateralFilter(img_Gaussia,50,50,50)
        bytesPerline = 3 * width
        img_Bilateral = QImage(img_Bilateral.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabe4.setPixmap(QPixmap.fromImage(img_Bilateral))
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())