import json
import os


def get_data():
    data_file = os.path.join(os.path.dirname(__file__), '../input/tickers.json')
    print(data_file)
    print(json.load(data_file))