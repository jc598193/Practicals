import random
def main():
    score = float(input("Enter score: "))
    print(get_score(score))
    print(random_score())

def get_score(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 50 and score <= 90:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"


def random_score():
    for i in range(100):
        return random.randint(1, 101)


main()
