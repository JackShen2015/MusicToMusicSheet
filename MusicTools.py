#! /usr/bin/python2.7
# coding=utf8
from pydub import AudioSegment
import os
import wave
import numpy as np
import ctypes

# 当wav文件的采样频率为44100时，每分钟100拍的音乐，16分音符的采样步长为6654
N = 6654


# 如果源文件为MP3文件，则转换成wav文件
def mp3_to_wav(music_path):
    if music_path == "" or music_path == None:
        return "错误！"
    else:
        AudioSegment.converter = "/usr/bin/ffmpeg"
        sound = AudioSegment.from_mp3(music_path)
        path, filename = os.path.split(music_path)
        wav_music_path = path + "/music/temp/" + filename.replace("mp3", "wav")
        sound.export(wav_music_path, format="wav")
        return wav_music_path


# wav文件转成数组
def wav_to_array(music_path):
    f = wave.open(music_path, "rb")
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]

    str_data = f.readframes(nframes)
    f.close()
    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data.shape = -1, 2
    wave_data = wave_data.T

    return wave_data[0]


# mp3文件转数组
def mp3_to_array(music_path):
    return wav_to_array(mp3_to_wav(music_path=music_path))


# 对音乐文件切片
def music_array_cut(wave_date):
    n = 0
    frames = []
    frame = []

    print "wavedate", len(wave_date)

    for i in range(0, len(wave_date)):
        frame.append(wave_date[i])
        n += 1
        if n == N:
            n = 0
            frames.append(frame)
            frame = []
        if i == len(wave_date) - 1:
            frame.append(wave_date[i])
            frames.append(frame)

    print "frames lenth:", len(frames)
    return frames


# 对每个音乐文件切片进行DCT计算获取基频
def get_all_basic_hz(frames):
    lib = ctypes.cdll.LoadLibrary("./cpp/test.so")
    print "frames", len(frames)
    all_basic_hz = []
    all_cut_c = []
    for frame in frames:
        c_frame = (ctypes.c_float * N)()
        n = 0
        for i in frame:
            c_frame[n] = i
            n += 1
        all_cut_c.append(c_frame)
    print len(all_cut_c[0])
    for i in range(0, len(all_cut_c)):
        lib.getBasicHz.restype = ctypes.c_float
        all_basic_hz.append(lib.getBasicHz(all_cut_c[i], N))
        print all_basic_hz[i]
    return all_basic_hz


# 运用OpenCV对音乐数组进行DCT计算
def get_all_basic_hz_with_open_cv():
    return


# 基频到音名的映射
def basic_hz_to_music_name(all_basic_hz):
    music_name = ['c', '#c', 'd', '#d', 'e', 'f', '#f', 'g', '#g',
                  'a', '#a', 'b', 'c1', '#c1', 'd1', '#d1', 'e1', 'f1',
                  '#f1', 'g1', '#g1', 'a1', '#a1', 'b1', 'c2', '#c2', 'd2',
                  '#d2', 'e2', 'f2', '#f2', 'g2', '#g2', 'a2', '#a2', 'b2']
    music_hz = [130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185.0, 196.0, 207.1,
                220.0, 233.1, 246.9, 261.6, 277.2, 293.7, 311.1, 329.6, 349.2,
                370.0, 392.0, 415.3, 440.0, 466.2, 493.9, 523.3, 554.4, 587.3,
                622.3, 659.3, 698.5, 740.0, 784.0, 830.6, 880.0, 932.3, 987.8]

    result = []
    for i in all_basic_hz:
        if i + 5 < 130.8:
            result.append(music_name[0])
        elif i - 5 > 987.8:
            result.append(music_name[35])
        else:
            # for j in range(0, 36):
            #     if i - 5.0 <= musicHz[j] < i + 5.0:
            #         result.append(musicName[j])
            #         break
            num = 10000
            no = 0
            for j in range(0, 36):
                if num > abs(music_hz[j] - i):
                    num = abs(music_hz[j] - i)
                    no = j
            result.append(music_name[no])

    return result
