#! /usr/bin/python2.7
# coding=utf8
from pydub import AudioSegment
import os
import wave
import numpy as np
import ctypes
import time


# 如果源文件为MP3文件，则转换成wav文件
def mp3ToWav(musicPath):
    if musicPath == "" or musicPath == None:
        return "错误！"
    else:
        AudioSegment.converter = "/usr/bin/ffmpeg"
        sound = AudioSegment.from_mp3(musicPath)
        path, filename = os.path.split(musicPath)
        wavMusicPath = path + "/temp/" + filename.replace("mp3", "wav")
        sound.export(wavMusicPath, format="wav")
        return wavMusicPath


# wav文件转成数组
def wavToArray(musicPath):
    file = wave.open(musicPath, "rb")
    params = file.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]

    str_data = file.readframes(nframes)
    file.close()
    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data.shape = -1, 2
    wave_data = wave_data.T

    return wave_data[0]


# 音乐文件切片
def musicArrayCut(wave_date):
    n = 0
    frames = []
    frame = []

    print "wavedate", len(wave_date)

    for i in range(0, len(wave_date)):
        frame.append(wave_date[i])
        n += 1
        if n == 1654:
            n = 0
            frames.append(frame)
            frame = []
        if i == len(wave_date) - 1:
            frame.append(wave_date[i])
            frames.append(frame)

    print "frames lenth:", len(frames)
    return frames


# 对每个音乐文件切片进行DCT计算获取基频
def getAllBasicHz(frames):
    lib = ctypes.cdll.LoadLibrary("./test.so")
    print "frames", len(frames)
    allBasicHz = []
    allCutC = []
    for frame in frames:
        cframe = (ctypes.c_float * 1654)()
        n = 0
        for i in frame:
            cframe[n] = i
            n += 1
        allCutC.append(cframe)
    for i in range(0, len(allCutC)):
        lib.cgetBasicHz.restype = ctypes.c_float
        allBasicHz.append(lib.cgetBasicHz(allCutC[i], 1654))
    return allBasicHz


# 基频到音名的映射
def BasicHzToMusicName(allBasizHz):
    musicName = ['c', '#c', 'd', '#d', 'e', 'f', '#f', 'g', '#g',
                 'a', '#a', 'b', 'c1', '#c1', 'd1', '#d1', 'e1', 'f1',
                 '#f1', 'g1', '#g1', 'a1', '#a1', 'b1', 'c2', '#c2', 'd2',
                 '#d2', 'e2', 'f2', '#f2', 'g2', '#g2', 'a2', '#a2', 'b2']
    musicHz = [130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185.0, 196.0, 207.1,
               220.0, 233.1, 246.9, 261.6, 277.2, 293.7, 311.1, 329.6, 349.2,
               370.0, 392.0, 415.3, 440.0, 466.2, 493.9, 523.3, 554.4, 587.3,
               622.3, 659.3, 698.5, 740.0, 784.0, 830.6, 880.0, 932.3, 987.8]

    result = []
    for i in allBasizHz:
        if i + 5 < 130.8:
            result.append(musicName[0])
        elif i - 5 > 987.8:
            result.append(musicName[35])
        else:
            # for j in range(0, 36):
            #     if i - 5.0 <= musicHz[j] < i + 5.0:
            #         result.append(musicName[j])
            #         break
            num = 10000
            no = 0
            for j in range(0, 36):
                if num > abs(musicHz[j] - i):
                    num = abs(musicHz[j] - i)
                    no = j
            result.append(musicName[no])

    return result
