import json

import urequests as requests

# this has been adapted for the urequests library
# originally from here:
# https://github.com/chand1012/discord-weather-bot/blob/204a78976cc4aedacb38d27f03311dea1d3d146d/weather.py#L6
class WorkerWeatherSearch():
    def __init__(self):
        self.lat = 41.08
        self.lng = -81.51
        self.base_url = "https://weather-api.chand1012.workers.dev"
        self.json = None
        self.forecasts = []

    def search(self, lat, lng):
        self.lat = lat
        self.lng = lng
        req = requests.post(self.base_url, headers={'content-type':'application/json'}, data=json.dumps({'lat':lat, 'lng':lng}))
        self.json = json.loads(req.text)
        self.forecasts = self.json['properties']['periods']
        return self.json
