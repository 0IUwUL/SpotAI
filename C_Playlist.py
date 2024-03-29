import os
from tkinter.constants import NONE
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re
from Spot_Clustering_Model import finale
from Spot_Clustering_Model import pas

display = []
count = 0
for items in finale:
    display.append(items.sort_values(pas[count], ascending = False))
    count+=1


load_dotenv()

MY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
MY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
MY_CLIENT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

#reason for app
scope = 'playlist-modify-public'
#username for user


try:
    username = input('Input link from your Spotify profile: ')
    username = re.split('/|\?', username)
    username = username[4]
except:
    print("Please input link from your Spotify link")
    username = input('Input link from your Spotify profile: ')
    username = re.split('/|\?', username)
    username = username[4]


#authentication for user
token = SpotifyOAuth(scope=scope, username = username, client_id = MY_CLIENT_ID, client_secret = MY_CLIENT_SECRET, redirect_uri = MY_CLIENT_URI)
spotifyObject = spotipy.Spotify(auth_manager = token)

for i in pas:
#create playlist
    playlist_name = i.upper()
    spotifyObject.user_playlist_create(user=username, name = playlist_name, public = True, description="None")

Onelist = []
count = 0

for song, row in display[2].iterrows():
    given = "spotify:track:"
    given+=row['track_id']
    Onelist.append(given)
    count+=1
    if count > 99:
        break
preplaylist = spotifyObject.user_playlists(user=username)
playlist = preplaylist['items'][2]['id']
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=Onelist)

Twolist = []
count = 0

for song, row in display[1].iterrows():
    given = "spotify:track:"
    given+=row['track_id']
    Twolist.append(given)
    count+=1
    if count > 99:
        break
preplaylist = spotifyObject.user_playlists(user=username)
playlist = preplaylist['items'][1]['id']
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=Twolist)

Threelist = []
count = 0

for song, row in display[0].iterrows():
    given = "spotify:track:"
    given+=row['track_id']
    Threelist.append(given)
    count+=1
    if count > 99:
        break
preplaylist = spotifyObject.user_playlists(user=username)
playlist = preplaylist['items'][0]['id']
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=Threelist)

