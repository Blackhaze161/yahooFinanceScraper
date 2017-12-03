from yahooFinanceScraper.jsonreader import get_tickers
from yahooFinanceScraper.dategroup import get_time_group
from yahooFinanceScraper.cookiecrumb import get_crumb
from yahooFinanceScraper.downloader import get_financial_history


def yahoo_finance_run():
    tickers = get_tickers()
    date_set = get_time_group()
    #crumb = get_crumb("KO")
    get_financial_history()



