import requests
import datetime
import time

currentTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def getStockInfo(symbol):
  url = 'https://mis.twse.com.tw/stock/api/getStockNames.jsp?'
  payload = {
    'n': str(symbol),
    '_': currentTime
  }
  response = requests.get(url, params=payload)
  if response.status_code == 200:
    data = response.json()
    try:
      result = data['datas'][0]['key'][:4]
    except:
      result = 'Not Found'
  return result

def getStockPrice(symbol):
  temp = getStockInfo(symbol)
  if temp == 'Not Found':
    return 'Not Found'
  
  url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp'
  payload = {
    'ex_ch': temp + str(symbol) + '.tw',
    'json': '1',
    'delay': '0',
    '_': currentTime
  }
  time.sleep(5)
  response = requests.get(url, params=payload)
  if response.status_code == 200:
    data = response.json()
    try:
      price = data['msgArray'][0]['pz']
    except:
      price = 'Not Found'
  return price 