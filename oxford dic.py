import requests
import json
from pprint import pprint as print

app_id = "29554b4f"
app_key = "41d2e7c74b2f75205d236f191a067bfb"
language = "en-gb"
word_id = "earth"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()


r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
#print(r.status_code)
res1 = r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

res2 = r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']

print(res2)
print(res1)