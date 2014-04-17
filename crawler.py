import os
import re
import csv
import sys
import urllib
import urllib2,cookielib



name=[]
author=[]
conference=[]
abstract=[]

def crawl(link):

    # for i in range (0,320):
    #     name.append(i)
    #     author.append(i)
    #     conference.append(i)
    #   abstract.append(i)
    # i=-1

    url="http://academic.research.microsoft.com/"+link
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    headers={'User-Agent':user_agent,} 
    response=urllib.urlopen(url,None,headers) #The assembled request
    name=""
    author=""
    conference=""
    abstract=""
    # for file in os.listdir('.'):
    #   f=open(file)
    #      i=i+1
    for lines in response:

        if re.search("\<title\>.*\<\/title\>",lines):
                r=lines.replace("<title>","")
                r=r.replace("&#58;","")
                r=re.sub("\r\n","",r)
                name=r.replace("</title>","")
                

        if re.search("\<.*content\=\"Authors\: .* Citations\: .*\" \/\>",lines):
                r=lines.replace("<meta name=\"description\" content=\"Authors: ","")
                r=re.sub(". Citations: \d*\" />","",r)
                r=re.sub("\r\n","",r)
                author=r
                

        if re.search("\<span id\=\"ctl00\_MainContent\_PaperItem\_txt.*\>",lines):
                r=re.sub("\<span id=\"ctl00_MainContent_PaperItem_txt.*\">","",lines)
                r=re.sub("</a>","",r)
                r=re.sub("&#40;","",r)
                r=re.sub("\r\n","",r)
                conference=r

        if re.search("\<span id=\"ctl00_MainContent_PaperItem_snippet\"\>",lines):
                r=re.sub("\<span id=\"ctl00_MainContent_PaperItem_snippet\"\>","",lines)
                r=re.sub("Categories and Subject Descriptors .*\<\/span\>\<\/div\>","",lines)
                r=re.sub("<\/span\>\<\/div\>","",lines)
                abstract=r
    
    return (name, author, conference, abstract)

if __name__ == "__main__":
    data=[]
    N=[]
    AU=[]
    C=[]
    A=[]
    extractor=()
    file=open("url.txt")
    i=0
    for lines in file:
        extractor=crawl(lines)
        data.append(extractor)
        writer=csv.writer(open('test.csv', 'a+b'))
        print extractor
        i+=1
   






