from sklearn.cluster import DBSCAN
import sys
sys.path.append("..")
from data.load_database import *
import numpy as np
import pprint
import matplotlib.pyplot as plt

def read_data_from_db():
	database = dbconn()
	cursor = database.cursor()
	sql = "SELECT lat,lon FROM gps LIMIT 0,257"	
	cursor.execute(sql)
	X = cursor.fetchall()
	X=np.array(X,np.float)
	return X 




def dbscan(X):
	db = DBSCAN(eps=0.15,min_samples=3).fit(X)
	# print db.labels_     zeros_like
	core_samples_mask = np.zeros_like(db.labels_)
	core_samples_mask[db.core_sample_indices_] = True
	lables = db.labels_
	n_clusters_ = len(set(lables)) -(1 if -1 in lables else 0)
	unique_lables = set(lables)
	cols = plt.cm.Spectral(np.linspace(0,1,len(unique_lables)))
	center_points = []
	for k,col in zip(unique_lables,cols):
		if k == -1:
			col = 'k'
		class_member_mask = (lables == k)
		k_x = X[class_member_mask & core_samples_mask]
		plt.plot(k_x[:,0],k_x[:,1],'o',markerfacecolor = col,
			markeredgecolor = 'k' , markersize = 5)
		center_points.append([np.mean(k_x[:,0]),np.mean(k_x[:,1])])
	plt.title('DBSCAN :Estimated number of clusters: %d' % n_clusters_)
	plt.show()


def main():
	X = read_data_from_db()
	dbscan(X)



if __name__ == '__main__':
	main()