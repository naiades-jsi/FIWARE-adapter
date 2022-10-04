import argparse
import json
import sys

from download.downloadScheduler import DownloadScheduler

scheduler = DownloadScheduler(configuration_path="downloadScheduler.json")

scheduler.run()
