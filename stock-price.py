import requests
import datetime
import math

time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def getStockInfo(symbol):
  url = 'https://mis.twse.com.tw/stock/api/getStockNames.jsp?'
  payload = {
    'n': str(symbol),
    '_': time
  }
  response = requests.get(url, params=payload)
  if response.status_code == 200:
    data = response.json()
    result = data['datas'][0]['key'][:4]
  return result

def getStockPrice(symbol):
  temp = getStockInfo(symbol)
  url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp'
  payload = {
    'ex_ch': temp + str(symbol) + '.tw',
    'json': '1',
    'delay': '0',
    '_': time
  }
  response = requests.get(url, params=payload)
  if response.status_code == 200:
    data = response.json()
    price = data['msgArray'][0]['pz']
  return price 

price = getStockPrice('0050')
print(price)