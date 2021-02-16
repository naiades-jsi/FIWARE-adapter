from typing import List
import time
import json
import schedule
import sys
import os

sys.path.append(os.path.abspath('./download'))

from APIClient import NaiadesClient

class DownloadScheduler():
    clients: List["NaiadesClient"]

    def __init__(self, configuration_path: str = None) -> None:
        self.configuration(configurationPath=configuration_path)
    
    def configuration(self, configurationPath: str = None) -> None:
        # Read config file
        full_path = "config/" + configurationPath
        with open(full_path) as data_file:
            conf = json.load(data_file)

        conf_clients = conf["clients"]
        self.clients = []

        for conf_client in conf_clients:
            path = "config/" + conf_client
            client = NaiadesClient(configurationPath=path)
            self.clients.append(client)

        # Schedule obtain calls (see schedule module documentation)
        for client in self.clients:
            if(client.seconds_between_samples is not None):
                # print("nope")
                schedule.every(client.seconds_between_samples).seconds.do(client.obtain)
            elif(client.second_in_minute is not None):
                if(client.period is not None):
                    schedule.every(client.period).minutes.at(client.second_in_minute).do(client.obtain)
                else:
                    schedule.every().minute.at(client.second_in_minute).do(client.obtain)
            elif(client.minute_in_hour is not None):
                # print("minute")
                if(client.period is not None):
                    schedule.every(client.period).hours.at(client.minute_in_hour).do(client.obtain)
                else:
                    schedule.every().hour.at(client.minute_in_hour).do(client.obtain)
            elif(client.hour_in_day is not None):
                #print(client.hour_in_day)
                if(client.period is not None):
                    schedule.every(client.period).days.at(client.hour_in_day).do(client.obtain)
                else:
                    schedule.every().day.at(client.hour_in_day).do(client.obtain)
            else:
                print("Client {} cant be scheduled.".format(client.entity_id))

    def run(self) -> None:
        while True:
            # run_pending obtain calls
            schedule.run_pending()
            time.sleep(1)
