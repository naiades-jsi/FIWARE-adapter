import sys
import os
import json

sys.path.append(os.path.abspath('../download'))

import status

with open("5980.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-5980", "braila"), s)

with open("5981.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-5981", "braila"), s)

with open("5982.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-5982", "braila"), s)

with open("2182.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-2182", "braila"), s)

with open("5770.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-5770", "braila"), s)

with open("5771.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-5771", "braila"), s)

with open("5772.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-5772", "braila"), s)

with open("5773.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-5773", "braila"), s)

with open("318505H498.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-318505H498", "braila"), s)

with open("211306H360.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-211306H360", "braila"), s)

with open("211106H360.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-211106H360", "braila"), s)

with open("211206H360.json", "w") as s:
    json.dump(status.status("urn:ngsi-ld:Device:Device-211206H360", "braila"), s)
