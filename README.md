# Guitar Practice Core

A package for generating practice exercises for guitar. The package uses a domain driven design (DDD) architecture, meaning that only core business logic for generating exercises is contained in this package. Code to integrate with a web API or the command-line will be contained in another repo (yet to be implemented).

## To Do

- ~~Create domain models~~
- ~~Create sequencer~~
- ~~Implement 16th note exercise~~
- ~~Implement list_exercises and get_exercise~~
- ~~Implement basic vextab formatter~~
- ~~Convert sequenceshifters into pickpattern that can take another pickpattern as a frozen argument~~
- ~~Implement __ceil__, __gt__, __lt__ and __sub__ in Beat~~
- ~~Fill the end of exercises with rests~~
- ~~Format odd beats for vextab using tie_split()~~
- ~~Fix chords in normalise_note_durations()~~
- Add tests for eq etc. for rest beats
- Allow ending to be filled with either last note or rests
- 16th note exercises
- Split pickpatterns into smaller modules
- Add metadata to sequences (e.g. tuning, exercise title, bpm, time) 
- Add triplets to vextab and tie_split()
- Implement pick patterns
- Implement basic exercises
- Import chord and scale shapes from legacy project
- Implement rhythm generator
- Add rhythm to sequencer
- Exercises that use rhythm
- Implement shape shifters
- Add shape shifters to sequencer
- Exercises that use shape shifters


## Features

The following types of exercises will be available from this package, each with varying levels of difficulty:
- Procedurally generated practice sequences (in progress):
  - Scales
  - Chords
  - Rhythm
  - Arpeggios
  - Finger Picking
  - Lead phrases
  - Riffs
  - Stretches
  - Co-ordination
  - Speed
- Memory and repetition (show a sequence, then hide it and try to repeat it)
- Fret/note matching
- Interval identification
  - Pairs of notes
  - Chords
  - Scales
  - Arpeggios
 