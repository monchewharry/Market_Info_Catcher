# -*- coding: UTF-8 -*-
import json
import httplib2
import sqlite3
import time
import sys
sys.path.append('path to this repo')
from emailTradeinfo import *

dt_sz = time.strftime("%y%m%d")
dt_ss = time.strftime("%Y-%m-%d")
url_ss ='http://query.sse.com.cn/infodisplay/showTradePublicFile.do?dateTx=%s' % dt_ss
url_sz ='http://www.szse.cn/szseWeb/common/szse/files/text/jy/jy%s.txt' % dt_sz

def parse_web_sz():
    n = 0
    print(time.ctime() + ' -- ' + url_sz)
    while n < 3:
        n += 1
        try:
            http = httplib2.Http()
            headers = {'Referer': 'http://www.szse.cn/main/disclosure/news/scgkxx/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.8 Safari/537.36'
            }
            response, content = http.request(url_sz, 'GET', headers=headers)
            c = content.decode(encoding='gb2312')#txt
            print(c)
        except Exception as e:
            print(str(e))
            print("test "+str(n))
            time.sleep(5)
    return c

def parse_web_ss():
    n = 0
    print(time.ctime() + ' -- ' + url_ss)
    while n < 3:
        n += 1
        try:
            http = httplib2.Http()
            headers = {'Referer': 'http://www.sse.com.cn/disclosure/diclosure/public/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.8 Safari/537.36'
            }
            response, content = http.request(url_ss, 'GET', headers=headers)
            c = json.loads(content.decode(encoding='utf-8'))

            if c['fileContents']== None:
                return ''
            else:
                a = c['fileContents'] #type list
                EmailContent= '\n'.join(a)
                l = len(a)
                i=0

                while i < l:
                    i += 1
                    print(a[i-1] + '\r')
            n = 10
        except:
            print("test "+str(n))
            time.sleep(5)
    return EmailContent


if __name__ == '__main__':
    c_sz=parse_web_sz() 
    c_ss = parse_web_ss()
    errorInfo='抱歉，您访问的页面不存在或有异常'
    if c_sz.find(errorInfo) > -1 and len(c_ss)<1:
        print('SZE No contents today!')
        print('SSE No contents today!')
    else:
        c_sz=c_sz + '\n 信息来自深圳证券交易所：http://www.szse.cn/ \n \n' +('='*100) +'\n'
        c_ss = c_ss + '\n 信息来自上海证券交易所：http://www.sse.com.cn/'
        send_mail(mailto_list,"两市最新交易披露", c_sz+c_ss)







