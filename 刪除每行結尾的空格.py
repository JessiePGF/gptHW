# Pyperclip module practice. Which can delete spaces at the end of the lines you just copied.

import pyperclip
text = pyperclip.paste()

splitText = text.split('\r\n')
for i in range(len(splitText)):
    splitText[i] = splitText[i].rstrip()

text = '\n'.join(splitText)
pyperclip.copy(text)