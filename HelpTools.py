#! /usr/bin/python2.7
# coding=utf8
import MusicTools


# 帮助工具，读取保存的音乐数据
def read_music_info_from_disk(data_location):
    f = open(data_location, "r")
    data_line = f.readline()  # 读取文件内容
    data_in_string = data_line.split(",")
    f.close()
    data_in_float = []
    for Item in data_in_string:
        data_in_float.append(float(Item))
    return data_in_float


# 帮助工具，保存音乐数据
def get_music_info_and_save_to_disk(music_location, music_info_save_location):
    music_info_cut = (MusicTools.music_array_cut(MusicTools.wav_to_array(music_location)))
    music_info_basic_hz = MusicTools.get_all_basic_hz(music_info_cut)
    pre = str(music_info_basic_hz)
    pre = pre.replace("[", "")
    pre = pre.replace("]", "")
    pre = pre.replace(" ", "")
    f = open(music_info_save_location, "w")
    f.write(pre)
    f.close()


# 返回音名和频率序列
def return_pitch_names_array_and_hz_array():
    pitch_name_array = []
    res_line = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    for i in range(0, 8):
        for j in res_line[:3]:
            pitch_name_array.append(j + str(i))
        for j in res_line[3:]:
            pitch_name_array.append(j + str(i + 1))
    # print pitch_name_array

    # basic_hz = 440.0
    # data = basic_hz
    # hz_array = [basic_hz]
    # for i in range(0, 48):
    #     data = data / 1.06
    #     hz_array.insert(0, data)
    # print hz_array
    # print len(hz_array)

    hz_array = [27.50, 29.14, 30.87, 32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91,
                55.00, 58.27, 61.74, 65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.5, 98.00, 103.8,
                110.0, 116.5, 123.5, 130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185.0, 196.0, 207.6,
                220.0, 233.1, 246.9, 261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.3,
                440.0, 466.2, 493.9, 523.2, 554.4, 587.3, 622.2, 659.3, 698.5, 740.0, 784.0, 830.6,
                880.0, 932.3, 987.8, 1046, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661,
                1760, 1865, 1976, 2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322,
                3520, 3729, 3951, 4186]
    return pitch_name_array[:88], hz_array


if __name__ == '__main__':
    a, b = return_pitch_names_array_and_hz_array()
    print len(a)
    print len(b)
    print a
    print b
