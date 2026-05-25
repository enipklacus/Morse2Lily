# Morse2Lily

Convert text to lilypond notes through morse code!

## How to run it

Run it with your python interpreter. There are some arguments to use.
```
python ./Morse2Lily.py
python3 ./Morse2Lily.py -tO 16 -tA 8 -tW 8. -tE 4 -o outputCode.txt
python ./Morse2Lily.py -m -s "Ooooooh yeah, Lily talking Morse!"
```
The "time" arguments must be written as Lilypond rhythm, i.e "1" and "multiples of 2". Dots are supported!

## Why...?

I've always wanted to convert morse code to music. Since Lilypond is text-based, doing that is as fundamental as a REGEX script.

I wrote this in python to exercise and strengthen my coding skills; surely it can be optimized in every way possible. Didn't vibe code it, though!

Sadly, this script only works with standard english letters, numbers and some ponctuation ( . ! ? ; , - ).

TODO: Support for latin letters (ã é ô etc...); allow change of spacer text (LS, WS, E, etc.).

Huge thanks to GeeksForGeeks and the official Python documentation.
