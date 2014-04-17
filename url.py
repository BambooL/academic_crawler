import urllib
import urllib2,cookielib
import re
import csv

def url(entrance):
	
	i=1
	urllist=[]	
	while  True:
		url=entrance+"&start="+str(i)+"&end="+str(i+9)
		user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
		headers={'User-Agent':user_agent,'Referer':'http://academic.research.microsoft.com'} 

		response=urllib.urlopen(url,None,headers) #The assembled request

		for lines in response:
			if re.search("\_Title\"",lines):
				lines=re.sub(".*href=\"","",lines)
				lines=re.sub("\">.*<\/a>","",lines)
				urllist.append(lines)
				print lines 

		i=i+10

		if response ==None:
			break
	return urllist
	# if i>51:
	# 	break

# for items in urllist:
# 	print items
List=[]
entrance="http://academic.research.microsoft.com/Detail?entitytype=8&searchtype=2&id=32912&orderBy=1"
List=url(entrance)

