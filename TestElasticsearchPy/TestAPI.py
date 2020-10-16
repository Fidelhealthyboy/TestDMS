import requests

url = " http://127.0.0.1:5000/search/index1/match_all"

r = requests.get(url=url)
print(r.text)
