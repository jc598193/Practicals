from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return "{} plus flagfall of $4.50 ".format(super().__str__(),
                                                             self.price_per_km)
