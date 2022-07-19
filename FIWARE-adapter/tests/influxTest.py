from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import ASYNCHRONOUS, SYNCHRONOUS

influx_writer = InfluxDBClient(url="http://localhost:8086", token="DakOTf1sdfD-Nse4__JJv1QYhpSpX-fO2_ZjxEgKDPF_Y-M50hifUTmkkPARjIb_TZONwaZvfLIweQ72eAqsvA==",
                                org="naiades").write_api(write_options=SYNCHRONOUS)

k = influx_writer.write("alicante", "naiades",
                                    [{"measurement": "salinity_EA001_36_level",
                                    "tags": {}, "fields": {"value": 7.5},
                                    "time": 1657548668000000000}])

print(k)