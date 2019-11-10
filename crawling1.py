import requests
from bs4  import BeautifulSoup
from bs4 import NavigableString



url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&amp;theatercode=0013&amp;date=20190928"
html = requests.get(url)
# print(html.text)
soup = BeautifulSoup(html.text,'html.parser')
title_list = soup.select('div.info-movie')

for i in title_list:
    print(i.select_one("a > strong").text.strip())

