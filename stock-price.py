import requests
import datetime
import math
# 上櫃 https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=otc_5508.tw&json=1&delay=0&_=1771661295326&lang=zh_tw
# 上市 https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0050.tw&json=1&delay=0&_=1771658259143&lang=zh_tw

def getStockPrice(symbol):
  time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
  
  url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp'
  payload = {
    'ex_ch': 'tse_' + str(symbol) + '.tw',
    'json': '1',
    'delay': '0',
    '_': time
  }
  response = requests.get(url, params=payload)
  if response.status_code == 200:
    data = response.json()
    return data['msgArray'][0]['pz']

price = getStockPrice('0050')
print(price)