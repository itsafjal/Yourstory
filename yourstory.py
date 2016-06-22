#! /usr/bin/python
#mport socks
import httplib2
import socket
from bs4 import BeautifulSoup, SoupStrainer
#import requests
import urllib2
import csv
'''
wiki = "http://www.yourstory.com/"

page = urllib2.urlopen(wiki)

soup = BeautifulSoup(page)

print(soup.title.string)
print(soup.a)

#for i in soup.find_all("div", class_="title-small bentonCondensed bold color-black-2 truncate-3 mt-15"):
#	print(i)

for link in soup.find_all("a", class_="content block"):
	print(link)

'''


url = "http://yourstory.com/2016/05/ola-luxury-range/"

page = urllib2.urlopen(url)

soup = BeautifulSoup(page)

print(soup.title.string)
#print(soup.a)


'''
f = open("1.txt","r")
for i in soup.find_all("div", class_="ys_post_content text"):
#	open("filename.csv","w").write(i)
	f.write(i)

for val in soup.find("p", class_="postInfo color-grey mt-5 fr"):
	print(val)
'''
f = open("1.txt", "a")
f.write(soup.title.string)
for i in soup.find("div", class_="fl mb-10"):
#        f = open("1.txt", "a")
        f.write(str(i))

for i in soup.find("div", class_="ys_post_content text"):
#	f = open("1.txt", "a")
	f.write(str(i))

	#print(i)

