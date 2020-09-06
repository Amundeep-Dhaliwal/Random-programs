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

# A Vigenere cipher implementation to both encode and decode strings given a key
from itertools import cycle
import string

def caesarPortion(letter, offset):
    if letter.isupper():
        value = ord(letter) -65
        universal = ((value + offset) %26)+65
        return chr(universal)
    else:
        value = ord(letter) - 97
        universal = ((value + offset)%26)+97
        return chr(universal)

def vigenereCipher(message, key, decode = False):
    key = key.lower()
    returnString = ''
    looper = cycle(range(len(key)))
    uppercase = {x for x in range(65,91)}
    lowercase = {x for x in range(97, 123)}
    offsets = dict(zip(string.ascii_lowercase, range(26)))
    if decode:
        coefficent = -1
    else:
        coefficent = 1
    for letter in message:
        if ord(letter) in uppercase:
            keyIndex = next(looper)
            offset = offsets[key[keyIndex]]
            returnString += caesarPortion(letter, coefficent * offset)
        elif ord(letter) in lowercase:
            keyIndex = next(looper)
            offset = offsets[key[keyIndex]]
            returnString += caesarPortion(letter, coefficent * offset)
        else:
            returnString += letter
    return returnString
