# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

text = input()
for ch in range(len(text)):
    if text[ch] == ':':
        print(':'+text[ch+1])
