import flask
import os
import requests
import json
import random

app = flask.Flask(__name__)


@app.route('/')  
def index(): 
    return flask.render_template("index.html")
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)



url =  "https://api.genius.com/search"

my_headers = {
    "Authorization": "Bearer cG7siougj_ooBlmUJ7t6TMK0LLArlMM2DjXpUwzQ3uQf4gQ-vYTMlIVrHHhq9-Tc"
}



artist = "Frank Ocean"
song_title = "White Ferrari"
data = {'q': song_title + ' ' + artist}


response = requests.get(url, data=data, headers=my_headers)
json_body = response.json()



print(json.dumps(json_body, indent=2))