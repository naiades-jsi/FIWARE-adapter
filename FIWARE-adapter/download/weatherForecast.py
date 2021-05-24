import requests
import json
from datetime import date

def call_service(service):
    url = "http://5.53.108.182:1026/v2/entities/"
    # get forecast from alicante
    r = requests.get(url, headers={"Fiware-Service": service})
    if(r.status_code != requests.codes.ok):
        print("Data from {} could not be obtained. Error code: {}.".format(service, r.status_code))

    body = r.json()
    
    
    forecasts = []
    for entity in body:
        if(entity["type"] == "WeatherForecast"):
            forecasts.append(entity)
    
    return forecasts


def main():
    # get forecast from services
    alicante_forecasts = call_service("alicante")
    braila_forecasts = call_service("braila")
    carouge_forecasts = call_service("carouge")

    output = {
        "alicante": alicante_forecasts,
        "braila": braila_forecasts,
        "carouge": carouge_forecasts 
    }

    print(output)

    today = date.today().strftime("%d_%m_%Y")

    output_json = json.dumps(output)
    f = open("predicted_weather_"+today+".json","w")
    f.write(output_json)
    f.close()
    


if (__name__ == '__main__'):
    main()