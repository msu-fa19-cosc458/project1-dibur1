import requests_oauthlib
import requests
url = "https://api.genius.com/search?q=Kendrick%20Lamar"

oauth = requests_oauthlib.OAuth1(
    "<API_KEY>", 
    "<API_SECRET>",
    "<ACCESS_TOKEN>",
    "<ACCESS_TOKEN_SECRET>"
)

response = requests.get(url, auth=oauth)

print(response.json())
