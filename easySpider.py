# -*- coding: utf-8 -*-

import re
from urllib2 import Request
import urllib2
from bs4 import BeautifulSoup
from config import *
QUNAR_URL = "http://flight.qunar.com/site/oneway_list.htm"
query_url = "%s?searchDepartureAirport=%s&searchArrivalAirport=%s&searchDepartureTime%s"\
                %(QUNAR_URL, START_CITY, DES_CITY, LAUNCH_TIME)

req = Request(query_url)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
response =  urllib2.urlopen(req)
response_html = response.read().decode('utf-8')

soup = BeautifulSoup(response_html)
result_url = soup.form.input['value']
req = Request(result_url)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
response = urllib2.urlopen(req)

response_html = response.read().decode('utf-8')

font_pattern = re.compile(r'font-face.*?\'(.*?)\'')
key_word = ""
for line in response_html.split('\n'):
    match = font_pattern.search(line)
    if match:
        key_word = match.group(1)
        break

print "key_word -->",key_word

soup = BeautifulSoup(response_html)
price_pattern = re.compile(r'<.*?>(.*)<.*?>')
for i in  soup.findAll(attrs={"class":"price {0}".format(key_word)}):
    print i.string
