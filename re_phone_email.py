#! python3
# Finds all phone and email addresses on the clipboard- potential use cases in collecting large quantities of information
# Script must be run with the text to be parsed copied to the clipboard

import re, pyperclip 

phoneregex = re.compile(r'''(
(\d{3}|\(\d{3}\))?     # Area code
(\s|-|\.)?              # Seperator
(\d{3})                 # First three digits
(\s|-|\.)               # Seperator
(\d{4})                 # Last 4 digits
(\s*(ext|x|ext\.)\s*(\d{2,5}))?     # Possible Extension
)''', re.VERBOSE)

emailregex = re.compile(r'''(
    [A-Za-z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = [] 
for groups in phoneregex.findall(text):
    phonenum = ' '.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phonenum += ' ext ' + groups[8]
    matches.append(phonenum)
for groups in emailregex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('The details have been to clipboard your highness')
    print('\n'.join(matches))
else:
    print('No emails or phone numbers were found.')
