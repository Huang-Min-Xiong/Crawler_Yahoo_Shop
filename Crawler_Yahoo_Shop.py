import requests
import sqlite3
from bs4 import BeautifulSoup

url = 'https://tw.buy.yahoo.com/search/product?p=RAM' #Yahoo購物中心網址
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')


db_path=r'.\Crawler_Yahoo_Shop_DB.db' #資料庫路徑
conn = sqlite3.connect(db_path) #連接資料庫
cur = conn.cursor()


for data in soup.find_all(class_='BaseGridItem__grid___2wuJ7 BaseGridItem__multipleImage___37M7b'):
    #將其資訊拆開
    Data = list(data.stripped_strings) #去除多餘空白內容

    #不是補貨中的資料才印出
    if '補貨中' not in Data:
        #顯示資訊
        print(Data)
        #執行SQL指令
        cur.execute("insert into Yahoo_Shop_DB values('{}','{}')" .format(Data[0],Data[1]))
        #傳送數據
        conn.commit()
        
print('已寫入資料庫!')

cur.close() #關閉資源
conn.close() #關閉連接

