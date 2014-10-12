#!/usr/bin/env python
# encoding: utf-8
from pyquery import PyQuery as pyq
from time import sleep
import urllib2 as ul
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
fr = open('uindex')
pfr = file('uinfo','wb')
a = 1
for line in fr:
    if a is 300:
        sleep(100)
        a = 1
    tmp = line.split()
    uname = tmp[0]
    u_url = r'http://www.douban.com/people/'+uname
    image_path = r'avatars/'+uname+'.jpg'
    doc = pyq(url=u_url)
    user_info = doc('#db-usr-profile')
    if user_info.find('img').attr('src') is not None:
        iurl = user_info.find('img').attr('src')
        nick = user_info.find('h1').text()
        print uname+' '+nick
        pfr.write(uname+' '+nick)
        pfr.write('\n')
        data = ul.urlopen(iurl).read()
        ifr = file(image_path,"wb")
        ifr.write(data)
        ifr.close()
    sleep(3)
    a = a+1
