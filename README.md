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
- ~~Import chord and scale shapes from legacy project~~
- ~~Make a plan of exercises~~ 
- ~~Fix tests~~
- ~~Ties and annotations (e.g. hammer-ons, pull-offs, palm muting, pick direction)~~
- ~~Add tests for hammer_on_asc~~
- ~~Fix asc_and_desc pick patterns in hammer/pull exercises~~
- ~~Add down-pick each whole beat to annotators + down hammer/pull if note has a pick annotation~~
- ~~Change repeat sequence to pick_pattern high-order function~~
- ~~Add triplets to vextab and tie_split()~~
- ~~Move tie to Beat and rename tie on note to articulation~~
- Add vertical shifter to lick patterns
- Add calculate_elapsed_beats function to lick exercises 
- Tests for each existing exercise combination
- Allow ending to be filled with either last note or rests
- Split pickpatterns into smaller modules
- Add vibrato and strong vibrato
- Add metadata to sequences (e.g. tuning, exercise title, bpm, time) 
- Implement remaining pick patterns
- Implement rhythm generator
- Implement shape shifters

## Exercises

This is the list of exercise types that are planned to be implemented:

- Metal Rhythm
  - Power chords and Palm muting
  - Individual note rhythms (i.e. no power chords)
  - Riffs (based on real songs)
- Rhythm
  - Sixteenth notes
  - Rhythm divisions
  - Time signatures
- Lead
  - Licks
- Left-hand technique:
  - Hammer-ons, pull-offs and trills
  - Vibrato
  - Slides
  - Bends
  - Harmonics
  - Warm-ups
  - Co-ordination
  - Dexterity
- Right-hand technique:
  - Alternate picking and pick-slanting
  - Legato
  - Sweep picking
  - Tapping
  - Pinched harmonics
  - Tremolo picking
- Scales
  - Scale mode shapes
    - Major
    - Pentatonic
    - Blues
    - Natural minor
    - Harmonic minor
    - Melodic minor
    - etc.
  - Arpeggios
- Chords
  - Chord progressions
  - Chord Arpeggios


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
 