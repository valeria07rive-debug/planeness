class TripPlanner:

    def _init_(self, client_name):
        self.client_name = client_name
        self.countries = []
        self.days = {}

    def add_country(self, country, days):
        self.countries.append(country)
        self.days[country] = days