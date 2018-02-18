sos = '...---...'
morseCode = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'S':'...',
    'O':'---'
}

def translateMorse(morseString):
    for letter in morseString:
        print('The letter {} in morse is {}'.format(letter, morseCode[letter]))
    print('To send {} in morse key this:- '.format(morseString),end='')
    for letter in morseString:
        print('{}'.format(morseCode[letter]),end='')
    print('')

translateMorse('SOS')

str = input('What do you want to translate')
translateMorse(str)
