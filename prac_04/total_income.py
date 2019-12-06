"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of total_month."""
    incomes = []
    total_month = int(input("How many total_month? "))

    for month in range(1, total_month + 1):
        income = float(input("Enter income for month {} : ".format(month)))
        incomes.append(income)
    output_print(total_month, incomes)


def output_print(total_month, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()