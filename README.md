# 104_ETL
"""
利用requests beautifulsoup os等套件 將從104爬取的職缺整理成文字檔存取至本地端

1.爬蟲起手式 import所需套件並帶入UserAgent headers的資訊

2.觀察輸入搜尋後的Url:"https://www.104.com.tw/jobs/search/?ro=0&keyword=React" 可發現"keyword"的值是代表搜尋的關鍵字

3.利用requests.get該職缺第一頁 再用Beautifulsoup整理html的文本 可爬取第一頁出現的職缺資訊

4.如需爬取更多資訊 須帶入動態網頁所需的dataform
datastr="""ro: 0
kwop: 11
keyword: React
expansionType: job
order: 14
asc: 0
page: 1      <<<<<      網頁下拉時page的值會依序加1
mode: s
langFlag: 0"""

5.完整的工作內容資訊 要分別找到職缺的一串六位數代碼 帶到這串網址後面'https://www.104.com.tw/job/ajax/content/{0123456}'
"""
