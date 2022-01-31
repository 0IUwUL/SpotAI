from dis import dis
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Spot_Clustering_Model import titles
from Spot_Clustering_Model import process
from Spot_Clustering_Model import names
import os
from dotenv import load_dotenv
from Profile_Link import username

#result of clustering
pas = titles()
finale = process()
tracks_names = names()
display = []
count = 0

for items in finale:
    display.append(items.sort_values(pas[count], ascending = False))
    count+=1

load_dotenv()

MY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
MY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
MY_CLIENT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

scope = 'playlist-modify-public'
#authentication for user
token = SpotifyOAuth(scope=scope, username = username, client_id = MY_CLIENT_ID, client_secret = MY_CLIENT_SECRET, redirect_uri = MY_CLIENT_URI)
spotifyObject = spotipy.Spotify(auth_manager = token)

for i in range(len(finale)-1, -1 ,-1):
#create playlist
    playlist_name = tracks_names[i].upper()
    spotifyObject.user_playlist_create(user=username, name = playlist_name, public = True, description="None")

Onelist = []
count = 0
n=len(finale)-1

for num in range(len(finale)-1, -1 ,-1):
    for song, row in display[num].iterrows():
        given = "spotify:track:"
        given+=row['track_id']
        Onelist.append(given)
        count+=1
        if count > 99:
            break
    preplaylist = spotifyObject.user_playlists(user=username)
    playlist = preplaylist['items'][n]['id']
    spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=Onelist)
    n-=1
    count = 0
    Onelist.clear()

print("Success")