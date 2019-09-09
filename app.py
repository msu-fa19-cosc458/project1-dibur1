#app.py
import flask
import os
import requests
import json
import random
import tweepy



import tweepy






url =  "https://api.genius.com/search?q=Frank%20Ocean"

my_headers = {"Authorization": "Bearer cG7siougj_ooBlmUJ7t6TMK0LLArlMM2DjXpUwzQ3uQf4gQ-vYTMlIVrHHhq9-Tc"}

#Twitter 
auth = tweepy.OAuthHandler('8U7ALxzOzjurDtW5b8cAgaU71', '9fXwrB2bDnQ67GPSvvbKny1NKV8QuQHq24E4UiDvXIP01Ic3AS')
auth.set_access_token('902294288465264645-dFfNxOQnUcJB9HLwAH9udhAcliXpOfZ', 'dJUISUFOkYCriYxto90p6BRMAp2ehshTU5yzNJjAvnkig')

api = tweepy.API(auth)




#'8U7ALxzOzjurDtW5b8cAgaU71'
#'9fXwrB2bDnQ67GPSvvbKny1NKV8QuQHq24E4UiDvXIP01Ic3AS'
#'902294288465264645-dFfNxOQnUcJB9HLwAH9udhAcliXpOfZ'
#'dJUISUFOkYCriYxto90p6BRMAp2ehshTU5yzNJjAvnkig'


#Functions
def get_info():
    
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    i = random.randint(0, len(json_body['response']['hits'])-1)
    return json_body['response']['hits'][i]

    
json_obj = get_info()



def get_artist(json_obj):
    return json_obj['result']['primary_artist']['name']
    
    
def get_artistimg(json_obj):
    return json_obj['result']['header_image_thumbnail_url']
    
def get_songimg(json_obj):
    return json_obj['result']['song_art_image_thumbnail_url']


def get_link(json_obj):
    return json_obj['result']['url']

def get_songname(json_obj):
    return json_obj['result']['title_with_featured']


def get_tweets():
    list = []
    public_tweets = api.search("peace")
    for r in range(10):
        for tweet in public_tweets:
         list.append(tweet.text)
    return list
    



    


    
app = flask.Flask(__name__)



@app.route('/')  
def index(): 
    artist_json = get_info()
    print(json.dumps(artist_json, indent=2))
    a = get_songname(artist_json)
    b = get_artist(artist_json)
    c = get_artistimg(artist_json)
    d = get_songimg(artist_json)
    e = get_link(artist_json)
    f = get_tweets()
    return flask.render_template("index.html", song1 = a, artist1 = b, frank1 = c, frank2 = d, link1 = e, tweet = f)
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True)
