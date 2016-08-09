import urllib.request as request
import re
import bs4
import time
import sys
sys.path.append('path to this repo')
from emailTradeinfo import *

page = request.urlopen('http://www.news.cn/fortune/').read()
page = page.decode(encoding='utf-8')
dt = time.strftime("%Y-%m/%d")
soup = bs4.BeautifulSoup(page,"lxml")#解析树
link = re.compile("^(http://news.xinhuanet.com/fortune/|http://news.xinhuanet.com/finance/)%s.*$" % dt )
result=soup.findAll(target="_blank",href= link) 
parent1='h3'

macro = []
security =[]
company =[]
for item in result:
	if item.parent.name == 'h3' and item.parent.parent.name =='li': 
		if 'class' in item.parent.parent.attrs.keys():
			if item.parent.parent.parent.attrs['id'] == 'showData0':
				macro.append(item.text)
			if item.parent.parent.parent.attrs['id'] == 'showData1':
				security.append(item.text)
			if item.parent.parent.parent.attrs['id'] == 'showData2':
				company.append(item.text)

print('\n' + "宏观头条"+'\n')
ms = ""
for i in range(len(macro)):
	ms += str(i+1)+ '、' +macro[i] + '\n'

print('\n' + "证券头条"+'\n')
ss = ""
for i in range(len(security)):
	ss += str(i+1)+ '、' +security[i] + '\n'

print('\n' + "公司头条"+'\n')
cs = ""
for i in range(len(company)):
	cs += str(i+1)+ '、' +company[i] + '\n'
	


if __name__ == '__main__':
	mailcontent = '\n' + "宏观头条"+'\n' + ms + '\n' + "证券头条"+'\n'+ ss + '\n' + "公司头条"+'\n' + cs
	#print(mailcontent)
	send_mail(mailto_list,"新华社财经头条摘要", mailcontent + '\n详细内容请登录官网：www.news.cn/fortune/')








		



#关于bs4 关注https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id20

