
from webbrowser import Chrome
from selenium import webdriver
from seleniumrequests import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import csv

from bs4 import BeautifulSoup as bs

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument("disable-gpu")
# options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")

# which chromedriver => /usr/sbin/chromedriver
# chrome = Chrome('./chromedriver', chrome_options=options)

def getNumberList(session, year):
  data = dict()
  data['drwNo'] = year
  response = session.request('POST', 'https://dhlottery.co.kr/gameResult.do?method=byWin', data=data);

  html = bs(response.text, 'html.parser')
  win_result = html.find('div', {'class': 'win_result'})
  lrgs = win_result.find_all('span', {'class': 'lrg'})

  return list(map((lambda x: x.text), lrgs))

def getNumberStr(session, year):
  return ','.join(getNumberList(session, year))


chrome = Chrome(service=Service(ChromeDriverManager().install()), options=options)

# results = dict()
# for number in list(map((lambda x: x+1), range(30))):
  # results[str(number)] = getNumberStr(chrome, number)
# print(results)

with open('lotto_data.csv', 'w') as f:
  fieldnames = ['no', '1', '2', '3', '4', '5', 'bonus']
  writer = csv.DictWriter(f, fieldnames=fieldnames)
  writer.writeheader()
  
  for number in list(map((lambda x: x+1), range(30))):
    row_data_list = getNumberList(chrome, number)
    row_data = {
      'no': str(number),
      '1': row_data_list[0],
      '2': row_data_list[1],
      '3': row_data_list[2],
      '4': row_data_list[3],
      '5': row_data_list[4],
      'bonus': row_data_list[5]
    }
    writer.writerow(row_data)

chrome.quit()

