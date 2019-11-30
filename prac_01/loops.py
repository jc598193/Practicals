for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in reversed(range(1, 21)):
    print(i, end=' ')
print()
stars = int(input("How many stars you want: "))
for i in range(0, stars):
    print("*", end='')
print()
for i in range(0, stars):
    for j in range(0, i + 1):
        print("* ", end="")
    print()
print()