# A simple caesar cipher to encode strings

def caesarCipher(text, offset):
    legible = ''
    punctuation ={'.',',',"'", '"', '?', '/', ':', ';', '!', '%', '\\', ' '}
    for letter in text:
        if letter in punctuation:
            legible += letter
        else:
            if letter.isupper():
                value = ord(letter) -65
                universal = ((value + offset) %26)+65
                legible += chr(universal)
            else:
                value = ord(letter) - 97
                universal = ((value + offset)%26)+97
                legible += chr(universal)
    return legible
