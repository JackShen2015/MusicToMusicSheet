#! /usr/bin/python2.7
# coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import ui
import time
import matplotlib.pyplot as plt
import numpy as np
import wave
import eyed3
import os
import MusicTools
import HelpTools


class Windows(QMainWindow, ui.Ui_MainWindow):
    FilePath = ""
    selectedMethod = ""
    pitch_name_array = []

    def __init__(self, parent=None):
        super(Windows, self).__init__(parent)
        self.musicFile = ""
        self.setupUi(self)
        self.ButtionActionConnect()

    def ButtionActionConnect(self):
        QObject.connect(self.selected_meusic_in_sheet, SIGNAL("clicked()"), self.open_music_file)
        QObject.connect(self.selected_music_in_musicinfo, SIGNAL("clicked()"), self.open_music_file)
        QObject.connect(self.startButtonInSheet, SIGNAL("clicked()"), self.musicToSheet)
        QObject.connect(self.startButtonInMusicInfo, SIGNAL("clicked()"), self.submit_file_and_show_all_method)
        QObject.connect(self.clear_result_A, SIGNAL("clicked()"), self.clear_result)
        QObject.connect(self.startButtonInMusicInfo_mfcc, SIGNAL("clicked()"), self.show_mfcc)
        QObject.connect(self.startButtonInMusicInfo_lpc, SIGNAL("clicked()"), self.show_lpc)
        QObject.connect(self.startButtonInMusicInfo_mfcc_d1, SIGNAL("clicked()"), self.show_mfcc_d1)
        QObject.connect(self.startButtonInMusicInfo_sharpness, SIGNAL("clicked()"), self.shows_sharpness)
        QObject.connect(self.startButtonInMusicInfo_zcr, SIGNAL("clicked()"), self.show_zcr)
        QObject.connect(self.startButtonInMusicInfo_energy, SIGNAL("clicked()"), self.show_energy)
        QObject.connect(self.startButtonInMusicInfo_spectralflatness, SIGNAL("clicked()"), self.show_spectral_flatness)
        QObject.connect(self.startButtonInMusicInfo_spectralrolloff, SIGNAL("clicked()"), self.show_spectral_rolloff)
        QObject.connect(self.startButtonInSheet_frames, SIGNAL("clicked()"), self.show_frames)
        QObject.connect(self.startButtonInSheet_datu2, SIGNAL("clicked()"), self.show_hz_gra)
        QObject.connect(self.startButtonInSheet_datu3, SIGNAL("clicked()"), self.show_energy_gra)
        self.exit.triggered.connect(QApplication.quit)
        self.exit.setShortcut('Ctrl+Q')
        self.exit.setStatusTip("Exit App")

    # 清空产生乐谱的所有的信息
    def clear_result(self):
        # self.music_info.clear()
        self.frames.clear()
        self.hz.clear()
        self.energy_in_sheet.clear()
        self.startButtonInSheet_frames.setEnabled(False)
        self.startButtonInSheet_datu3.setEnabled(False)
        self.startButtonInSheet_datu2.setEnabled(False)
        self.after_music_info.clear()
        self.after_music_info_2.clear()

    # 展示音乐文件的波形图
    def show_frames(self):
        show_frames_gra(self.FilePath)

    # 展示音乐文件基音频率图
    def show_hz_gra(self):
        array = HelpTools.read_music_info_from_disk("./music/temp/test.txt")
        show_hz_gra(array)

    # 展示音乐文件能量图片
    def show_energy_gra(self):
        all_enegry = MusicTools.get_every_energy(
            MusicTools.music_array_cut(MusicTools.wav_to_array(self.FilePath)))
        show_energy_gra(all_enegry)

    # 文件选择
    def open_music_file(self):
        musicFilePath = QFileDialog.getOpenFileName(self, "Choose a file to open", "./music/wav",
                                                    "Music (*.mp3 *.wav)")
        self.FilePath = unicode(QString(musicFilePath).toUtf8(), 'utf-8', 'ignore')
        self.music_location_in_musicinfo.setText(self.FilePath)
        self.music_location_in_sheet.setText(self.FilePath)

    # 确认提交的文件，将提交的音乐文件的信息展现到ui上
    def submit_file_and_show_all_method(self):
        if self.FilePath == "" or self.FilePath == None:
            msg_box = QMessageBox(QMessageBox.Warning, u"错误", u"请先选择音乐文件！")
            msg_box.exec_()
        else:
            musicPath = self.FilePath
            musicInfo = ["MFCC", "LPC", "MFCC_D1", "Sharpness"
                , "ZCR", "Energy", "SpectralRolloff", "spectralFlatness"]
            # showFeather(musicPath, musicInfo[1])
            for i in musicInfo:
                showFeather(self.FilePath, i, 1)
            self.add_image_in_music_info()
            # self.mfcc.show()

    # 添加产生的图片到ui界面中
    def add_image_in_music_info(self):
        a = QPixmap('./music/temp/MFCC.jpg')
        a = a.scaled(self.mfcc.size())
        self.mfcc.setPixmap(a)
        self.startButtonInMusicInfo_mfcc.setEnabled(True)

        a = QPixmap('./music/temp/LPC.jpg')
        a = a.scaled(self.lpc.size())
        self.lpc.setPixmap(a)
        self.startButtonInMusicInfo_lpc.setEnabled(True)

        a = QPixmap('./music/temp/MFCC_D1.jpg')
        a = a.scaled(self.mfcc_d1.size())
        self.mfcc_d1.setPixmap(a)
        self.startButtonInMusicInfo_mfcc_d1.setEnabled(True)

        a = QPixmap('./music/temp/Sharpness.jpg')
        a = a.scaled(self.sharpness.size())
        self.sharpness.setPixmap(a)
        self.startButtonInMusicInfo_sharpness.setEnabled(True)

        a = QPixmap('./music/temp/ZCR.jpg')
        a = a.scaled(self.zcr.size())
        self.zcr.setPixmap(a)
        self.startButtonInMusicInfo_zcr.setEnabled(True)

        a = QPixmap('./music/temp/Energy.jpg')
        a = a.scaled(self.energy.size())
        self.energy.setPixmap(a)
        self.startButtonInMusicInfo_energy.setEnabled(True)

        a = QPixmap('./music/temp/SpectralRolloff.jpg')
        a = a.scaled(self.spectralrolloff.size())
        self.spectralrolloff.setPixmap(a)
        self.startButtonInMusicInfo_spectralrolloff.setEnabled(True)

        a = QPixmap('./music/temp/spectralFlatness.jpg')
        a = a.scaled(self.spectralflatness.size())
        self.spectralflatness.setPixmap(a)
        self.startButtonInMusicInfo_spectralflatness.setEnabled(True)

    # 将音乐文件转换成乐谱
    def musicToSheet(self):
        if self.FilePath == "" or self.FilePath == None:
            msg_box = QMessageBox(QMessageBox.Warning, u"错误", u"请先选择音乐文件！")
            msg_box.exec_()
        else:
            result_str = ""
            if (not os.path.exists("./music/temp/test.txt")):
                HelpTools.get_music_info_and_save_to_disk(self.FilePath, "./music/temp/test.txt")
                array = HelpTools.read_music_info_from_disk("./music/temp/test.txt")
            else:
                array = HelpTools.read_music_info_from_disk("./music/temp/test.txt")

            time.sleep(5)

            # 显示音乐文件的frames
            save_frames_gra(self.FilePath)
            a = QPixmap("./music/temp/temp1.jpg")
            a = a.scaled(self.frames.size())
            self.frames.setPixmap(a)
            self.startButtonInSheet_frames.setEnabled(True)

            # 显示音乐文件的基音频率
            save_hz_gra(array)
            a = QPixmap("./music/temp/temp2.jpg")
            a = a.scaled(self.hz.size())
            self.hz.setPixmap(a)
            self.startButtonInSheet_datu2.setEnabled(True)

            result_str += u"音乐基频序列："
            result_str += str(array)
            result_str += "\n" + "\n"
            pitch_name = MusicTools.basic_hz_to_pitch_names(array)
            all_enegry = MusicTools.get_every_energy(
                MusicTools.music_array_cut(MusicTools.wav_to_array(self.FilePath)))

            # 显示音乐文件的能量
            print all_enegry
            save_energy_gra(all_enegry)
            a = QPixmap("./music/temp/temp3.jpg")
            a = a.scaled(self.energy_in_sheet.size())
            self.energy_in_sheet.setPixmap(a)
            self.startButtonInSheet_datu3.setEnabled(True)

            pitch_name_array = MusicTools.pitch_array(pitch_name, all_enegry)
            result_str += u"未整合的序列："
            for i in pitch_name_array:
                result_str += "{" + i.name + " " + str(i.time) + " " + str(i.energy) + "}" + " "

            result_str += "\n" + "\n"
            # self.music_info.setText(result_str)

            print result_str

            result_str = ""
            result_str += u"已经整合的序列："
            after = MusicTools.after_pitch_array(pitch_name_array)
            for i in after:
                result_str += "{" + i.name + " " + str(i.time) + " " + str(i.energy) + "}" + " "
            result_str += "\n" + "\n"
            result_str += u"拍号：" + MusicTools.get_beat(frames=after[0:6])
            result_str += "\n"
            result_str += u"调号：" + MusicTools.get_diao_hao()
            self.after_music_info.setText(result_str)

            str1 = MusicTools.get_final_music()
            self.after_music_info_2.setText(str1)

    def show_mfcc(self):
        showFeather(self.FilePath, "MFCC", 0)

    def show_lpc(self):
        showFeather(self.FilePath, "LPC", 0)

    def show_mfcc_d1(self):
        showFeather(self.FilePath, "MFCC_D1", 0)

    def show_energy(self):
        showFeather(self.FilePath, "Energy", 0)

    def shows_sharpness(self):
        showFeather(self.FilePath, "Sharpness", 0)

    def show_zcr(self):
        showFeather(self.FilePath, "ZCR", 0)

    def show_spectral_rolloff(self):
        showFeather(self.FilePath, "SpectralRolloff", 0)

    def show_spectral_flatness(self):
        showFeather(self.FilePath, "spectralFlatness", 0)


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


