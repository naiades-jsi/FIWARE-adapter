import argparse
import json
import sys

from download.downloadScheduler import DownloadScheduler

scheduler = DownloadScheduler(configuration_path="config/downloadScheduler.json")

scheduler.run()
