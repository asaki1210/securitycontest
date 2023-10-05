import requests
from bs4 import BeautifulSoup
url = 'https://scraping-for-beginner.herokuapp.com/ranking/'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
data = []
spots = soup.find_all('div',attrs={'class':'u_areaListRankingBox'})
# spot = spots[0]
# spot_name = spot.find('div',attrs = {'class':'u_title'})
# print(spot_name.text)


for spot in spots:
    spot_name = spot.find('div',attrs = {'class':'u_title'})
    spot_name.find('span',attrs = {'class':'badge'}).extract()
    spot_name = spot_name.text.replace('\n','')

    eval_num = spot.find('div',attrs = {'class':'u_rankBox'}).text
    eval_num = float(eval_num.replace('/n',''))

    categoryItems = spot.find('div',attrs = {'class':'u_categoryTipsItem'})
    categoryItems = categoryItems.find_all('dl')

    details = {}

    for categoryItem in categoryItems:
        category = categoryItem.dt.text
        rank = float(categoryItem.span.text)

        details[category] = rank

    datum = details
    datum['観光地名'] = spot_name
    datum['評価'] = eval_num
    data.append(datum)

import pandas as pd
df = pd.DataFrame(data)
df = df[['観光地名', '評価','楽しさ', '人混みの多さ', '景色', 'アクセス']]
print(df)
df.to_csv('観光地情報.csv', index=False)