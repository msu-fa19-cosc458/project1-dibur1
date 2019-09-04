import requests
import json

url =  "https://api.genius.com"
my_headers = {
    "Authorization": "Bearer cG7siougj_ooBlmUJ7t6TMK0LLArlMM2DjXpUwzQ3uQf4gQ-vYTMlIVrHHhq9-Tc"
}


search_api = url + "/search"
artist = "Frank Ocean"
song_title = "Self Control"
data = {'q': song_title + ' ' + artist}


response = requests.get(search_api, data=data, headers=my_headers)
json_body = response.json()

print(json_body["response"]["hits"][0]["type"])
print (response.text )