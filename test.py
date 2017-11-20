import urllib2
from bs4 import BeautifulSoup

url = 'https://www.nextmuni.com/#!/sf-muni/29/29___I_F00/4838/6533'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
#name_box = soup.find('table', attrs={'id': 'values'})
