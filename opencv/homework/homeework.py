import sys
import cv2 as cv
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow,QMenu,QAction

class Window(QMainWindow):
    def __init__(self,parent=None): #視窗建立
        super().__init__(parent)
        self.setWindowTitle("test")
        self.resize(1000,800)
        self._createMenuBar()
        self._createToolBar()

    def _createMenuBar(self): #選單
        menuBar=self.menuBar()
        fileMenu=QMenu("&File",self)
        menuBar.addMenu(fileMenu)
        SettingMenu=menuBar.addMenu("&Setting")
        ImageMenu=menuBar.addMenu("&Image Processing")
    
    def _createToolBar(self):
        fileToolbar=self.addToolBar("File")
        editToolbar=QToolBar("Setting",self)
        self.addToolBar(editToolBar)
        helpToolBar = QToolBar("Image Processing", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

    def _createActions(self):
        self.newAction=QAction(self)
        self.newAction.setText("&OpenImage")
        self.ROIAction=QAction("&ROI",self)
        self.IHAction=QAction("&Image histogram",self)
        self.CSAction=QAction("&Color space",self)
        self.THAction = QAction("&Thresholding", self)
        self.HEAction = QAction("&Histogram Equalization", self)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())