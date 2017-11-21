# -*- coding: utf-8 -*-
#! /usr/bin/env python

import urllib2
import sys
import re
import time 

reload(sys)
sys.setdefaultencoding('utf-8')
print ('你好')
print sys.stdin.encoding
print sys.stdout.encoding 



k='11'
w='E'
AllData=[]
dic={}

class Stock():	
	def __init__(self, ID,Name,Type):
		self.ID=ID
		self.Name=Name
		self.Type=Type
		self.jbmgsy=[]
		self.kfmgsy=[]
		self.xsmgsy=[]
		self.mgjzc=[]
		self.mggjj=[]
		self.mgwfply=[]
		self.mgjyxjl=[]

		self.yyzsr=[]
		self.mlr=[]
		self.gsjlr=[]
		self.kfjlr=[]
		self.yyzsrtbzz=[]
		self.gsjlrtbzz=[]
		self.kfjlrtbzz=[]
		self.yyzsrgdhbzz=[]
		self.gsjlrgdhbzz=[]
		self.kfjlrgdhbzz=[]

		self.jqjzcsyl=[]
		self.tbjzcsyl=[]
		self.tbzzcsyl=[]
		self.mll=[]
		self.jll=[]
		self.sjsl=[]

		self.yskyysr=[]
		self.xsxjlyysr=[]
		self.jyxjlyysr=[]

		self.zzczzy=[]
		self.yszkzzts=[]
		self.chzzts=[]

		self.zcfzl=[]
		self.ldzczfz=[]
		self.ldbl=[]
		self.sdbl=[]

		




def GetStockInf(pStock,response):
	original=response.read()
	s2=r'"jbmgsy":"(.*?)\"'
	pat=re.compile(s2)
	pStock.jbmgsy = pat.findall(original)
	print len(pStock.jbmgsy)
	s2=r'"kfmgsy":"(.*?)\"'
	pat=re.compile(s2)
	pStock.kfmgsy = pat.findall(original)
	print len(pStock.kfmgsy)
	s2=r'"xsmgsy":"(.*?)\"'
	pat=re.compile(s2)
	pStock.xsmgsy = pat.findall(original)
	print len(pStock.xsmgsy)
	s2=r'"mgjzc":"(.*?)\"'
	pat=re.compile(s2)
	pStock.mgjzc = pat.findall(original)
	print len(pStock.mgjzc)
	s2=r'"mggjj":"(.*?)\"'
	pat=re.compile(s2)
	pStock.mggjj = pat.findall(original)
	print len(pStock.mggjj)
	s2=r'"mgwfply":"(.*?)\"'
	pat=re.compile(s2)
	pStock.mgwfply = pat.findall(original)
	print len(pStock.mgwfply)
	s2=r'"mgjyxjl":"(.*?)\"'
	pat=re.compile(s2)
	pStock.mgjyxjl = pat.findall(original)
	print len(pStock.mgjyxjl)







# for x in xrange(1,10):	
# 	test1=test(x)
# 	AllData.append(test1)
# 	dic[x]=test1
# output = open('data.pkl', 'wb')

# pickle.dump(AllData, output, True)
# pickle.dump(dic,output,True)

# output.close()


# pkl_file = open('data.pkl', 'rb')
# data1 = pickle.load(pkl_file)
# data2=pickle.load(pkl_file)
# pkl_file.close()
# print data1[2].ID
# print data2[2].ID


import urllib2
allStock=[]
response = urllib2.urlopen("http://quote.eastmoney.com/stocklist.html")
html= (response.read().decode('gbk'))

s1=r'<li><a target="_blank" href="http://quote.eastmoney.com/(\S+).html">(.*?)</a></li>'


pat=re.compile(s1)
code = pat.findall(html)


for item in code:	
	if item[1][item[1].find('(')+1:-1][0]=='0':
		pStock=Stock(item[1][item[1].find('(')+1:-1],item[1][:item[1].find('(')],'sz')		
		allStock.append(pStock)
	if item[1][item[1].find('(')+1:-1][0]=='6':
		pStock=Stock(item[1][item[1].find('(')+1:-1],item[1][:item[1].find('(')],'sh')	
		allStock.append(pStock)
	if item[1][item[1].find('(')+1:-1][0]=='3':
		pStock=Stock(item[1][item[1].find('(')+1:-1],item[1][:item[1].find('(')],'cy')	
		allStock.append(pStock)
	
print len(allStock)

# for stock in allStock:
# 	url='http://emweb.securities.eastmoney.com/FinanceAnalysis/Index?type=web&code=%s%s#'%(stock.Type,stock.ID)
for num in xrange(0,1):
	
	url="http://emweb.securities.eastmoney.com/PC_HSF10/FinanceAnalysis/FinanceAnalysisAjax?code=%s%s&ctype=0"%(allStock[num].Type,allStock[num].ID)
	response = urllib2.urlopen(url)
	# print response.read()
	GetStockInf(allStock[num],response)
	# time.sleep(1)

# response = urllib2.urlopen("http://emweb.securities.eastmoney.com/PC_HSF10/FinanceAnalysis/FinanceAnalysisAjax?code=sh600622&ctype=0")
# print  (response.read())

# s2=r'"jbmgsy":"(.*?)\"'


# pat=re.compile(s2)
# codes = pat.findall(response.read())

# for code in codes:
# 	print code

# pStock=Stock('600622','AAA','sz')


