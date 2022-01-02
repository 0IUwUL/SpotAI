import pandas as pd 
import numpy as np
from sklearn import cluster 
#import matplotlib.pyplot as plt
#plt.style.use("seaborn")
#from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from Land import att

df = pd.read_csv('Data/Track.csv')
initial = ['track_id','track_name','artist_name']
pas = []
for i in att:
    if bool(att[i]):
        pas.append(i.lower())

initial += pas

df = df[initial]

#print(att)
#print(df)

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
#grouped clusters
cluster_0 = df[df['kmeans']==0]
cluster_1  = df[df['kmeans']==1]
cluster_2 = df[df['kmeans']==2]
cluster_3  = df[df['kmeans']==3]
cluster_4 = df[df['kmeans']==4]

clusters = [cluster_0, cluster_1, cluster_2, cluster_3, cluster_4]

#getting means per column per clusters
hold = {}
hold[0] = cluster_0[pas].mean()
hold[1] = cluster_1[pas].mean()
hold[2] = cluster_2[pas].mean()
hold[3] = cluster_3[pas].mean()
hold[4] = cluster_4[pas].mean()

#setting compare vars
Largest_0 = 0
Largest_1 = 0
Largest_2 = 0

final = {}

#getting index from cluster with highets per attribute
for i in hold:
    if float(hold[i][pas[0]])> Largest_0:
        Largest_0 = float(hold[i][pas[0]])
        final[0] = i
    if float(hold[i][pas[1]]) > Largest_1:
        Largest_1 = float(hold[i][pas[1]])
        final[1] = i
    if float(hold[i][pas[2]]) > Largest_2:
        Largest_2 = float(hold[i][pas[2]])
        final[2] = i
#print(final)
df.to_csv("Data/df.csv")
clusters[final[0]].to_csv("Data/1st.csv")
clusters[final[1]].to_csv("Data/2nd.csv")
clusters[final[2]].to_csv("Data/3rd.csv")

finale = []

for i in final:
    finale.append(clusters[final[i]])