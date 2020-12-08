import json

from download.APIClient import NaiadesClient
from download.output import KafkaOutput

client = NaiadesClient("config/APIClientConfiguration.json")