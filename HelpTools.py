#! /usr/bin/python2.7
# coding=utf8
from MusicTools import *


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
    music_info_cut = (music_array_cut(wav_to_array(music_location)))
    music_info_basic_hz = get_all_basic_hz(music_info_cut)
    pre = str(music_info_basic_hz)
    pre = pre.replace("[", "")
    pre = pre.replace("]", "")
    pre = pre.replace(" ", "")
    f = open(music_info_save_location, "w")
    f.write(pre)
    f.close()
