
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from sklearn import preprocessing
from itertools import permutations
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import Playlist


print("Get Playlist")

print("=============================================================")
print("                         PLEASE WAIT                            ")
print("=============================================================")


load_dotenv()

MY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
MY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
MY_CLIENT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

client_credentials_manager = SpotifyClientCredentials(client_id=MY_CLIENT_ID, client_secret=MY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#get user playlist
playlist_id = 'spotify:user:spotifycharts:playlist:'+Playlist.link
#print(playlist_id)
results = sp.playlist(playlist_id)
#getting song in playlist
track_song = []

#while results['tracks']['items'][j]['track']['uri'] != NULL:
#    track_song = results['tracks']['items'][j]['track']['uri']
#    j+=1

#listing songs from user's playlist to list
for x in results['tracks']['items']:
    track_song.append(x['track']['uri'])

features = sp.audio_features(track_song)
#print(track_song)
#print(len(track_song))
#print('This is features')
#print(features)

songs_and_features = {}

for a in range(len(track_song)):
    songs_and_features[a] = features[a]


#print(songs_and_features)

#songs from playlist given
df = pd.DataFrame.from_dict(songs_and_features, orient ='index')
df.drop(df.columns[[11, 13, 14, 15, 17]], axis = 1, inplace = True)
df.drop_duplicates(subset=['id'])

df.to_csv('Data/Playlist.csv', index=False)

df = pd.read_csv('Data/Playlist.csv')

columns = ["energy", "key", "speechiness", "acousticness", "instrumentalness", "loudness","tempo","danceability", 'valence' , "liveness"]

df = df[columns]

perm = permutations(columns, 3)
output = set(map(lambda x: tuple(sorted(x)),perm))
a=[]
column_names = ["features", "score", "elbow"]
df3 = pd.DataFrame(columns = column_names)

for i in list(output):
    df1 = df[[i[0], i[1], i[2]]]
    x = df1.values  # returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)

    model = KMeans(random_state=0)
    visualizer = KElbowVisualizer(model, k=(2,12), metric='silhouette', timings=False)
    visualizer.fit(x_scaled)
    score = visualizer.elbow_score_
    value = visualizer.elbow_value_
    if score>0.4:
        # visualizer.show()
        idx = df1.columns
        mylist = idx.tolist()
        dict = {
            "features": mylist,
            "score": score,
            "elbow": value
        }
        df3 = df3.append(dict, ignore_index=True)

df3.to_csv('Data/elbow_clusters.csv', index=False)

get_features = pd.read_csv('Data/elbow_clusters.csv')
sorted_df = get_features.sort_values(["score"], ascending=False)
sorted_df.reset_index(inplace=True)

#print(sorted_df)

pass_feat = []

pass_feat = sorted_df.features[0]
pass_feat = list(pass_feat.split(","))

#removing extra characters in features pulled
for x in range(len(pass_feat)):
    pass_feat[x] = pass_feat[x].replace("[", "")
    pass_feat[x] = pass_feat[x].replace("'", "")
    pass_feat[x] = pass_feat[x].replace("]", "")
    pass_feat[x] = pass_feat[x].replace(" ", "")

clusters = sorted_df.elbow[0]

#print(clusters)


