from yahooFinanceScraper.jsonreader import get_tickers
from yahooFinanceScraper.dategroup import get_time_group
from yahooFinanceScraper.cookiecrumb import get_crumb
from yahooFinanceScraper.downloader import get_financial_history


def yahoo_finance_run():
    ticker_map = get_tickers()
    for ticker in ticker_map:
        download_historical(ticker_map[ticker])


def download_historical(ticker):
    date_set = get_time_group()
    crumb = get_crumb(ticker)
    get_financial_history(ticker, date_set, crumb)



