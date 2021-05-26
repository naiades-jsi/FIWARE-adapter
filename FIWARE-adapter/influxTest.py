from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "mytoken"
org = "myorg"
bucket = "braila"

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

write_api.write(bucket, org, [{"measurement": "h2o_feet", "tags": {"location": "coyote_creek"}, "fields": {"water_level": 7}}])