# 保存音乐文件的波形图
def save_frames_gra(path):
    wavdata, wavtime = wavread(path)
    plt.title("test music's Frames")
    plt.plot(wavtime, wavdata[0])
    plt.savefig("./music/temp/temp1.jpg")
    plt.close()


# 展示音乐文件的波形图
def show_frames_gra(path):
    wavdata, wavtime = wavread(path)
    plt.title("test music's Frames")
    plt.plot(wavtime, wavdata[0])
    plt.show()


# 保存音乐文件基音频率图
def save_hz_gra(array):
    xx = range(0, len(array))
    plt.plot(xx, array, linestyle='-', marker='.')
    plt.savefig("./music/temp/temp2.jpg")
    plt.close()


def show_hz_gra(array):
    xx = range(0, len(array))
    plt.plot(xx, array, linestyle='-', marker='.')
    plt.show()


def save_energy_gra(array):
    xx = range(0, len(array))
    plt.plot(xx, array, linestyle="-", marker='.')
    plt.savefig("./music/temp/temp3.jpg")
    plt.close()


def show_energy_gra(array):
    xx = range(0, len(array))
    plt.plot(xx, array, linestyle='-', marker='.')
    plt.show()


# 绘制图像
def showGraFeather(songData, title, time, musicInfo, type):
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
    if type == 0:
        plt.show()

    else:
        plt.savefig("./music/temp/" + musicInfo + ".jpg")
        plt.close()


# 获取相应的特征值和绘制图像
def showFeather(musicPath, musicInfo, type):
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
    showGraFeather(data, title, time, musicInfo, type)


def fun():
    app = QApplication(sys.argv)
    demo = Windows()
    demo.show()
    sys.exit(app.exec_())
