# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Wed May 31 20:27:12 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(699, 502)
        MainWindow.setMinimumSize(QtCore.QSize(699, 502))
        MainWindow.setMaximumSize(QtCore.QSize(699, 502))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 681, 441))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.sheet = QtGui.QWidget()
        self.sheet.setObjectName(_fromUtf8("sheet"))
        self.music_info = QtGui.QTextBrowser(self.sheet)
        self.music_info.setGeometry(QtCore.QRect(10, 161, 661, 231))
        self.music_info.setObjectName(_fromUtf8("music_info"))
        self.music_location_in_sheet = QtGui.QLineEdit(self.sheet)
        self.music_location_in_sheet.setGeometry(QtCore.QRect(110, 20, 501, 27))
        self.music_location_in_sheet.setObjectName(_fromUtf8("music_location_in_sheet"))
        self.label = QtGui.QLabel(self.sheet)
        self.label.setGeometry(QtCore.QRect(13, 20, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.selected_meusic_in_sheet = QtGui.QToolButton(self.sheet)
        self.selected_meusic_in_sheet.setGeometry(QtCore.QRect(620, 20, 23, 25))
        self.selected_meusic_in_sheet.setObjectName(_fromUtf8("selected_meusic_in_sheet"))
        self.startButtonInSheet = QtGui.QPushButton(self.sheet)
        self.startButtonInSheet.setGeometry(QtCore.QRect(540, 70, 98, 27))
        self.startButtonInSheet.setObjectName(_fromUtf8("startButtonInSheet"))
        self.label_4 = QtGui.QLabel(self.sheet)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 91, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.sheet, _fromUtf8(""))
        self.info = QtGui.QWidget()
        self.info.setObjectName(_fromUtf8("info"))
        self.music_location_in_musicinfo = QtGui.QLineEdit(self.info)
        self.music_location_in_musicinfo.setGeometry(QtCore.QRect(110, 40, 501, 27))
        self.music_location_in_musicinfo.setObjectName(_fromUtf8("music_location_in_musicinfo"))
        self.selected_music_in_musicinfo = QtGui.QToolButton(self.info)
        self.selected_music_in_musicinfo.setGeometry(QtCore.QRect(620, 40, 23, 25))
        self.selected_music_in_musicinfo.setObjectName(_fromUtf8("selected_music_in_musicinfo"))
        self.label_2 = QtGui.QLabel(self.info)
        self.label_2.setGeometry(QtCore.QRect(13, 40, 91, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.featureComboBox = QtGui.QComboBox(self.info)
        self.featureComboBox.setGeometry(QtCore.QRect(110, 90, 121, 27))
        self.featureComboBox.setObjectName(_fromUtf8("featureComboBox"))
        self.featureComboBox.addItem(_fromUtf8(""))
        self.featureComboBox.addItem(_fromUtf8(""))
        self.featureComboBox.addItem(_fromUtf8(""))
        self.featureComboBox.addItem(_fromUtf8(""))
        self.featureComboBox.addItem(_fromUtf8(""))
        self.featureComboBox.addItem(_fromUtf8(""))
        self.featureComboBox.addItem(_fromUtf8(""))
        self.startButtonInMusicInfo = QtGui.QPushButton(self.info)
        self.startButtonInMusicInfo.setGeometry(QtCore.QRect(530, 90, 98, 27))
        self.startButtonInMusicInfo.setObjectName(_fromUtf8("startButtonInMusicInfo"))
        self.label_3 = QtGui.QLabel(self.info)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.info, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.exit = QtGui.QAction(MainWindow)
        self.exit.setObjectName(_fromUtf8("exit"))
        self.menu.addAction(self.exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "民族音乐信息提取系统", None))
        self.label.setText(_translate("MainWindow", "音乐文件路径", None))
        self.selected_meusic_in_sheet.setText(_translate("MainWindow", "...", None))
        self.startButtonInSheet.setText(_translate("MainWindow", "开始提取", None))
        self.label_4.setText(_translate("MainWindow", "提取信息展示", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sheet), _translate("MainWindow", "乐谱", None))
        self.selected_music_in_musicinfo.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "音乐文件路径", None))
        self.featureComboBox.setItemText(0, _translate("MainWindow", "MFCC", None))
        self.featureComboBox.setItemText(1, _translate("MainWindow", "MFCC_D1", None))
        self.featureComboBox.setItemText(2, _translate("MainWindow", "Sharpness", None))
        self.featureComboBox.setItemText(3, _translate("MainWindow", "ZCR", None))
        self.featureComboBox.setItemText(4, _translate("MainWindow", "Energy", None))
        self.featureComboBox.setItemText(5, _translate("MainWindow", "SpectralRolloff", None))
        self.featureComboBox.setItemText(6, _translate("MainWindow", "spectralFlatness", None))
        self.startButtonInMusicInfo.setText(_translate("MainWindow", "开始提取", None))
        self.label_3.setText(_translate("MainWindow", "提取信息", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.info), _translate("MainWindow", "音乐信息", None))
        self.menu.setTitle(_translate("MainWindow", "菜单", None))
        self.exit.setText(_translate("MainWindow", "退出", None))

