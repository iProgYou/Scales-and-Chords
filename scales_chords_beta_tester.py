from scales_chords_beta import get_scale, get_chords_in_scale
from constants import MODE_LIST, ALL_KEYS, WHITE_NOTES, CIRCLE_OF_SHARPS, CIRCLE_OF_FLATS, MODE_MOD, ROMAN_NUMERALS_MAJOR

print()
for e in ALL_KEYS:
    scale_dict = get_chords_in_scale(e)
    print("Key of " + e)
    print()
    print("Chords in the key of " + e)
    for numeral in ROMAN_NUMERALS_MAJOR:
        print(numeral + ':\t' + str(scale_dict[numeral]))
    print()
    print("Modes for the key of " + e)

    for f in MODE_LIST:
        print(f)
        print(get_scale(e,mode=f))
    print()
    print('---------------------------------------------------------')
    print()
