import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("4a830212")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 600, 532))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 10, 600, 400))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.sld = QtWidgets.QSlider(self.centralwidget)
        self.sld.setGeometry(QtCore.QRect(80, 620, 251, 51))
        self.sld.setMaximum(255)
        self.sld.setOrientation(QtCore.Qt.Horizontal)
        self.sld.setObjectName("sld")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 620, 51, 51))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 570, 91, 31))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1626, 25))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Setting = QtWidgets.QMenu(self.menubar)
        self.menu_Setting.setObjectName("menu_Setting")
        self.menu_2 = QtWidgets.QMenu(self.menu_Setting)
        self.menu_2.setObjectName("menu_2")
        self.menu_Image_Processing = QtWidgets.QMenu(self.menubar)
        self.menu_Image_Processing.setObjectName("menu_Image_Processing")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action123 = QtWidgets.QAction(MainWindow)
        self.action123.setObjectName("action123")
        self.fileopen = QtWidgets.QAction(MainWindow)
        self.fileopen.setObjectName("fileopen")
        self.action123_2 = QtWidgets.QAction(MainWindow)
        self.action123_2.setObjectName("action123_2")
        self.ROIset = QtWidgets.QAction(MainWindow)
        self.ROIset.setObjectName("ROIset")
        self.Histogram = QtWidgets.QAction(MainWindow)
        self.Histogram.setObjectName("Histogram")
        self.Thresholding = QtWidgets.QAction(MainWindow)
        self.Thresholding.setObjectName("Thresholding")
        self.histogram_equalization = QtWidgets.QAction(MainWindow)
        self.histogram_equalization.setObjectName("histogram_equalization")
        self.gray = QtWidgets.QAction(MainWindow)
        self.gray.setObjectName("gray")
        self.gray_2 = QtWidgets.QAction(MainWindow)
        self.gray_2.setObjectName("gray_2")
        self.hsv_2 = QtWidgets.QAction(MainWindow)
        self.hsv_2.setObjectName("hsv_2")
        self.menu_File.addAction(self.fileopen)
        self.menu_File.addAction(self.action123_2)
        self.menu_2.addAction(self.gray_2)
        self.menu_2.addAction(self.hsv_2)
        self.menu_Setting.addAction(self.ROIset)
        self.menu_Setting.addAction(self.Histogram)
        self.menu_Setting.addAction(self.menu_2.menuAction())
        self.menu_Image_Processing.addAction(self.Thresholding)
        self.menu_Image_Processing.addAction(self.histogram_equalization)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Setting.menuAction())
        self.menubar.addAction(self.menu_Image_Processing.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("4a830212", "4a830212"))
        self.label_4.setText(_translate("MainWindow", "二值化閥值"))
        self.menu_File.setTitle(_translate("MainWindow", "檔案(File)"))
        self.menu_Setting.setTitle(_translate("MainWindow", "設定(Setting)"))
        self.menu_2.setTitle(_translate("MainWindow", "改變色彩空間"))
        self.menu_Image_Processing.setTitle(_translate("MainWindow", "影像處理(Image Processing)"))
        self.action123.setText(_translate("MainWindow", "123"))
        self.action123.setIconText(_translate("MainWindow", "開啟圖片"))
        self.fileopen.setText(_translate("MainWindow", "開啟圖片"))
        self.action123_2.setText(_translate("MainWindow", "儲存圖片"))
        self.ROIset.setText(_translate("MainWindow", "設定ROI"))
        self.Histogram.setText(_translate("MainWindow", "顯示影像直方圖"))
        self.Histogram.setIconText(_translate("MainWindow", "顯示影像直方圖"))
        self.Thresholding.setText(_translate("MainWindow", "影像二值化"))
        self.histogram_equalization.setText(_translate("MainWindow", "直方圖等化"))
        self.gray.setText(_translate("MainWindow", "gray"))
        self.gray_2.setText(_translate("MainWindow", "gray"))
        self.hsv_2.setText(_translate("MainWindow", "hsv"))

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.graphicview = None
        self.qimg = None
        self.img = None
        self.img_path = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.fileopen.triggered.connect(self.open_file)
        self.ui.ROIset.triggered.connect(self.ROI)
        self.ui.Histogram.triggered.connect(self.show_gray_histogram)
        self.ui.histogram_equalization.triggered.connect(self.histogram)
        self.ui.gray_2.triggered.connect(self.gray)
        self.ui.hsv_2.triggered.connect(self.hsv)
        self.ui.Thresholding.triggered.connect(self.Thresholding)
        self.ui.sld.valueChanged[int].connect(self.Thresholding)

    def display_img(self):
        self.img = cv.imread(self.img_path)
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.label.setPixmap(QPixmap.fromImage(self.qimg))
        self.ui.label.resize(self.qimg.size())

    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.img_path = filename
        self.display_img()

    def ROI(self):
        img = cv.imread(self.img_path)
        roi = cv.selectROI(windowName="roi", img=img, showCrosshair=False, fromCenter=False)
        x, y, w, h = roi
        cv.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
        img_roi = img[int(y):int(y+h), int(x):int(x+w)]
        cv.imshow("roi", img)
        cv.imshow("roi_sel", img_roi)
        cv.waitKey(0)

    def show_gray_histogram(self):
        img = cv.imread(self.img_path)
        plt.hist(img.ravel(), 256, [0, 256])
        plt.show()


    def histogram(self):
        img = cv.imread(self.img_path)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('original image', gray)
        img_eq = cv.equalizeHist(gray)
        cv.imshow('equalized image', img_eq)
        plt.hist(gray.ravel(), 256, [0, 256])
        plt.hist(img_eq.ravel(), 256, [0, 256])
        plt.show()

    def gray(self):
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        height, width = gray.shape
        bytesPerline = 1 * width
        self.qimg = QImage(gray, width, height, bytesPerline, QImage.Format_Grayscale8).rgbSwapped()
        self.ui.label_2.setPixmap(QPixmap.fromImage(self.qimg))
        self.ui.label_2.resize(self.qimg.size())

    def hsv(self):
        hsv = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
        height, width, channel = hsv.shape
        bytesPerline = 3 * width
        self.qimg = QImage(hsv, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.label_2.setPixmap(QPixmap.fromImage(self.qimg))
        self.ui.label_2.resize(self.qimg.size())

    def Thresholding(self):
        self.ui.label_3.setText(str(self.ui.sld.value()))
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        ret, result = cv.threshold(gray, self.ui.sld.value(), 255, cv.THRESH_BINARY)
        height, width = result.shape
        bytesPerline = 1 * width
        self.qimg = QImage(result, width, height, bytesPerline, QImage.Format_Grayscale8).rgbSwapped()
        self.ui.label_2.setPixmap(QPixmap.fromImage(self.qimg))
        self.ui.label_2.resize(self.qimg.size())


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())

