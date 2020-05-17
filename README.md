#### 安裝所需套件
`pip install -r requirements.txt`

#### 透過requests套件來實作功能
- requests.get(): 向網頁發送請求

#### 透過BeautifulSoup套件來實作功能
- BeautifulSoup(): 解析網頁

#### 透過sqlite3套件來實作功能
#### 資料庫

- 初始設定

  conn=sqlite3.connect(db_path): 連接資料庫

  cur=conn.cursor(): 建立Cursor物件

- cur.execute(): 執行 SQL 指令
- conn.commit(): 寫入資料庫
- cur.close(): 關閉資源
- conn.close(): 關閉連接
