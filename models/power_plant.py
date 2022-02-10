from math import floor, ceil


class PowerPlant:

    def __init__(self, name, ptype, efficiency, pmin, pmax, fuels):
        self.name = name
        self.ptype = ptype
        self.efficiency = efficiency
        self.pmin = pmin
        self.pmax = pmax
        self.get_fuel_cost(fuels)
        self.p = 0
        self.cost_per_mwh = self.calculate_cost_per_mwh()

    def get_pmin(self):
        return self.pmin

    def get_pmax(self):
        return self.pmax

    def set_p(self, val):
        if self.p == 0:
            self.p = val

    def get_name(self):
        return self.name

    def get_fuel_cost(self, fuels):
        if self.ptype == 'gasfired':
            # Take into account the cost of CO2
            # Take rounded cost (highest)
            self.fuel_cost = ceil(fuels['gas(euro/MWh)'] + (0.3 * 25))
            return
        if self.ptype == 'turbojet':
            self.fuel_cost = fuels['kerosine(euro/MWh)']
            return
        if self.ptype == 'windturbine':
            self.fuel_cost = 0
            # Nominal maximum power output is dependent on wind factor
            power_wind_factor = fuels['wind(%)'] / 100

            # Take worst case pmax
            self.pmax = floor(self.pmax * power_wind_factor)
            return

    def calculate_cost_per_mwh(self):
        # Take rounded cost (highest)
        return ceil(self.fuel_cost * (1.0/self.efficiency))

    def to_json(self):
        return {"name": self.name, "p": self.p}
