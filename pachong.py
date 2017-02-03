#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
if __name__=='__main__':
    #请求
    url = "http://www.maiziedu.com/course/teachers/"
    #头部
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0'}
    request = urllib2.Request(url=url,headers=headers)

    #接收
    response = urllib2.urlopen(request)
    print response.read()