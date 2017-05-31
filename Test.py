#! /usr/bin/python2.7
# coding=utf8
import MusicTools
import time
import HelpTools
import GUI_Tools


def test():
    start = time.clock()

    # pitch_name = basic_hz_to_pitch_names(HelpTools.read_music_info_from_disk(
    #     data_location="./music/music_info/茉莉花100.txt"))
    # # print len(basic_hz_to_pitch_names(MusicData))
    # all_enegry = get_every_energy(music_array_cut(wav_to_array("./music/wav/茉莉花100.wav")))

    # array = music_array_cut(wav_to_array("./test.wav"))
    # HelpTools.get_music_info_and_save_to_disk("./test.wav", "./test.txt")
    array = HelpTools.read_music_info_from_disk("./test.txt")
    print array
    pitch_name = MusicTools.basic_hz_to_pitch_names(array)
    all_enegry = MusicTools.get_every_energy(MusicTools.music_array_cut(MusicTools.wav_to_array("./test.wav")))

    print pitch_name
    print all_enegry
    print len(all_enegry)

    end = time.clock()

    print "time", end - start


def main():
    GUI_Tools.fun()


if __name__ == '__main__':
    main()
