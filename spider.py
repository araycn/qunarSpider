# -*- coding: utf-8 -*-

import re
import selenium
import time
from selenium import webdriver

driver = webdriver.Firefox()
starting = "沈阳"
destination = "上海"
depart_time = "2016-02-02"
QUNAR_URL = "http://flight.qunar.com/site/oneway_list.htm"
current_url = "%s?searchDepartureAirport=%s&searchArrivalAirport=%s&searchDepartureTime%s"\
                %(QUNAR_URL,starting,destination,depart_time)
driver.get(current_url)
time.sleep(100)
print(driver.page_source)
