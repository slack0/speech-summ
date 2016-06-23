
import os, sys, argparse, pprint
from pyteaser import SummarizeUrl

pp = pprint.PrettyPrinter(indent=4)

parser = argparse.ArgumentParser()
parser.add_argument('-u', action='store', dest='url_list', help='path to url list')
results = parser.parse_args()
urls = results.url_list

if os.path.isfile(urls):
    with open(urls) as f:
        l = f.readlines()
        for url in l:
            summaries = SummarizeUrl(url)
            pp.pprint('*'*40)
            pp.pprint(summaries)


