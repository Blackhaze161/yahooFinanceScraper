import json
import os


def get_tickers():
    data_file = os.path.join(os.path.dirname(__file__), '../input/tickers.json')
    data = json.load(open(data_file))
    return data
