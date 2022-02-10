from flask import jsonify
from models.power_plant import PowerPlant
from helpers.powerplant_calculations import get_total_achievable_load, powerplant_uc_solver


def handle_powerplant_post(request):
    json = request.get_json()
    try:
        load = json["load"]
        fuels = json["fuels"]
        powerplants = json["powerplants"]
        power_plant_objects = []

        total_achieveable_load = 0

        for plant in powerplants:
            power_plant_objects.append(PowerPlant(
                plant["name"], plant["type"], plant["efficiency"],
                plant["pmin"], plant["pmax"], fuels)
            )

        total_achieveable_load = get_total_achievable_load(power_plant_objects)

        if load > total_achieveable_load:
            raise ValueError("Required load cannot be obtained by these powerplants, the maximum power output of this configuration is: {}".format(
                total_achieveable_load))

        results = powerplant_uc_solver(power_plant_objects, load)

        return json, results
    except KeyError as e:
        raise KeyError(
            "The requested key: {} does not exist in the POST request".format(e.args[0]))
