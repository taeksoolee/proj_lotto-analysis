from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url)

win_result = driver.find_elements(By.CLASS_NAME, 'win_result')
lrgs = win_result[0].find_elements(By.CLASS_NAME, 'lrg')

# 당첨번호를 순서대로 출력한다.
for lrg in lrgs:
  print(lrg.text)

driver.close();
driver.quit();
