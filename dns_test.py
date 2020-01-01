#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  dns.resolver
import  os
import http.client

iplist = []
appdomain = 'www.google.com'

def get_iplist(domain=""):
    '''域名解析函数，解析成功的IP将追加到iplist列表'''
    try:
        A = dns.resolver.query(domain,'A') #解析A记录
    except Exception as e:
        print ("dns resolver error:" + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                iplist.append(j.address) #追加到iplist
    return True


def checkip(ip):
    '''对IP列表进行http级别探测'''
    checkurl = ip+":80"
    getcontent = ""

    conn = http.client.HTTPConnection(checkurl, timeout= 3) #创建http连接对象
    try:
        conn.request(method="GET", url=checkurl, headers={"Host": appdomain})  #发起URL请求，添加host主机头
        r = conn.getresponse()
        print(r.status)
    finally:
        if getcontent=="200":  #监控URL页的内容一般是事先定义好，比如“HTTP200”等
            print (ip+" [OK]")
        else:
            print (ip+" [Error]")    #此处可放告警程序，可以是邮件、短信通知

if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist)>0:    #条件：域名解析正确且至少要返回一个IP
        for ip in iplist:
            checkip(ip)
    else:
        print ("dns resolver error.")