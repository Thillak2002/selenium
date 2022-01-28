import urllib
import  urllib.request
from bs4 import  BeautifulSoup

url ="https://twitter.com/sachin_rt"
page=urllib.request.urlopen(url)
soup= BeautifulSoup(page,"html.parser").text

s=soup.find("div[class='css-1dbjc4n r-6gpygo r-14gqq1x']>div>div>div>div>span>span")
print(s)

