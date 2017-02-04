import requests
import re
import sys
import unicodedata
from bs4 import BeautifulSoup
pin1 = open('websites.txt','r')
lines1 = pin1.readlines();
urls=[]

for line in lines1: 

	values1 = re.split('\n', line);

	urls.append("http://www."+str(values1[0])+"")

for i in range(0, len(urls)):

	try:
		url= urls[i]
		response = requests.get(url)
		soup = BeautifulSoup(response.text)
		metas = soup.find_all('meta')
		a=[ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ]
		# print a
		if a==[] or a==[u'']:
			print "N/A"
		if len(a) > 0:
			trans=a
			print trans;
		print '\n'

	except:
		print "N/A"
		continue;
