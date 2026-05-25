import re, sys, argparse

parser = argparse.ArgumentParser(
    prog='python Morse2Lily.py',
    description='Convert text into lilypond musical Morse Code!\nSentences and text must be written with double quotes!',
    formatter_class=argparse.RawTextHelpFormatter,
    epilog='Ooooooh yeah, Lily talkin\' Morse!'
)
DCOU = "(doesn\'t change other units)."
parser.add_argument('-o', '--output', metavar='', help='Outputs to specified file.')
parser.add_argument('-s', '--sentence', metavar='', type=str, help='Input text without query')
parser.add_argument('-m', '--minimal' , action='store_true', help='Only prints starter note and subsequent rhythms.')
parser.add_argument('-tO', '--timeDot', metavar='', type=str, help='Alter the rhythm/value of dots ' + DCOU )
parser.add_argument('-tA', '--timeDash', metavar='', type=str, help='Alter the rhythm/value of dashes ' + DCOU )
parser.add_argument('-tW', '--timeWords', metavar='', type=str, help='Alter the rhythm/value of spaces between words ' + DCOU )
parser.add_argument('-tE', '--timeEnd', metavar='', type=str, help='Alter the rhythm/value of the final letter ' + DCOU )
args = parser.parse_args()

timeDot = "16" if args.timeDot is None else args.timeDot
timeDash = "8." if args.timeDash is None else args.timeDash
timeBetweenWords = "4." if args.timeWords is None else args.timeWords
timeEnd = "2" if args.timeEnd is None else args.timeEnd

codeDot = timeDot + "_\".\""
codeDash = timeDash + "_\"_\""
codeStart = "^\"Srt.\""

defaultLS = "\\autoBeamOff " + timeDash + "^\"" + "LS" + "\" \\autoBeamOn"
defaultWS = "\\autoBeamOff " + timeBetweenWords + "^\"" + "WS" + "\" \\autoBeamOn\n"
defaultEnd = "\n\\autoBeamOff " + timeEnd + "^\"" + "E" + "\" \\autoBeamOn"

if args.minimal is True:
    codeDot, codeDash, codeStart = timeDot, timeDash, ""
    defaultLS, defaultWS, defaultEnd = timeDash, timeBetweenWords, timeEnd
else:
    pass

translateLily = {
    "c": "c", ".": codeDot , "-": codeDash , 
    "L": defaultLS , 
    "W": defaultWS , 
    "E": defaultEnd
    }

translateMorse =      { 
                    'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '-':'-....-',
                    '!':'.-.-.-', ';': '--..--'
                    }

def encMorse(string):
    cipher = ''
    for letter in string:
        if letter != ' ':
            cipher += translateMorse[letter] + 'L'
        else:
            cipher += ' '
    return cipher

def encLy(string):
    cipher = ''
    for letter in string:
        if letter != ' ':
            cipher += translateLily[letter] + ' '
        else:
            cipher += ' '
    return cipher

if args.sentence is None:
    print("Type in your sentence:")
    userInput = input()
else:
    userInput = args.sentence

upperCaseInput = userInput.upper()

convertedText = re.sub("[\'\"]", "", upperCaseInput)
convertedText = re.sub("L\\s", "W", encMorse(convertedText) )
convertedText = re.sub("L$", "E", convertedText)
convertedText = re.sub(r"^", "c", convertedText)

convertedText = encLy(convertedText)
convertedText = re.sub("(c) (\\d*\\S*) ", "\\1\\2" + codeStart + " ", convertedText)

print(f"\n%% {userInput}")
print(convertedText)

if args.output is not None:
   with open(args.output, "w") as f:
    f.write(userInput + "\n")
    f.write(convertedText + "\n")
else:   
    pass