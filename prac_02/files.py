name_file = open("name.txt", "w")
name = str(input("Name: "))
name_file.write(name)
name_file.close()
name_open = open("name.txt", "r")
for name_infile in name_open:
    print("Your name is", name_infile)
print('*************')
number1 = int(input("number1: "))
number2 = int(input("number2: "))
number_file = open("number.txt", "w")
number_file.write(str(number1))
number_file.write('\n')
number_file.write(str(number2))
number_file.write('\n')
number_file.close()
number_open = open("number.txt", "r")
num01 = number_open.readline()
num02 = number_open.readline()
total = int(num01) + int(num02)
print(total)

print("************")

movie = open("number.txt", "r")
file_read = movie.readlines()
total = 0
for num in file_read:
    try:
        total += float(num)
    except ValueError:
        continue
print(total)
