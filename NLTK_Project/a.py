import urllib.request
from bs4 import BeautifulSoup
response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup=BeautifulSoup(html)
text=soup.get_text(strip=True)
print(text)

