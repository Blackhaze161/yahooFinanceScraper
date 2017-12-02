import urllib.request
import re



def get_crumb(symbol):
    cookie_crumb = parse_page(symbol)

    return cookie_crumb


def parse_page(symbol):
    yahoo = "https://finance.yahoo.com/quote/%s?p=%s" % (symbol, symbol)

    tmp_file, headers = urllib.request.urlretrieve(yahoo)
    find_crumb_store(tmp_file)

    return "Filler"


def find_crumb_store(tmp_file):
    regex = re.compile('"CrumbStore":{"crumb":".*?"}')
    for line in open(tmp_file):
        match = regex.search(line)
        if match:
            print(match.group(0))









