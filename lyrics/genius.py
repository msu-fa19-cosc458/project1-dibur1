import requests 
import json

url =  "https://api.genius.com/search?q=Kendrick%20Lamar"
my_headers = {
    "Authorization": "Bearer 991_Rh5jkm6T5y3TDdifsit8mqBLmTwQAGdCgjSd_u7WWab1xa5E8o3h1DNITSRU"
}

response = requests.get(url, headers=my_headers)
json_body = response.json()
print(json_body["response"]["hits"][0]["type"])