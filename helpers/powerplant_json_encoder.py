from flask.json import JSONEncoder
from models.power_plant import PowerPlant


class PowerPlantJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PowerPlant):
            return obj.to_json()
        return JSONEncoder.default(self, obj)
