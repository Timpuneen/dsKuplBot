import re, os, sys
import urllib
from urllib import request
from urllib.parse import quote
import requests
import config

class kuplinov: 
	host = 'https://www.youtube.com/user/KuplinovPlay/videos'
	url = 'https://www.youtube.com'
	lastkey = ""

	def __init__(self):
		self.lastkey = config.lastkey  

	def new_games(self):
		newmas = []
		doc = urllib.request.urlopen(self.host).read().decode('cp1251',errors='ignore') 
		match = re.findall("\?v\=(.+?)\"",doc)
		if not (match is None):
			for ii in match:
				if(len(ii)<25):
					newmas.append(ii)
        
		newmas = dict(zip(newmas,newmas)).values()
		mma=[]
        
		for i in newmas:	  
			if(i!=self.lastkey):
				mma.append(i)	 
			else:  
			    break   

		mas2=[]
		for y in mma: mas2.append('https://www.youtube.com/watch?v='+y)        
		return mma             


	def update_lastkey(self, new_key):
		self.lastkey = new_key
		config.lastkey = str(new_key)

		return new_key