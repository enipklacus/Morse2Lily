import re

dicLily = {
    "c": "c", ".": "16_\".\"", "-": "8._\"_\"", 
    "L": "\\autoBeamOff 8.^\"L\" \\autoBeamOn", 
    "P": "\\autoBeamOff 4.^\"W\" \\autoBeamOn\n", 
    "F": "\n\\autoBeamOff 2^\"E\" \\autoBeamOn"
    }

dicMorse =      { 'A':'.-', 'B':'-...',
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
            cipher += dicMorse[letter] + 'L'
        else:
            cipher += ' '
    return cipher

def encLy(string):
    cipher = ''
    for letter in string:
        if letter != ' ':
            cipher += dicLily[letter] + ' '
        else:
            cipher += ' '
    return cipher

print("Type in your sentence:")
userInput = input()
upperCaseInput = userInput.upper()

convertedText = re.sub("L\\s", "P", encMorse(upperCaseInput) )
convertedText = re.sub("L$", "F", convertedText)
convertedText = re.sub(r"^", "c", convertedText)

convertedText = encLy(convertedText)

print(f"\n\n%% {userInput}")
print(convertedText)
