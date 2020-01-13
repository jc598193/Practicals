from prac_08.car import Car
from random import randrange


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.reliability = reliability

    def drive(self, distance):
        """
        Method to get the distance if the reliability better than random number.
        :param distance:  distance want to drive
        :return: distance actually drive
        """
        number = randrange(0, 100)
        print(number)
        if number < self.reliability:
            distance_driven = super().drive(distance)
            self.current_fare_distance += distance_driven
            return distance_driven
