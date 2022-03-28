import sys
import cv2 as cv
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow,QAction,QMenu

class Window(QMainWindow):
    def __init__(self,parent=None): #視窗建立
        super().__init__(parent)
        self.setWindowTitle("test")
        self.resize(1000,800)
        self._createMenuBar()

    def _createMenuBar(self): #選單
        menuBar=self.menuBar()
        fileMenu=menuBar.addMenu('File')
        OpenImageMenu=QMenu("&OpenImage",self)
        fileMenu.addMenu(OpenImageMenu)

        SettingMenu=menuBar.addMenu("&Setting")
        ROIMenu=QMenu("&ROI",self)
        SettingMenu.addMenu(ROIMenu)
        IHAMenu=QMenu("&Image histogram",self)
        SettingMenu.addMenu(IHAMenu)
        Image_histogramMenu=QMenu("&Color space",self)
        SettingMenu.addMenu(Image_histogramMenu)

        ImageMenu=menuBar.addMenu("&Image Processing")
        Color_spaceMenu=QMenu("&Color spaceMenu",self)
        ImageMenu.addMenu(Color_spaceMenu)
        ThresholdingMenu=QMenu("&Thresholding",self)
        ImageMenu.addMenu(ThresholdingMenu)
        Histogram_EqualizationMenu=QMenu("&Histogram Equalization",self)
        ImageMenu.addMenu(Histogram_EqualizationMenu)

    def open_image(self):
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())