#!/usr/bin/env python
# encoding: utf-8
from pyquery import PyQuery as pyq
from time import sleep
import urllib2 as ul
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
urls=[]
url1='http://flight.qunar.com/site/oneway_list_inter.htm?searchDepartureAirport=%E9%A6%99%E6%B8%AF&searchArrivalAirport=%E6%97%A7%E9%87%91%E5%B1%B1&searchDepartureTime=2014-08-13&searchArrivalTime=2014-08-13&nextNDays=0&startSearch=true&from=tejia_rili'
url2='http://flight.qunar.com/site/oneway_list_inter.htm?searchDepartureAirport=%E9%A6%99%E6%B8%AF&searchArrivalAirport=%E6%97%A7%E9%87%91%E5%B1%B1&searchDepartureTime=2014-08-12&searchArrivalTime=2014-08-13&nextNDays=0&startSearch=true&from=tejia_rili'
url3='http://flight.qunar.com/site/oneway_list_inter.htm?searchDepartureAirport=%E9%A6%99%E6%B8%AF&searchArrivalAirport=%E6%97%A7%E9%87%91%E5%B1%B1&searchDepartureTime=2014-08-14&searchArrivalTime=2014-08-13&nextNDays=0&startSearch=true&from=tejia_rili'
urls.append(url1)
urls.append(url2)
urls.append(url3)
while 1:
    for l in urls:
        doc=pyq(url=l)
        model=doc('.a_model')#.filter(lambda i: pyq(this).find('strong').text() == 'CX870')
        print model.html()#.find('strong')
