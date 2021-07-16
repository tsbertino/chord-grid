# chord-grid

A quick script inspired by an [answer](https://www.reddit.com/r/musictheory/comments/o442gg/how_can_i_name_a_chord_that_i_dont_know_the_name/h2f74b2/) on /r/musictheory demonstrating how to find possible chords from a set of musical notes. The script takes a set of notes as the input and outputs a grid, arranging the set in thirds with each note as the root.

## Basic input

``` python

input = ['C','Eb', 'G', 'F']

```

## Differing accidentals

If different accidentals are present (i.e. a sharp and a flat), the first accidental will become the standard, and all following notes will be converted to their enharmonic equivalents.

```python
input = ['C','Eb', 'G#', 'F']
```
```
>>> Flat Mode
```
```python
input = ['C', 'Eb', 'Ab', 'F']
```

This is not preferable and in practice, one set of accidentals may be more likely than another based on the harmonic context, but I included this as a simple redundancy. In most cases it could be assumed that notes are following the standard of using one type of accidental, which preserves the 'stack of thirds' (if the notes inputted are thirds). 

In this script, if the enharmonic equivalent is not present in the 'stack of thirds' built from the other notes, it simply will not be included, as the the template is set in thirds and accidentals are only added later.

## Output

The sequence is then rearranged by thirds up to the 13th, using each note as the root, with n/a notes marked by an x.

```
>>> ['1', '3', '5', '7', '9', '11', '13']
    ['C', 'Eb', 'G', 'x', 'x', 'F', 'x']
    ['Eb', 'G', 'x', 'x', 'F', 'x', 'C']
    ['G', 'x', 'x', 'F', 'x', 'C', 'Eb']
    ['F', 'x', 'C', 'Eb', 'G', 'x', 'x']
```

For this example, this sequence of notes could represent a Cmin(add11), as it has the most notes present in the 'beginning' of the stack of thirds, namely the full minor triad of C, Eb and G, along with an extension of F, the 11th.

The presense of more 'important' notes, like the third and seventh, weigh heavier than the fifth or extensions, but this is situtational and really up to interpretation.

This is simply an easy, automated way to visualize the potential harmonic relationships of any given set of notes, allowing the user to decide likelhood of any given chord form based on harmonic context, arrangement, music theory, key, etc.

---
