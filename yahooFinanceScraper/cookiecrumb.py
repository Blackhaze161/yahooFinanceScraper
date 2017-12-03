import urllib.request
import re


def get_crumb(symbol):
    cookie_crumb = parse_page(symbol)
    return cookie_crumb


def parse_page(symbol):
    yahoo = "https://finance.yahoo.com/quote/%s?p=%s" % (symbol, symbol)
    tmp_file, headers = urllib.request.urlretrieve(yahoo)
    crumb_store = find_crumb_store(tmp_file)
    crumb = find_crumb(crumb_store)
    return crumb


def find_crumb_store(tmp_file):
    regex = re.compile('"CrumbStore":{"crumb":".*?"}')
    for line in open(tmp_file):
        match = regex.search(line)
        if match:
            return match.group(0)


def find_crumb(cookie_store):
    sliced = cookie_store.split(':')
    crumb = sliced[2][1:-2]  # remove first and last 2 chars in string
    return crumb






