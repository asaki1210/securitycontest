from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager

# headless処理(裏側で動いてくれる)
options = Options()
options.add_argument('--headless')

# ブラウザの起動
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()

# username imanisi  pass kohei (ログイン画面)
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)

# 場所取ってくる
elem_username = browser.find_element(By.ID, 'username')
elem_password = browser.find_element(By.ID, 'password')
elem_login_btn = browser.find_element(By.ID, 'login-btn')
# テキスト入力
elem_username.send_keys('imanishi')
elem_password.send_keys('kohei')
# ログインボタンクリック
elem_login_btn.click()

# thの値取得
elems_th = browser.find_elements(By.TAG_NAME,'th')
keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

# tdの値取得
elems_td = browser.find_elements(By.TAG_NAME,'td')
values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)

import pandas as pd
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values
print(df)

# 取得したデータをcsvファイルにする
df.to_csv('講師情報.csv',index=False)

import time
time.sleep(10)
browser.quit()