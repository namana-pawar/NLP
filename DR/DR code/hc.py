# Hierarchical Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
df1 = pd.read_csv('experience.csv')
df2 = pd.read_csv('interval.csv')
df3 = pd.read_csv('frequency.csv')
df_combined = df1.merge(df2, how='outer', on=['index','Project']).merge(df3, how='outer', on=['index','Project'])
df_combined=df_combined[['index','Project','Experience','Interval','Frequency']]
df_combined.rename(columns={'index':'ID'})
df_combined=df_combined.dropna(axis=0, how='any')

print(df_combined.isnull())
print(df_combined.head(5))

X = df_combined.iloc[:, [2, 3]].values

from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
X[:,0]=label.fit_transform(X[:,0])



# Using the dendrogram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Programmers')
plt.ylabel('Euclidean distances')
plt.show()

# Fitting Hierarchical Clustering to the dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)


# Visualising the clusters
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.title('Clusters of programmers')
plt.xlabel('Experience')
plt.ylabel('Interval')
plt.legend()
plt.show()