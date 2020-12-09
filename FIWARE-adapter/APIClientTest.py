from time import sleep
import sys
import os

sys.path.append(os.path.abspath('./download'))

from APIClient import NaiadesClient
from output import KafkaOutput


# Expected time interval in seconds
time_interval = 30
client = NaiadesClient("config/APIClientConfiguration.json")

while(True):
    client.obtain()
    sleep(time_interval)
