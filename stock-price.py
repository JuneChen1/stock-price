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
    price = 'Not Found'
    name = 'Not Found'
    return price, name
  
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
      price = data['msgArray'][0]['z']
      if price == '-':
        price = data['msgArray'][0]['a'].split('_')[0]
    except:
      price = 'Not Found'

    try:
      name = data['msgArray'][0]['n']
    except:
      name = 'Not Found'

  return price, name

symbol = input('股票代號：')
price, name = getStockPrice(symbol)

print('股票名稱：', name, sep='')
if price == 'Not Found':
  print('股價：', price, sep='')
else:
  print('股價：', f"{float(price):.2f}", sep='')