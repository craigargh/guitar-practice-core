import random
from functools import partial

from guitarpractice.models import Sequence, FretPosition, GuitarShape, Beat
from guitarpractice.sequencer import make_sequence
from guitarpractice.sequenceshifters import repeat_each_position


def rhythm_sixteenth_notes(variation: str) -> Sequence:
    return level_one()


def level_one() -> Sequence:
    fret_choice = random.choice(list(range(0, 13)))
    string_choice = random.choice([6, 6, 6, 5, 5, 4, 3, 2, 1])

    position = FretPosition(fret=fret_choice, string=string_choice)
    shape = GuitarShape('Fifth fret', 'note', positions=[position])
    repeater = partial(repeat_each_position, repeats=16)

    rhythm = [Beat(duration=1, division=16)]

    return make_sequence(
        shapes=[shape],
        rhythm=rhythm,
        sequence_shifters=[repeater],
    )


"""
Exercise Ideas

Level 2:
- Play a whole bar of 16th notes before switching to another note on the same string, repeat for 4 bars/notes
- Play two notes in a bar of 16th notes, switching every 2 beats
- Play two notes on adjacent strings, switching every bar
- Alternate between sixteenth notes, and quarter/eighth/rest notes each beat

Level 3:
- Ascend and a three string scale or arpeggio, picking each note multiple times
- Root + ascend and/or descend a two note arpeggio, picking each note multiple times
- On a single string ascend one chromatic shape, descend another chromatic shape that is shifted up 1+ frets
- On a single string Ascend and/or descend and chromatic shape
- On a single string play four different notes in a bar, changing each beat (i.e. 4 x 16th notes)
- Alternate between sixteenth notes, and triplets/gallops/eighth+rest/rest+eighth notes each beat

Level 4:
- On multiple strings ascend one chromatic shape, descend another chromatic shape that is shifted up 1+ frets
- On a multiple strings  ascend and descend and chromatic shape
- Large string skips between bars of 16th notes

Level 5:
- Ascend one chromatic shape, descend another chromatic shape that is shifted up 1+ frets
- Ascend and descend and chromatic shape
"""