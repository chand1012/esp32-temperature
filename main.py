
import time

from lib import WorkerWeatherSearch

while True:
    weather = WorkerWeatherSearch()
    print(weather.search(41, -81.5))
    time.sleep(3)
