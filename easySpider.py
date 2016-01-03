# -*- coding: utf-8 -*-

import re
import urllib2
from urllib2 import Request
from bs4 import BeautifulSoup
from config import *
import sys;
reload(sys)
sys.setdefaultencoding("utf-8")


class QunarSpider(object):
    """
    the Qunar.com spider to find whether there is ticket lower the the setting price
    """
    def __init__(self):
        """ constructiong funcion """
        self.qunar_url = "%s?searchDepartureAirport=%s&searchArrivalAirport=%s&searchDepartureTime%s"\
                %(QUNAR_URL, START_CITY, DES_CITY, LAUNCH_TIME)

    def get_query_page(self):
        """ get the query url for the ticket infomation page """
        req = Request(self.qunar_url)
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        try :
            response =  urllib2.urlopen(req)
            response_html = response.read().decode('utf-8')
            soup = BeautifulSoup(response_html)
            query_url = soup.form.input['value']
        except Exception,e:
            # if any exception, return None
            print e
            return None
        response.close()
        return query_url

    def get_font_key_word(self,response_html):
        """ get the font key word to check the price info futher """
        font_pattern = re.compile(r'font-face.*?\'(.*?)\'')
        for line in response_html.split('\n'):
            match = font_pattern.search(line)
            if match:
                return match.group(1)
        # if pattern not found
        return None

    def get_ticket_info(self):
        """ get ticket infomation to find if there is any ticket avialble """
        query_url = self.get_query_page()
        if not query_url:
            return None
        print "Spider-INFO::Going... to the page %s,to check if there is any affordable ticket" %query_url
        req = Request(query_url)
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        try:
            response = urllib2.urlopen(req)
            response_html = response.read().decode('utf-8')
        except Exception,e :
            print e
            return None
        response.close()

        key_word = self.get_font_key_word(response_html)
        if not key_word:
            return None
        print "Spider-INFO::found the price font-pattern: %s" %key_word
        soup = BeautifulSoup(response_html)
        res = ""
        for i in  soup.findAll(attrs={"class":"price {0}".format(key_word)}):
            price =  int(unicode(i.string).encode('utf-8'))
            if price < AFFORD_PRICE:
                res += str(price)+"RMB   "
        return res

if __name__ =="__main__":
    qunar_spider = QunarSpider()
    res = qunar_spider.get_ticket_info()
    print res
