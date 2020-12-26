import re, os, sys
import urllib
from urllib import request
from urllib.parse import quote
import requests
import config
from bs4 import BeautifulSoup as BS
import datetime

class kuplinov: 
	host = 'https://www.youtube.com/user/KuplinovPlay/videos'
	url = 'https://www.youtube.com'

	def new_games(self):
		newmas = []
		doc = urllib.request.urlopen(self.host).read().decode('cp1251',errors='ignore') 
		match = re.findall("\?v\=(.+?)\"",doc)
		if not (match is None):
			for ii in match:
				if(len(ii)<25):
					newmas.append(ii)
        
		newmas = dict(zip(newmas,newmas)).values()
		#mma=[]
		#for i in newmas:	  
		#	if(i!=self.lastkey):
		#		mma.append(i)	 
		#	else:  
		#	    break   
		#mas2=[]
		#for y in mma: mas2.append('https://www.youtube.com/watch?v='+y)        
        
		resMas = self.parsedate(newmas)
		return resMas 

	def parsedate(self, massive):
		resultM = []
		now  = datetime.datetime.now()
		prek = str(now.year)+str(now.month)+str(now.day)
		for i in massive:
			r = requests.get("https://www.youtube.com/watch?v="+i)
			html = BS(r.content, 'html.parser')
			res = str(html.div)
			date = res.find("datePublished")-12
			kost = date - 10
			topDate = res[kost:date]
			mas = topDate.split('-')
			year = mas[0]
			month = mas[1]
			day = mas[2]
			code = int(year+month+day)
			if(code == int(prek)):
				resultM.append(i)
		return resultM	
