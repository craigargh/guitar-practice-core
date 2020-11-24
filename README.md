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
- ~~Add fixed_pattern pick pattern~~
- ~~Change shape_name to be part of make_sequence and get it to work with arpeggios and scales~~
- ~~Change symbol for down strokes to the correct symbol~~
- ~~Make a riff generator and a fill generator~~
- ~~Refactor chug into fixed_chug_pattern ('*c'=x number of chugs, '*n'=x number of notes)~~
- ~~Move chug to pickpatterns and add tests~~
- ~~Add chromatic scale shape and include in metal picked riffs~~
- ~~Add single string scale shapes for strings 5 and 6 + include in metal picked riffs~~
- Add more picked_metal_patterns
- Fix bass_and_ pickpatterns for chord arpeggios
- Add vertical shifter to lick patterns
- Add calculate_elapsed_beats function to lick exercises 
- Tests for each existing exercise combination
- Run test coverage report
- Add missing tests
- Allow ending to be filled with either last note or rests
- Split pickpatterns into smaller modules
- Add vibrato and strong vibrato
- Add metadata to sequences (e.g. tuning, exercise title, bpm, time) 
- Implement remaining pick patterns
- Implement rhythm generator
- Implement shape shifters
- Add categories to index page

## Exercises

This is the list of exercise types that are planned to be implemented (✓=started implementing):

- Metal Rhythm
  - Power chords and Palm muting (✓)
  - Picked riffs and fills (✓)
  - Riffs and fills (inc. power chords)
- Rhythm
  - Single beat rhythm divisions (✓)
  - Sixteenth notes speed (✓)
  - Sixteenth notes variations / Gallop and reverse gallop speed
  - Time signatures
- Lead
  - Pentatonic Licks (✓)
  - Major Licks
  - Chromatic Licks
- Left-hand technique:
  - Hammer-ons, pull-offs and trills (✓)
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
  - Scale/mode shapes
    - Major (✓)
    - Pentatonic (✓)
    - Blues
    - Natural minor
    - Harmonic minor
    - Melodic minor
    - etc.
  - Alternate between two or more shapes
  - Three notes per string scales
  - All shapes of a scale played in sequence
  - Arpeggios
- Chords
  - Chord progressions (✓)
  - Chord Arpeggios (✓)
