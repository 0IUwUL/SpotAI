from sklearn import preprocessing
from itertools import permutations
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import pandas as pd

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
    #implements the “elbow” method
    visualizer = KElbowVisualizer(model, k=(2,12), metric='silhouette', timings=False)
    visualizer.fit(x_scaled)
    score = visualizer.elbow_score_
    value = visualizer.elbow_value_
    idx = df1.columns
    mylist = idx.tolist()
    dict = {
        "features": mylist,
        "score": score,
        "elbow": value
    }
    df3 = df3.append(dict, ignore_index=True)

sorted_df = df3.sort_values(["score"])
sorted_df.reset_index(inplace=True)
print(sorted_df)
#getting mean of score column
basis = sorted_df['score'].mean()
column_names = ["features", "score", "elbow"]
pass_feat = pd.DataFrame(columns = column_names)

for i in range(len(df3["score"])):
    if df3.iloc[i]['score'] > basis:
        dict = {
            "features": df3.iloc[i]['features'],
            "score": df3.iloc[i]['score'],
            "elbow": df3.iloc[i]['elbow'],
        }
        pass_feat = pass_feat.append(dict, ignore_index=True)
pass_feat.to_csv('Data/elbow_clusters.csv', index=False)