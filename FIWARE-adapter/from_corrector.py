import json

with open("config/productionInflux/downloadScheduler.json") as data_file:
    conf = json.load(data_file)

conf_clients = conf["clients"]

for conf_client in conf_clients:
    path = "config/" + conf_client
    use_case = conf_client.split("/")[1]
    file_name = conf_client.split("/")[2]
    print(file_name)
    with open(path) as data_file_old:
        with open("config/productionSIMAVI/" + use_case + "/" + file_name, "r") as data_file_new:
            conf_new = json.load(data_file_new)
            conf_old = json.load(data_file_old)
        with open("config/productionSIMAVI/" + use_case + "/" + file_name, "w") as data_file_new_r:
            conf_new["from"] = conf_old["from"]
            json.dump(conf_new, data_file_new_r)
