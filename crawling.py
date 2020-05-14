from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import re
import requests

# 1. csv file open
csv_filename_to_write = "billboard.csv"
csv_open = open(csv_filename_to_write, 'w+', encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow( ('rank','title','artist'))

# 2. BeautifulSoup
crawling_url = "https://www.billboard.com/charts/hot-100"
req = requests.get(crawling_url)
html = req.text
bs = BeautifulSoup(html, 'html.parser')

li_list = bs.findAll('li', {'class':re.compile("chart-list__element")})
for li in li_list:
    # rank
    span_rank = li.find('span',{'class':re.compile("chart-element__rank__number")})
    rank = span_rank.text

    # title
    span_title = li.find('span',{'class':re.compile("chart-element__information__song")})
    title = span_title.text

    # artist
    span_artist = li.find('span',{'class':re.compile("chart-element__information__artist")})
    artist = span_artist.text

    csv_writer.writerow( (rank, title, artist))

csv_open.close()