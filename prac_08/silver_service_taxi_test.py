from prac_08.silverservice_taxi import SilverServiceTaxi


def main():

    taxi = SilverServiceTaxi('Prius 1', 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


if __name__ == "__main__":
    main()