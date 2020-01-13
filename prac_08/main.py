from prac_08.taxi import Taxi
from prac_08.silverservice_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    list_taxi(taxis)
    total_trip = 0
    # current_taxi = None
    trip = True
    while trip:
        choice = input('q)uit, c)hoose taxi, d)rive').lower()
        if choice == 'c':
            print('Taxi available: ')
            list_taxi(taxis)
            index = int(input('Choose taxi: '))
            # current_taxi =

        elif choice == 'd':
            distance = int(input('Drive how far: '))
            total_trip += drive(taxis[index], distance)
            print('Bill to date: {}'.format(total_trip))
        elif choice == 'q':
            print('Total {}'.format(total_trip))
            print('Taxis are now: ')
            list_taxi(taxis)
            quit()
        else:
            print('It not a option')


def list_taxi(taxis):
    for each_taxi in taxis:
        print('{} - {}, fuel={}, odo={}, {}'.format(taxis.index(each_taxi), each_taxi.name, each_taxi.fuel, each_taxi.odometer, each_taxi))


def drive(taxi, distance):
    taxi.drive(distance)
    print('Your {} trip cost you {}'.format(taxi.name, taxi.get_fare()))
    return taxi.get_fare()


if __name__ == '__main__':
    main()
