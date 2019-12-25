from scales_chords_beta import *

mode_list = ['IONIAN','DORIAN','PHYRGIAN','LYDIAN','MIXOLYDIAN','AEOLIAN','LOCRIAN','HARMONIC','MELODIC']
circle_of_sharps = ['C','G','D','A','E','B','F#','C#']
circle_of_flats = ['C','F','Bb','Eb','Ab','Db','Gb','Cb']
keys = circle_of_sharps + circle_of_flats

roman_numerals_major = ['I','ii','iii','IV','V','vi','vii°']

print()
for e in keys:
    scale_dict = get_chords_in_scale(e)
    print("Key of " + e)
    print()
    print("Chords in the key of " + e)
    for numeral in roman_numerals_major:
        print(numeral + ':\t' + str(scale_dict[numeral]))
    print()
    print("Modes for the key of " + e)

    for f in mode_list:
        print(f)
        print(get_scale(e,mode=f))
    print()
    print('---------------------------------------------------------')
    print()
