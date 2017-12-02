from yahooFinanceScraper.jsonreader import get_tickers
from yahooFinanceScraper.datetime import get_time_group


def yahoo_finance_run():
    tickers = get_tickers()
    date_set = get_time_group()


