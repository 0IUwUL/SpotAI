import os
from tkinter.constants import NONE
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import re

load_dotenv()

MY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
MY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
MY_CLIENT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

try:
    username = input('Input link from your Spotify profile: ')
    username = re.split('/|\?', username)
    username = username[4]
except:
    print("Please input link from your Spotify link")
    username = input('Input link from your Spotify profile: ')
    username = re.split('/|\?', username)
    username = username[4]

scope = 'playlist-modify-public'