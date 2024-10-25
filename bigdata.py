import urllib.request 
from bs4 import BeautifulSoup
import pandas as pd

shops = []

for page_num in range(1, 50):
    url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page_num}&sido=&gugun=&store="
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    tbody = soup.find("tbody")
    trs = tbody.find_all("tr")
    
    for tr in trs:
        tds = tr.find_all("td")
        shop_name = tds[1].text
        shop_addr = tds[3].text
        phone_num = tds[5].text
        shops.append([shop_name, shop_addr, phone_num])

hollys_df = pd.DataFrame(shops, columns=["매장명", "주소", "전화번호"])
hollys_df.to_csv("hollys.csv", index=False, encoding="utf-8")

print(hollys_df.head())