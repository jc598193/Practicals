COLOURS = {'white': '#ffffff', 'purple': '#a020f0', 'sienna': '#a052dd', 'Skyblue': '#87ceeb', 'tan': '#d2b48c', 'thistle': '#d8bfd8'}

# print dictionary COLOURS
for color, code in COLOURS.items():
    print('{:7} : {}'.format(color, code))

# loop for input colours
choose = input('Enter a color: ')
while choose.strip() != '':
    if choose in COLOURS.keys():
        print(COLOURS[choose])
    else:
        print('Invalid colour name')
    choose = input('Enter a color: ')


