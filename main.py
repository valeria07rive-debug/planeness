from okok import TripPlanner
from planner import (
    search_country,
    format_country_info,
    get_country_weather,
    format_weather_info
)


def create_new_plan():
    print("\n--- Create New Travel Plan ---")
    agency_name = input("Travel agency name: ").strip()
    client_name = input("Client name: ").strip()
    special_requirements = input("Special requirements: ").strip()

    return TripPlanner(client_name, agency_name, special_requirements)


def show_country_search():
    country_name = input("\nEnter country name to search: ").strip()
    country_data = search_country(country_name)

    if not country_data:
        print("Country not found.")
        return None

    print(format_country_info(country_data))

    weather = get_country_weather(country_data)
    print(format_weather_info(weather, country_data["capital"]))

    return country_data


def add_country_to_trip(planner):
    country_name = input("\nEnter country name to add: ").strip()
    country_data = search_country(country_name)

    if not country_data:
        print("Country not found.")
        return

    print(format_country_info(country_data))

    try:
        stay_days = int(input("Planned duration of stay (days): "))
        start_date = input("Estimated start date (YYYY-MM-DD): ").strip()
        notes = input("Notes for this country: ").strip()

        planner.add_country_to_plan(country_data, stay_days, start_date, notes)
        print(f"{country_data['common_name']} added to the trip plan.")
    except ValueError:
        print("Invalid input. Please check the date format and number of days.")


def main():
    planner = None

    while True:
        print("\n==============================")
        print("TRAVEL PLANNER APPLICATION")
        print("==============================")
        print("1. Create new travel plan")
        print("2. Search country information")
        print("3. Add country to client plan")
        print("4. Show trip summary")
        print("5. Show total estimated cost")
        print("6. Save itinerary")
        print("7. Load itinerary")
        print("8. Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            planner = create_new_plan()
            print("New travel plan created successfully.")

        elif option == "2":
            show_country_search()

        elif option == "3":
            if planner is None:
                print("Create or load a travel plan first.")
            else:
                add_country_to_trip(planner)

        elif option == "4":
            if planner is None:
                print("Create or load a travel plan first.")
            else:
                planner.show_summary()

        elif option == "5":
            if planner is None:
                print("Create or load a travel plan first.")
            else:
                print(f"\nTotal Estimated Trip Cost: ${planner.get_total_trip_cost()}")

        elif option == "6":
            if planner is None:
                print("Create or load a travel plan first.")
            else:
                filename = input("Enter file name to save (example: trip1.json): ").strip()
                if not filename:
                    filename = "saved_trip_plan.json"
                planner.save_plan(filename)
                print("Itinerary saved successfully.")

        elif option == "7":
            filename = input("Enter file name to load (example: trip1.json): ").strip()
            if not filename:
                filename = "saved_trip_plan.json"

            loaded_plan = TripPlanner.load_plan(filename)

            if loaded_plan is None:
                print("Saved itinerary not found.")
            else:
                planner = loaded_plan
                print("Itinerary loaded successfully.")

        elif option == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()