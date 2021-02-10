import argparse
import json
import sys

from download.downloadScheduler import DownloadScheduler

def main():
    parser = argparse.ArgumentParser(description="scheduler")

    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        help=u"Config file located in ./config/ directory."
    )

    # Display help if no arguments are defined
    if (len(sys.argv) == 1):
        parser.print_help()
        sys.exit(1)

    # Parse input arguments
    args = parser.parse_args()

    scheduler = DownloadScheduler(configuration_path=args.config)

    scheduler.run()


if (__name__ == '__main__'):
    main()
