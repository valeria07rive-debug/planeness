from okok import TripPlanner
from planner import (
    get_country_data,
    format_country_info,
    get_coordinates,
    get_weather_summary
)

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
            country = input("Enter country: ")
            days = int(input("Days staying: "))
            planner.add_country(country, days)

        elif option == "2":
            country = input("Enter country: ")
            data = get_country_data(country)
            print(format_country_info(data))

        elif option == "3":
            country = input("Enter country: ")
            coords = get_coordinates(country)

            if coords:
                lat, lon = coords
                print(get_weather_summary(lat, lon))
            else:
                print("Country not found")

        elif option == "4":
            planner.show_summary()

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "_main_":
    main()