from prac_06.guitars import Guitar


def main():
    """"""
    gibson = Guitar('Gibson L-5 CES', 1922, 16035.40)
    print('{} get_age - Expected 96. Got {}'.format(gibson.name, gibson.get_age()))
    print('{} is_vintage() - Expected True. Got {}'.format(gibson.name, gibson.is_vintage()))
    print(gibson)

if __name__ == '__main__':
    main()
