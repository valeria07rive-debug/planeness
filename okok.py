class TripPlanner:

    def _init_(self, client_name):
        self.client_name = client_name
        self.countries = []
        self.days = {}

    def add_country(self, country, days):
        self.countries.append(country)
        self.days[country] = days

        def estimate_cost(self):

        DAILY_COST = 120
        TRANSPORT = 300
        AGENCY_FEE = 200

        total_days = sum(self.days.values())

        cost = total_days * DAILY_COST

        if len(self.countries) > 1:
            cost += TRANSPORT * (len(self.countries) - 1)

        cost += AGENCY_FEE

        return cost