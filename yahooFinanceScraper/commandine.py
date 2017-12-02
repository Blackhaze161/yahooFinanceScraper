from yahooFinanceScraper.jsonreader import get_tickers
from yahooFinanceScraper.dategroup import get_time_group
from yahooFinanceScraper.cookiecrumb import get_crumb


def yahoo_finance_run():
    tickers = get_tickers()
    date_set = get_time_group()
    crumb = get_crumb("KO")


