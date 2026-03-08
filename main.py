from okok import TripPlanner
from planner import get_country_data, format_country_info
from rutas import get_weather_summary


def main():

    name = input("Client name: ")
    planner = TripPlanner(name)

    while True:

        print("\n1. Add country")
        print("2. Show country info")
        print("3. Show weather")
        print("4. Show trip summary")
        print("5. Exit")

        option = input("Choose option: ")

        if option == "1":

            country = input("Country name: ")
            days = int(input("Days staying: "))
            planner.add_country(country, days)

        elif option == "2":

            country = input("Country name: ")
            data = get_country_data(country)

            if data:
                print(format_country_info(data))
            else:
                print("Country not found")

        elif option == "3":

            country = input("Country name: ")
            data = get_country_data(country)

            if data:
                lat, lon = data["latlng"]
                print(get_weather_summary(lat, lon))
            else:
                print("Weather unavailable")

        elif option == "4":

            print(planner.summary())

        elif option == "5":

            print("Goodbye")
            break


main()