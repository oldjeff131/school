# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1626, 736)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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