MODE_MOD = {
    'IONIAN':           [],
    'MAJOR':            [],
    'DORIAN':           [(3,'b'),(7,'b')],
    'PHYRGIAN':         [(2,'b'),(3,'b'),(6,'b'),(7,'b')],
    'LYDIAN':           [(4,'#')],
    'MIXOLYDIAN':       [(7,'b')],
    'MINOR':            [(3,'b'),(6,'b'),(7,'b')],
    'AEOLIAN':          [(3,'b'),(6,'b'),(7,'b')],
    'LOCRIAN':          [(2,'b'),(3,'b'),(5,'b'),(6,'b'),(7,'b')],
    'HARMONIC':         [(3,'b'),(6,'b')],
    'MELODIC':          [(3,'b')],
}

CIRCLE_OF_SHARPS = ['C','G','D','A','E','B','F#','C#']
CIRCLE_OF_FLATS = ['C','F','Bb','Eb','Ab','Db','Gb','Cb']
WHITE_NOTES = ['C','D','E','F','G','A','B']
MODE_LIST = list(MODE_MOD.keys())
ROMAN_NUMERALS_MAJOR = ['I','ii','iii','IV','V','vi','vii°']
ALL_KEYS = CIRCLE_OF_SHARPS + CIRCLE_OF_FLATS[1:] # removes C duplicate
