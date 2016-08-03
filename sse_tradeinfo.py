import json
import httplib2
import time
import sys
sys.path.append('the path to this repo')
from emailTradeinfo import *

dt = time.strftime("%Y-%m-%d")
#url ='http://query.sse.com.cn/infodisplay/showTradePublicFile.do?dateTx=%s' % '2016-08-01'
url ='http://query.sse.com.cn/infodisplay/showTradePublicFile.do?dateTx=%s' % dt

def parse_web():
    n = 0
    print(time.ctime() + ' -- ' + url)

    while n < 3:
        n += 1
        try:
            http = httplib2.Http()
            headers = {'Referer': 'http://www.sse.com.cn/disclosure/diclosure/public/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.8 Safari/537.36'
            }
            response, content = http.request(url, 'GET', headers=headers)
            c = json.loads(content.decode(encoding='utf-8'))

            if c['fileContents']==None:
                print('No contents today!')
            else:
                a = c['fileContents'] #type list
                EmailContent= '\n'.join(a)
                output = open('tradeinfo_%s' % dt, 'w')
                l = len(a)
                i=0

                while i < l:
                    i += 1
                    print(a[i-1] + '\r')
                    #output.write(a[i-1] + '\r')

            n = 10
            #output.close()
        except:
            print("test "+str(n))
            time.sleep(10)
    return EmailContent




if __name__ == '__main__':
    send_mail(mailto_list,"today's trade info",tradeinfo)





