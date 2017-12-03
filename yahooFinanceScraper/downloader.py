import requests
import os


def get_financial_history(ticker, date_set, crumb):
    download_path = os.path.join(os.path.dirname(__file__), '../output/')
    file_name = "%s.csv" % ticker
    new_file = os.path.join(download_path, file_name)

    yahoo = "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%s&period2=%s&interval=1d&events=history" \
            "&crumb=%s" % (ticker, date_set['start_date'], date_set['end_date'], crumb['crumb'])

    temp = {'B': crumb['cookie']}  # requires a map in the GET request

    response = requests.get(yahoo, cookies=temp)

    with open(new_file, 'wb') as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

