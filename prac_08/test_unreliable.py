from prac_08.unreliable_car import UnreliableCar


def main():

    car = UnreliableCar('Prius 1', 100, 80)
    car.drive(40)
    print(car)


if __name__ == '__main__':
    main()
