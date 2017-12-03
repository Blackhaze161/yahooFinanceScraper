import urllib.request
import os
import csv


def get_financial_history():
    download_path = os.path.join(os.path.dirname(__file__), '../output/')
    print(download_path)

