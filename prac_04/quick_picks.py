import random
picks = int(input('How many quick picks? '))
MIN = 1
MAX = 45
for line in range(picks):
    list_pick = []
    for i in range(6):
        number = random.randint(MIN, MAX)
        while number in list_pick:
            number = random.randint(MIN, MAX)
        list_pick.append(number)
    list_pick.sort()
    for number in list_pick:
        print('{:>2}'.format(number), end=' ')
    print()
