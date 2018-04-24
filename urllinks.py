"""

Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a 
Python program similar to http://www.py4e.com/code3/urllink2.py. The program will 
use urllib to read the HTML from the data files below, and parse the data, extracting 
numbers and compute the sum of the numbers in the file.

"""


# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_85335.html'  
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
sum=0
for tag in tags:
    sum+=int(tag.contents[0])

print ('sum: ', sum)
