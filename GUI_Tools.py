#! /usr/bin/python2.7
# coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import MusicTools
import sys
import ui
import matplotlib.pyplot as plt
import numpy as np
import wave
import eyed3
import os


class Windows(QMainWindow, ui.Ui_MainWindow):
    FilePath = ""
    selectedMethod = ""

    def __init__(self, parent=None):
        super(Windows, self).__init__(parent)
        self.musicFile = ""
        self.setupUi(self)
        self.ButtionActionConnect()

    def ButtionActionConnect(self):
        QObject.connect(self.selected_meusic_in_sheet, SIGNAL("clicked()"), self.openMusicFileInSheet)
        QObject.connect(self.selected_music_in_musicinfo, SIGNAL("clicked()"), self.openMusicFileInMusicInfo)
        QObject.connect(self.startButtonInSheet, SIGNAL("clicked()"), self.musicToSheet)
        QObject.connect(self.startButtonInMusicInfo, SIGNAL("clicked()"), self.submitFileAndMethod)

    def openMusicFileInSheet(self):
        musicFilePath = QFileDialog.getOpenFileName(self, "Choose a file to open", ".",
                                                    "Music (*.mp3 *.wav)")
        self.FilePath = unicode(QString(musicFilePath).toUtf8(), 'utf-8', 'ignore')
        self.music_location_in_sheet.setText(self.FilePath)

    def openMusicFileInMusicInfo(self):
        musicFilePath = QFileDialog.getOpenFileName(self, "Choose a file to open", ".",
                                                    "Music (*.mp3 *.wav)")
        self.FilePath = unicode(QString(musicFilePath).toUtf8(), 'utf-8', 'ignore')
        self.music_location_in_musicinfo.setText(self.FilePath)

    # 确认提交的文件，并显示输出选择的特性
    def submitFileAndMethod(self):
        if self.FilePath == "" or self.FilePath == None:
            msg_box = QMessageBox(QMessageBox.Warning, u"错误", u"请先选择音乐文件！")
            msg_box.exec_()
        else:
            musicPath = self.FilePath
            musicInfoRaw = self.featureComboBox.currentText()
            musicInfo = unicode(QString(musicInfoRaw).toUtf8(), 'utf-8', 'ignore')
            print musicPath
            print musicInfo
            showFeather(musicPath, musicInfo)

    def musicToSheet(self):
        if self.FilePath == "" or self.FilePath == None:
            msg_box = QMessageBox(QMessageBox.Warning, u"错误", u"请先选择音乐文件！")
            msg_box.exec_()
        else:
            data = MusicTools.wav_to_array(self.FilePath)
            showGra(self.FilePath)


def wavread(path):
    wavfile = wave.open(path, "rb")
    params = wavfile.getparams()
    framesra, frameswav = params[2], params[3]
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.fromstring(datawav, dtype=np.short)
    datause.shape = -1, 2
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0 / framesra)
    return datause, time


def showGra(path):
    wavdata, wavtime = wavread(path)
    plt.title("Night.wav's Frames")
    plt.plot(wavtime, wavdata[0])
    plt.show()


# 绘制图像
def showGraFeather(songData, title, time):
    data = np.array(songData)
    xNum, yNum = data.shape
    xAxis = np.linspace(0, int(time), yNum)
    plt.figure('Feather', figsize=(20, 5))
    plt.title(title)

    if xNum == 1:
        plt.plot(xAxis, data[0])
    else:
        for i in range(0, xNum):
            plt.plot(xAxis, data[i], label='data' + str(i))

        plt.legend(loc='upper right')
    plt.show()


# 获取相应的特征值和绘制图像
def showFeather(musicPath, musicInfo):
    print musicPath, musicInfo
    name1, name2 = os.path.split(musicPath)
    title = musicInfo + " for " + name2
    data = MusicTools.getFeather(musicPath, musicInfo)
    if musicPath.endswith(".mp3"):
        time1 = eyed3.load(musicPath)
        print('time: {} second'.format(time1.info.time_secs))
        time = format(time1.info.time_secs)
    else:
        time = wave.Wave_read(musicPath)
        time = 1
    showGraFeather(data, title, time)


def fun():
    app = QApplication(sys.argv)
    demo = Windows()
    demo.show()
    sys.exit(app.exec_())
