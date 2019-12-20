# Import Car class
from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car('Car', 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    limo = Car('limo', 100)  # Add car name and fuel
    limo.add_fuel(20)  # Add more fuel
    limo.drive(115)  # Add distance drive
    print('fuel = ', limo.fuel)  # print remaining fuel
    print('odometer = ', limo.odometer)  # print distance
    print(limo)  # print car

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()
