from typing import Any
import requests


from typing import Dict, Any

ip = "5.53.108.182"
port = "8668"


entity_from = {
    "urn:ngsi-ld:Device:Autobuses-Volume": "alicante",
    "urn:ngsi-ld:WeatherObserved:WeatherObserved-2": "alicante",
    "urn:ngsi-ld:WeatherObserved:WeatherObserved-1": "alicante",
    "urn:ngsi-ld:Alert:ES-Alert-AlicanteBenalua-13-2120201216-02": "alicante",
    "urn:ngsi-ld:Alert:ES-Alert-AlicanteBenalua20201216-02": "alicante",
    "Consumption:Spain-Consumption-Alicante-Benalua20201216-02": "alicante",
    "urn:ngsi-ld:Device:Benalua-Volume": "alicante",
    "urn:ngsi-ld:Device:Benalua-Flow": "alicante",
    "urn:ngsi-ld:Device:Autobuses-Volume": "alicante",
    "urn:ngsi-ld:Device:Autobuses-Flow": "alicante",
    "urn:ngsi-ld:Device:Diputacion-Volume": "alicante",
    "urn:ngsi-ld:Device:Diputacion-Flow": "alicante",
    "urn:ngsi-ld:Device:Mercado-Volume": "alicante",
    "urn:ngsi-ld:Device:Mercado-Flow": "alicante",
    "urn:ngsi-ld:Device:Alipark-Volume": "alicante",
    "urn:ngsi-ld:Device:Alipark-Flow": "alicante",
    "urn:ngsi-ld:Device:Montaneta-Volume": "alicante",
    "urn:ngsi-ld:Device:Montaneta-Flow": "alicante",
    "urn:ngsi-ld:Device:Rambla-Volume": "alicante",
    "urn:ngsi-ld:Device:Rambla-Flow": "alicante",
    "urn:ngsi-ld:Device:Device-test": "alicante",
    "urn:ngsi-ld:WeatherObserved:WeatherObserved": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-0": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-1": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-2": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-3": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-0": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-1": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-2": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-3": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-0": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-1": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-2": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-3": "braila",
    "urn:ngsi-ld:Device:Device-5770": "braila",
    "urn:ngsi-ld:Device:Device-5771": "braila",
    "urn:ngsi-ld:Device:Device-5772": "braila",
    "urn:ngsi-ld:Device:Device-5773": "braila",
    "urn:ngsi-ld:Device:Device-2182": "braila",
    "urn:ngsi-ld:Device:Device-5980": "braila",
    "urn:ngsi-ld:Device:Device-5981": "braila",
    "urn:ngsi-ld:Device:Device-5982": "braila",
    "urn:ngsi-ld:Device:Device-test": "braila",
    "urn:ngsi-ld:Device:Device-test2": "braila",
    "urn:ngsi-ld:FlowerBed:FlowerBed-test": "braila",
    "PlantsWateringPredicted:CH-PlantsWateringPredicted-Carouge-20201215-19": "braila",
    "urn:ngsi-ld:Device:Device-318505H498": "braila",
    "urn:ngsi-ld:Device:Device-211306H360": "braila",
    "urn:ngsi-ld:Device:Device-211106H360": "braila",
    "urn:ngsi-ld:Device:Device-211206H360": "braila",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-0": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-1": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-2": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-3": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-0": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-1": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-2": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-3": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-0": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-1": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-2": "carouge",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-3": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-3": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-4": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-5": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-6": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-7": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-8": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-2": "carouge",
    "urn:ngsi-ld:WaterQualityObserved:Fountain-1": "carouge",
    "urn:ngsi-ld:FountainUsageObserved:Fountain-1": "carouge",
    "urn:ngsi-ld:WaterQualityForecast:Fountain-1": "carouge",
    "urn:ngsi-ld:WeatherObserved:WeatherObserved": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-1": "carouge",
    "urn:ngsi-ld:Device:Device-0972": "carouge",
    "urn:ngsi-ld:Device:Device-0a35": "carouge",
    "urn:ngsi-ld:Device:Device-0a6a": "carouge",
    "urn:ngsi-ld:Device:Device-0a7c": "carouge",
    "urn:ngsi-ld:Device:Device-0a7d": "carouge",
    "urn:ngsi-ld:Device:Device-0a80": "carouge",
    "urn:ngsi-ld:Device:Device-0a81": "carouge",
    "urn:ngsi-ld:Device:Device-0a83": "carouge",
    "urn:ngsi-ld:Device:Device-1f0d": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-test": "carouge",
    "PlantsWateringPredicted:CH-PlantsWateringPredicted-Carouge-20201215-19": "carouge",
    "PlantsWateringPredicted:CH-PlantsWateringPredicted-Carouge-test-20201215-19": "carouge",
    "Alert:1": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-15": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-200": "carouge",
    "Alert:200": "carouge",
    "Alert:201": "carouge",
    "Alert:50": "carouge",
    "Alert:": "carouge",
    "urn:ngsi-ld:FlowerBed:": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-51": "carouge",
    "urn:ngsi-ld:FlowerBed:FlowerBed-9": "carouge",
    "urn:ngsi-ld:WaterQualityObserved:WaterTreatmentPlant": "wtp_lab",
    "urn:ngsi-ld:WaterQualityForecast:WaterTreatmentPlant": "wtp_lab",
    "urn:ngsi-ld:WeatherObserved:WeatherObserved": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-0": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-1": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-2": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-3": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-0": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-1": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-2": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-3": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-0": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-1": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-2": "wtp_lab",
    "urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-3": "wtp_lab",
    "urn:ngsi-ld:WaterQualityObservedFake:WaterQualityObservedFake": "wtp_lab"    
    }

def status(entity_id: str, service: str) -> Dict[str, Any]:
    # Base URL and headers construction
    base_url = "http://" + ip + ":" + port + "/v2/entities/" + entity_id + "?limit=100000"
    headers = {
        "Fiware-Service": service,
        "Fiware-ServicePath": "/",
        "Content-Type": "application/json"
    }

    ret_dict = {}
    sample_count = 0

    # Send the get request
    r = requests.get(base_url, headers=headers)
    # If request failed output just that
    if(r.status_code != requests.codes.ok):
        ret_dict["http_status"] = r.status_code
        return ret_dict
    else:
        ret_dict["http_status"] = 200
    body = r.json()
    timestamps = body["index"]
    sample_count += len(timestamps)
    ret_dict["first_date"] = timestamps[0]
    last_date = timestamps[-1]

    while(len(timestamps) == 10000):
        # Send the get request
        new_url = base_url + "&fromDate=" + last_date
        r = requests.get(new_url, headers=headers)
        # If request failed output just that
        if(r.status_code != requests.codes.ok):
            ret_dict["http_status"] = r.status_code
            return ret_dict
        body = r.json()
        timestamps = body["index"]
        # First sample was already included in the last batch
        sample_count += (len(timestamps)-1)
        last_date = timestamps[-1]

    ret_dict["sample_count"] = sample_count
    ret_dict["last_date"] = timestamps[-1]

    return ret_dict
