import sys
import cv2 as cv
import numpy as np
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow,QMenu,QFileDialog,QAction,QLabel, QGridLayout
from PyQt5.QtGui import QImage, QPixmap

class Window(QMainWindow):
    def __init__(self,parent=None): #視窗建立
        super().__init__(parent)
        self.setWindowTitle("test")
        self.resize(1000,800)
        self.intUI()
        self._createActions() 
        self._createMenuBar() #選單分類
        self._connectActions()

    def intUI(self):
        self.picturelabel = QLabel('picture',self)
        self.picturelabel.move(100,100)
        self.picturelabel.setGeometry(QRect(0, 0, 600, 400))
        layout = QGridLayout(self)
        layout.addWidget(self.picturelabel, 0, 0, 4, 4)

    def _createActions(self):#選單基礎設定
        self.OpenImageAction=QAction(self)
        self.OpenImageAction.setText("&Open_Image")
        self.ROIAction=QAction("&ROI",self)
        self.IeHmAction=QAction("&Image histogram",self)
        self.CrSeAction=QAction("&Color space",self)
        self.CrSuAction=QAction("&Color spaceMenu",self)
        self.ThgAction=QAction("&Thresholding",self)
        self.HmEnAction=QAction("&Histogram Equalization",self)

    def _createMenuBar(self):
        menuBar=self.menuBar()
        fileMenu=QMenu("&File",self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.OpenImageAction)

        SettingMenu=menuBar.addMenu("&Setting")#母選單
        SettingMenu.addAction(self.ROIAction)
        IeHmActionMenu=SettingMenu.addMenu("&IeHmAction")#子選單
        IeHmActionMenu.addAction("gray")
        IeHmActionMenu.addAction("hsv")     

        ImageMenu=menuBar.addMenu("&Image Processing")
        ImageMenu.addAction(self.CrSuAction)
        ImageMenu.addAction(self.ThgAction)
        ImageMenu.addAction(self.HmEnAction)

    def _connectActions(self):#按鍵觸發
        self.OpenImageAction.triggered.connect(self.openSlot)

    def openSlot(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Image', 'Image', '*.png *.jpg *.bmp')
        if filename is '':
            return
        self.img = cv.imread(filename, -1)
        if self.img.size == 1:
            return
        self.showImage()

    def showImage(self):
        height, width, Channel = self.img.shape
        bytesPerline = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.picturelabel.setPixmap(QPixmap.fromImage(self.qImg))
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())