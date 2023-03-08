from sklearn.cluster import DBSCAN

X_train = df[['exercise','lifespan']]

model = DBSCAN()
model.fit(X_train)

cluster_labels = model.labels_
plt.scatter(df["exercise"], df["lifespan"], c = cluster_labels)
plt.show()

df['labels'] = cluster_labels

df_cluster_clean = df[df['labels'] != -1]