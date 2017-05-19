#! /usr/bin/python2.7
# coding=utf8
from MusicTools import *
import time
import HelpTools

start = time.clock()

MusicData = HelpTools.read_music_info_from_disk(
    data_location="./music/music_info/茉莉花100.txt")
print basic_hz_to_music_name(MusicData)
print len(basic_hz_to_music_name(MusicData))

end = time.clock()
print "time", end - start
