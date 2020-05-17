
from lib import WorkerWeatherSearch
import time

while True:
    weather = WorkerWeatherSearch()
    print(weather.search(41, -81.5))
    time.sleep(3)

