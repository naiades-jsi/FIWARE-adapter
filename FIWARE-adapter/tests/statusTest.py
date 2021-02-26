import sys
import os
import json

sys.path.append(os.path.abspath('../download'))

import status

with open("statusTest.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:WeatherObserved:WeatherObserved", "braila"), s)