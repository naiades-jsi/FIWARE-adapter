import json

with open("config/productionSIMAVI/downloadScheduler.json") as data_file:
    conf = json.load(data_file)

conf_clients = conf["clients"]

for conf_client in conf_clients:

    with open("config/" + conf_client, "r") as data_file_old:
        print(conf_client)
        conf_old = json.load(data_file_old)
        conf_old["from"] = "2022-08-05T21:30:00.000"
    
    with open("config/" + conf_client, "w") as wrt:
        json.dump(conf_old, wrt)
