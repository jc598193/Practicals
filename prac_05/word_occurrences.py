text = input('Text: ')
list_word = []

# store words in list
for string in text:
    list_word = text.split()
list_word.sort()
WORD_DICT = {}

# store words and count in dictionary
for word in list_word:
    if word in WORD_DICT:
        WORD_DICT[word] += 1
    else:
        WORD_DICT[word] = 1

# print dictionary
for each, show in WORD_DICT.items():
    print('{} : {}'.format(each, show))
