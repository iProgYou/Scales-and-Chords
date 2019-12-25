def get_scale(note,mode='Ionian'):
    #takes a note and returns the notes of the scale based on that note.
    mode = mode.upper()

    mode_mod = {
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

    if mode not in mode_mod:
        print('Invalid mode chosen. Major selected as default.')
        mode = 'MAJOR'

    circle_of_sharps = ['C','G','D','A','E','B','F#','C#']
    circle_of_flats = ['C','F','Bb','Eb','Ab','Db','Gb','Cb']
    white_notes = ['C','D','E','F','G','A','B']
    new_scale = white_notes

    #Gets you a regular old major scale
    if note in circle_of_sharps:
        iter = circle_of_sharps.index(note)
        for i in range(iter):
            new_scale = new_scale[4:] + new_scale[:4]
            new_scale[6] = new_scale[6] + '#'

    elif note in circle_of_flats:
        iter = circle_of_flats.index(note)
        for i in range(iter):
            new_scale = new_scale[3:] + new_scale[:3]
            new_scale[3] = new_scale[3] + 'b'
    # This modifies the major scale to get you whatever mode you pass in.
    modifier = mode_mod[mode]

    for interval_direction in modifier:
        interval_index = interval_direction[0] - 1 #int
        current_scale_degree = new_scale[interval_index] #string

        if '#' in current_scale_degree: 
            # print("Here in # conditional")
            if interval_direction[1] == '#':
                new_scale[interval_index] = current_scale_degree[:1] + 'x'
            else:
                new_scale[interval_index] = current_scale_degree[:1]

        elif 'b' in current_scale_degree:
            # print("Here in b conditional")

            if interval_direction[1] == '#':
                new_scale[interval_index] = current_scale_degree[:1]
            else:
                new_scale[interval_index] = current_scale_degree + 'b'

        else:
            # print("Here in neither conditional")

            new_scale[interval_index] = current_scale_degree + interval_direction[1]

    return new_scale

def get_chords_in_scale(root,extensions=5):
    scale = get_scale(root)
    chord_extentions = [3,5,7,9,11,13]
    if extensions not in chord_extentions:
        print('Invalid extension chosen. 5 selected as default.')
        extensions = 5

    roman_numerals_major = ['I','ii','iii','IV','V','vi','vii°']
    chords_in_scale = []

    for i in range(7):
        scale_in_thirds = [scale[i] for i in range(0,7,2)] + [scale[i] for i in range(1,7,2)]
        chords_in_scale.append(scale_in_thirds[:(extensions+1)//2])
        scale = scale[1:] + scale[:1]

    with_romans = dict(zip(roman_numerals_major,chords_in_scale))
    return with_romans

# print(get_scale("C#","lydian"))

