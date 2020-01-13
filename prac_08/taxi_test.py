from prac_08.taxi import Taxi

Prius_1 = Taxi('Prius 1', 100)
Prius_1.drive(40)
print(Prius_1)
print(Prius_1.get_fare())
Prius_1.start_fare()
Prius_1.drive(90)
print(Prius_1)
print(Prius_1.get_fare())