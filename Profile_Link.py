from tkinter import *

from matplotlib.style import use
from Spot_Clustering_Model import *
from tkinter import messagebox
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re


def btn_clicked():
    username = re.findall(r"[\w']+", entry0.get())
    print(username)
    username=username[5]
    print(username)
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

    for i in tracks_names:
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
    print("success")

window = Tk()

Uinput = StringVar()

window.geometry("1280x720")
window.configure(bg = "#191414")
canvas = Canvas(
    window,
    bg = "#191414",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(master=window, file = f"./assets/Profbackground.png")
background = canvas.create_image(
    639.0, 360.0,
    image=background_img)

entry0_img = PhotoImage(master=window, file = f"./assets/Prof_textBox0.png")
entry0_bg = canvas.create_image(
    588.0, 541.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#938888",
    highlightthickness = 0,
    master=window,)

entry0.place(
    x = 196.0, y = 519,
    width = 784.0,
    height = 43)

img1 = PhotoImage(master=window, file = f"./assets/Profimg1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : btn_clicked(),
    relief = "flat",
    master=window)

b1.place(
    x = 999, y = 519,
    width = 92,
    height = 45)




window.resizable(False, False)
window.mainloop()
