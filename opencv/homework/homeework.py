import sys
import cv2 as cv
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow,QMenu,QToolBar

class Window(QMainWindow):
    def __init__(self,parent=None): #視窗建立
        super().__init__(parent)
        self.setWindowTitle("test")
        self.resize(400,200)
        self._createMenuBar()

    def _createMenuBar(self): #選單
        menuBar=self.menuBar()
        fileMenu=QMenu("&File",self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.openAction)
        SettingMenu=menuBar.addMenu("&Setting")
        SettingMenu.addActions(self.SettingROI)
        SettingMenu.addActions(self.Image_histogram)
        SettingMenu.addActions(self.Color_space)
        ImageMenu=menuBar.addMenu("&Image Processing")
    

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())