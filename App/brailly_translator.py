alphabet = {
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',
}
upper_case = {
    'A': '000001a',
    'B': '000001b',
    'C': '000001c',
    'D': '000001d',
    'E': '000001e',
    'F': '000001f',
    'G': '000001g',
    'H': '000001h',
    'I': '000001i',
    'J': '000001j',
    'K': '000001k',
    'L': '000001l',
    'M': '000001m',
    'N': '000001n',
    'O': '000001o',
    'P': '000001p',
    'Q': '000001q',
    'R': '000001r',
    'S': '000001s',
    'T': '000001t',
    'U': '000001u',
    'V': '000001v',
    'W': '000001w',
    'X': '000001x',
    'Y': '000001y',
    'Z': '000001z'
}

numbers = {
    '0': "000000",
    '1': '100000',
    '2': '110000',
    '3': '100100',
    '4': '100110',
    '5': '100010',
    '6': '110100',
    '7': '110110',
    '8': '110010',
    '9': '010100',
}

wordSigns = {
    'wh': '100011',
    'of': '111011',
    'ou': '110011',
    'ow': '010101',
    'sh': '100101',
    'st': '001100',
    'th': '100111',
    'ar': '001110',
    'ch': '100001',
    'ed': '110101',
    'en': '010001',
    'er': '110111',
    'gh': '110001',
    'in': '001010',
    'and': '111101',
    'for': '111111',
    'the': '011101',
    'with': '011111',
}

contractions = {
    'but ' : 'b ',
    'can ' : 'c ',
    'do ' : 'd ',
    'every ' : 'e ',
    'from ' : 'f ',
    'go ' : 'g ',
    'have ' : 'h ',
    'just ' : 'j ',
    'more ' : 'm ',
    'not ' : 'n ',
    'people ' : 'p ',
    'quite ' : 'q ',
    'rather ' : 'r ',
    'so ' : 's ',
    'that ' : 't ',
    'still ' : 'st ',
    'child ' : 'ch ',
    'us ' : 'u ',
    'very ' : 'v ',
    'it ' : 'x ',
    'you ' : 'y ',
    'as ' : 'z ',
    'shall ' : 'sh ',
    'this ' : 'th ',
    'which ' : 'wh ',
    'out ' : 'ou ',
    'will ' : 'w ',
    'be ' : 'bb ',
    'en ' : 'enough ',
    'to ' : 'ff ',
    'were ' : 'gg ',
    'was ' : '” ',
    'braille ' : 'brl ',
    'and ': '111101 ',
    'for ': '111111 ',
    'the ': '011101 ',
    'with ': '011111 ',
}

def translate_numbers(text: str) -> str:
    out = ""
    i = 0
    while i < len(text):
        if text[i].isnumeric():
           out += "001111"
           while i < len(text) and text[i].isnumeric():
                out += numbers[text[i]]
                i += 1 
        else:
            out += text[i]
            i += 1

    return out

def grade2_braille_translate(text):
    text += " "

    text = translate_numbers(text)

    for key in upper_case.keys():
        text = text.replace(key, upper_case[key])

    for key in contractions.keys():
        text = text.replace(key, contractions[key])

    for key in wordSigns.keys():
        text = text.replace(key, wordSigns[key])

    for key in alphabet.keys():
        text = text.replace(key, alphabet[key])

    return text
    
def grade1_braille_translation(text):
    text += " "

    text = translate_numbers(text)

    for key in upper_case.keys():
        text = text.replace(key, upper_case[key])

    for key in alphabet.keys():
        text = text.replace(key, alphabet[key])
    
    return text

if __name__ == "__main__":
    test_text = "Hello world how are you doing this is a sample text"

    translated_text = grade1_braille_translation(test_text)

    print(translated_text)

