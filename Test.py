# coding=utf8
from Tools import *
import time

start = time.clock()
# print len(wavToArray(mp3ToWav("./music/diziduzou.mp3")))
# print len(musicArrayCut(wavToArray(mp3ToWav("./music/diziduzou.mp3"))))
# a = (getAllBasicHz(musicArrayCut(wavToArray(mp3ToWav("./music/diziduzou.mp3")))))
b = (musicArrayCut(wavToArray("./test.wav")))
a = getAllBasicHz(b)
print len(a)
print a
print BasicHzToMusicName(a)
print len(BasicHzToMusicName(a))
end = time.clock()

print "time", end - start
