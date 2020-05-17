import json

import urequests as requests


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
