#!/usr/bin/env python3

import requests 
r = requests.get('http://web.physics.ucsb.edu/~phys129/lipman/')

r.content
r.encoding
r.text
#print(r.text)
#print(type(r.text))

html_doc = r.text #html website code 

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser') #parses the code

#print(soup)

import re

a = soup.find_all('p')[0].get_text() #finds code lines that start with letter p.
								     #displays as a list.
#print(a)

b = a.split() 
# splits each string into a seperate list element.

print('\nThe Physics 125 webpage announcements were last updated on:\n',b[3],b[4],b[5])

#prints the wanted message. Extracted list elements in print statement.




