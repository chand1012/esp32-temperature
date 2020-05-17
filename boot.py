import network
import webrepl
import time

WiFi = network.WLAN(network.STA_IF)
WiFi.active(True)

WiFi.connect('','')
webrepl.start()

print("Waiting for connection...")

while not WiFi.isconnected():
    pass

print("Done. Running main.py....")