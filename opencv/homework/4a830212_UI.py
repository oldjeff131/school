import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import PyQtmain as pyqt
class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.graphicview = None
        self.qimg = None
        self.img = None
        self.img_path = None
        self.ui = pyqt.Ui_MainWindow()
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

