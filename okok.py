import json
from datetime import datetime, timedelta


class TripPlanner:
    def __init__(self, client_name, agency_name, special_requirements=""):
        self.client_name = client_name
        self.agency_name = agency_name
        self.special_requirements = special_requirements
        self.stops = []
        self.fixed_agency_fee = 120.0

    def add_country_to_plan(self, country_data, stay_days, start_date, notes=""):
        """
        Adds one country stop to the travel plan.
        start_date must be in YYYY-MM-DD format.
        """
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = start_dt + timedelta(days=stay_days)

        accommodation_per_day = self.get_daily_cost_by_region(country_data["region"])
        accommodation_total = accommodation_per_day * stay_days

        transportation_cost = 0
        if len(self.stops) > 0:
            transportation_cost = 450

        stop_total = accommodation_total + transportation_cost

        stop = {
            "common_name": country_data["common_name"],
            "official_name": country_data["official_name"],
            "capital": country_data["capital"],
            "region": country_data["region"],
            "subregion": country_data["subregion"],
            "country_code": country_data["country_code"],
            "stay_days": stay_days,
            "start_date": start_dt.strftime("%Y-%m-%d"),
            "end_date": end_dt.strftime("%Y-%m-%d"),
            "notes": notes,
            "daily_accommodation_cost": accommodation_per_day,
            "accommodation_total": accommodation_total,
            "transportation_cost": transportation_cost,
            "stop_total": stop_total
        }

        self.stops.append(stop)

    def get_daily_cost_by_region(self, region):
        region_costs = {
            "Europe": 150,
            "Asia": 90,
            "Americas": 120,
            "Africa": 80,
            "Oceania": 170
        }
        return region_costs.get(region, 100)

    def get_total_trip_cost(self):
        total = self.fixed_agency_fee
        for stop in self.stops:
            total += stop["stop_total"]
        return total

    def show_summary(self):
        print(f"\nTravel Agency: {self.agency_name}")
        print(f"Client Name: {self.client_name}")
        print(f"Special Requirements: {self.special_requirements if self.special_requirements else 'None'}")

        if not self.stops:
            print("No countries added to the trip yet.")
            return

        print("\nPlanned Countries:")
        total_days = 0

        for i, stop in enumerate(self.stops, start=1):
            print(f"\nStop #{i}")
            print(f"Country: {stop['official_name']}")
            print(f"Capital: {stop['capital']}")
            print(f"Region: {stop['region']} / {stop['subregion']}")
            print(f"Country Code: {stop['country_code']}")
            print(f"Stay: {stop['stay_days']} day(s)")
            print(f"Estimated Dates: {stop['start_date']} to {stop['end_date']}")
            print(f"Notes: {stop['notes'] if stop['notes'] else 'None'}")
            print(f"Accommodation per day: ${stop['daily_accommodation_cost']}")
            print(f"Accommodation total: ${stop['accommodation_total']}")
            print(f"Transportation cost: ${stop['transportation_cost']}")
            print(f"Stop total: ${stop['stop_total']}")

            total_days += stop["stay_days"]

        print(f"\nTotal Days: {total_days}")
        print(f"Fixed Agency Fee: ${self.fixed_agency_fee}")
        print(f"Total Estimated Trip Cost: ${self.get_total_trip_cost()}")

    def save_plan(self, filename="saved_trip_plan.json"):
        data = {
            "client_name": self.client_name,
            "agency_name": self.agency_name,
            "special_requirements": self.special_requirements,
            "fixed_agency_fee": self.fixed_agency_fee,
            "stops": self.stops
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_plan(cls, filename="saved_trip_plan.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            planner = cls(
                data["client_name"],
                data["agency_name"],
                data.get("special_requirements", "")
            )
            planner.fixed_agency_fee = data.get("fixed_agency_fee", 120.0)
            planner.stops = data.get("stops", [])
            return planner
        except FileNotFoundError:
            return None

        for country, days in self.countries:
            print(f"{country}: {days} days")
            total_days += days

        print(f"Total days: {total_days}")