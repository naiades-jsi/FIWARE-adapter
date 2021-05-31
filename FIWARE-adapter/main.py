import argparse
import json
import sys
import requests
import time
import logging
import threading
from datetime import datetime

from download.downloadScheduler import DownloadScheduler


def ping_watchdog():
    interval = 30 # ping interval in seconds
    url = "localhost"
    port = 5001
    path = "/pingCheckIn/Data adapter"

    # print("{}: Pinging.".format(datetime.now()))
    
    try:
        r = requests.get("http://{}:{}{}".format(url, port, path))
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        logging.warning(e)
    else:
        logging.info('Successful ping at ' + time.ctime())
    threading.Timer(interval, ping_watchdog).start()

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

    scheduler = DownloadScheduler(configuration_path=args.config)

    # Ping watchdog every 30 seconds if specfied
    if (args.watchdog):
        logging.info("=== Watchdog started ===")
        ping_watchdog()

    # Start periodic download
    scheduler.run()


if (__name__ == '__main__'):
    main()
