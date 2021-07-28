import argparse
import sys
import requests
import time
import logging

#from datetime import datetime
from multiprocessing import Process
from time import sleep
from download.downloadScheduler import DownloadScheduler


def ping_watchdog(process):
    interval = 30 # ping interval in seconds
    url = "localhost"
    port = 5001
    path = "/pingCheckIn/Data adapter"
    print("start ping")
    while(process.is_alive()):
        #print("{}: Pinging.".format(datetime.now()))
        try:
            r = requests.get("http://{}:{}{}".format(url, port, path))
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            logging.warning(e)
        else:
            logging.info('Successful ping at ' + time.ctime())
        sleep(interval)

def start_scheduler(path):
    scheduler = DownloadScheduler(configuration_path=path)
    scheduler.run()

def main():
    parser = argparse.ArgumentParser(description="scheduler")

    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        help=u"Config file located in ./config/ directory."
    )

    parser.add_argument(
        "-w",
        "--watchdog",
        dest="watchdog",
        action='store_true',
        help=u"Ping watchdog",
    )

    # Display help if no arguments are defined
    if (len(sys.argv) == 1):
        parser.print_help()
        sys.exit(1)

    # Parse input arguments
    args = parser.parse_args()

    

    # Ping watchdog every 30 seconds if specfied
    if (args.watchdog):
        logging.info("=== Watchdog started ===")

        # Run and save a parelel process
        # Start periodic download
        process = Process(target=start_scheduler, args=(str(args.config),))
        process.start()

        # On the main thread ping watchdog if child process is alive
        ping_watchdog(process)
    else:
        scheduler = DownloadScheduler(configuration_path=args.config)
        # Start periodic download
        scheduler.run()


if (__name__ == '__main__'):
    main()
