class TripPlanner:

    def _init_(self, client_name):
        self.client_name = client_name
        self.countries = []

    def add_country(self, country, days):
        self.countries.append((country, days))
        print(f"{country} added for {days} days")

    def show_summary(self):

        print(f"\nTrip Summary for {self.client_name}")

        total = 0

        for country, days in self.countries:
            print(f"{country}: {days} days")
            total += days

        print(f"Total trip days: {total}")