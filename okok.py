class TripPlanner:

    def _init_(self, client_name):
        self.client_name = client_name
        self.countries = []

    def add_country(self, country, days):
        self.countries.append((country, days))
        print(f"{country} added for {days} days.")

    def show_summary(self):

        print(f"\nTrip summary for {self.client_name}")

        total_days = 0

        for country, days in self.countries:
            print(f"{country}: {days} days")
            total_days += days

        print(f"Total days: {total_days}")