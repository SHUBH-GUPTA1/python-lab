# import requests
# res=requests.get('https://ipinfo.io/')
# data=res.json()
# citydata=data['city']
# print(citydata)
# url='https://wttr.in/{}'.format(citydata)
# res=requests.get(url)
# print(res.text)


import requests

res=requests.get('https://ipinfo.io/')
data=res.json()
citydata=data['city']
print(citydata)
url='https://wttr.in/{}'.format(citydata)
res=requests.get(url)
print(res.text)
