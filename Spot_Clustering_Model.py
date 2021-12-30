import pandas as pd 
import numpy as np 
#import matplotlib.pyplot as plt
#plt.style.use("seaborn")
#from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from Land import att

print (att)
df = pd.read_csv('Data/Track.csv')
df = df[['track_name','artist_name','danceability','energy','key','loudness','acousticness','valence']]

#fig,axes = plt.subplots(2,2,figsize=(15,8))

#axes[0,0].hist(df['key'])
#axes[0,0].set_title('Key',fontsize=15)
#axes[0,1].hist(df['energy'])
#axes[0,1].set_title('Energy',fontsize=15)
#axes[1,0].hist(df['acousticness'])
#axes[1,0].set_title('Acousticness',fontsize=15)

#plt.show()

col_features = df.columns[3:]
X = MinMaxScaler().fit_transform(df[col_features])
kmeans = KMeans(init="k-means++", n_clusters=5, random_state=15).fit(X)

df['kmeans'] = kmeans.labels_

#fig = plt.figure(figsize=(10,8))
#ax = fig.add_subplot(111,projection='3d')

#x = df['energy']
#y = df['key']
#z = df['acousticness']
#cmhot = cmhot = plt.get_cmap('bwr')

#ax.scatter(x,y,z,c=df['kmeans'],s=40,cmap=cmhot)
#ax.set_xlabel('energy',fontsize=12)
#ax.set_ylabel('key',fontsize=12)
#ax.set_zlabel('acousticness',fontsize=12)

#ax.set_title("3D Scatter Plot of Songs Clustered")
#plt.show()

print(df.groupby(['kmeans']).mean())

cluster_0 = df[df['kmeans']==0]
cluster_1  = df[df['kmeans']==1]
cluster_2 = df[df['kmeans']==2]
cluster_3  = df[df['kmeans']==3]
cluster_4 = df[df['kmeans']==4]

cluster_0.to_csv("data/cluster0.csv",index=False)
cluster_1.to_csv("data/cluster1.csv",index=False)
cluster_2.to_csv("data/cluster2.csv",index=False)
cluster_3.to_csv("data/cluster3.csv",index=False)
cluster_4.to_csv("data/cluster4.csv",index=False)
df.to_csv("data/df.csv",index=False)