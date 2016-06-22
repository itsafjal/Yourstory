#! /usr/bin/python
import bleach
import re
import httplib2
import socket
from bs4 import BeautifulSoup, SoupStrainer
import requests
import urllib2
import csv
import socialshares

f = open("link3.txt", "r")
k = 0
#name = str(k)+".txt"
for links in f:
#	print(links[0], links[-2])
	if links[0]=="h" and links[-2]=="/":
		name = str(k)+".txt"
		url = links
#	print(url)
		try:

			page = urllib2.urlopen(url)
			soup = BeautifulSoup(page, 'html.parser')
			data = soup.title.string
			data = data.encode('utf-8').decode('ascii', 'ignore')
			print(data)
			authour = soup.find("a", attrs={"class":"aboutAuthor_name inline-block mr-5"})
			val = authour.text.split()
			s1 = str(val[0])
			s2 = str(val[1])
	 	        author = s1 + " " + s2
			sharecount = soup.find("p", attrs={"class":"postInfo color-grey mt-5 fr"})
			val1 = sharecount.text.split()
			date = str(val1[1])
			month = str(val1[2])
			year = str(val1[3])
			val3 = soup.find("div", attrs={'class':'ys_post_content text'})
			contents = bleach.clean(val3,tags=[],styles=[],strip=True)
			contents = contents.encode('utf-8').decode('ascii', 'ignore')




			counts = socialshares.fetch(links, ['facebook', 'linkedin'])
			facebook = counts['facebook']
			linkedin = counts['linkedin']



			with open('index3.csv', 'a') as csv_file:
			        writer = csv.writer(csv_file)
			        writer.writerow([date, month, year, author, data, facebook, linkedin,  contents])

		except:
			continue		
#	f = open(name, "a")
#	if soup.title.string:
#		print(soup.title.string)
#		f.write(soup.title.string)

#	for i in soup.find("div", class_="fl mb-10"):
#        f = open("1.txt", "a")
#		f.write(str(i))
#	for i in soup.find("div", class_="ys_post_content text"):
#       f = open("1.txt", "a")
#		f.write(str(i))
'''
	for data in soup.find("div", class_="ys_post_content text"):
		with open('link1.csv', 'a') as csv_file:  
			writer = csv.writer(csv_file)
			writer.writerow([data])
	data = soup.title.string
	with open('index.csv', 'a') as csv_file:
		writer = csv.writer(csv_file)
                writer.writerow([data])

'''
#	k = k + 1

