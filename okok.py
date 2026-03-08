class TripPlanner:

    def _init_(self, name):
        self.name = name
        self.countries = []

    def add_country(self, country, days):
        self.countries.append((country, days))
        print(f"{country} added for {days} days")

    def show_summary(self):
        print(f"\nTrip summary for {self.name}:")

        if not self.countries:
            print("No countries added yet")
            return

        total_days = 0

        for country, days in self.countries:
            print(f"- {country}: {days} days")
            total_days += days

        print(f"Total days: {total_days}")