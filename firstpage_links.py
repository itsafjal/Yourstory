from bs4 import BeautifulSoup
import urllib2
'''
url = 'http://yourstory.com/'
data = urllib2.urlopen(url).read()
f = open("first_links.txt", "a")
page = BeautifulSoup(data,'html.parser')

for link in page.findAll('a'):
       l = link.get('href')
       if "http://yourstory.com/2016/05/" in l:
		f.write(l)
		f.write("\n")

'''
f = open("all_links.txt", "a")
for i in range(46,100):
	url = 'http://yourstory.com/page/'+str(i)+'/'

	print(url)
	data = urllib2.urlopen(url).read()
#	f = open("all_links.txt", "a")
	page = BeautifulSoup(data,'html.parser')
#	print(page)
	for link in page.findAll('a'):
		l = link.get('href')
		if "http://yourstory.com/2015/" in l:
	#		print(l)
			f.write(l)
			f.write("\n")
         
