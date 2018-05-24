from bs4 import*
import requests
url="https://www.accuweather.com/en/us/san-jose-ca/95110/weather-forecast/347630"
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
data=requests.get(url,headers=headers)
soup=BeautifulSoup(data.text,"html.parser")
soup.find('div',{'class':'info'})
data2 = soup.find('div',{'class':'info'})
data3 = data2.find('span',{'class':'large-temp'})
print(data3.contents[0])