import sys
sys.path.append("..")
import matplotlib.pyplot as plt
from data.load_database import *
import pprint
import numpy as np
from sklearn.cluster import DBSCAN



def read_from_db():
	x = list()
	database = dbconn()
	cursor = database.cursor()
	sql = 'SELECT * FROM gps LIMIT 0,257 '
	cursor.execute(sql)
	data = cursor.fetchall() 
	for datum in data:
		# print datum
		x.append(datum[2:4])
		# print x
	return x

def change_to_matrix():
	x = list()
	x = read_from_db()
	x = np.array(x, np.float)
	return x


#start dbscan
def compute_dbscan():
	x = change_to_matrix()
	print x
	db = DBSCAN(eps=0.15, min_samples=4).fit(x)
	#get the result matrix:everypoint belongs which cluster
	print db.labels_
	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	#core_sample_indices is core point
	core_samples_mask[db.core_sample_indices_] = True
	labels = db.labels_

	# Number of clusters in labels, ignoring noise if present.
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
	##############################################################################
	# Plot result


	# Black removed and is used for noise instead.
	unique_labels = set(labels)
	print unique_labels
	return 
	colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
	fig = plt.figure(2)
	centerPoint = []
	for k, col in zip(unique_labels, colors):
		if k == -1:
			# Black used for noise.
			col = 'k'
	#        continue

		class_member_mask = (labels == k)

		xy = X[class_member_mask & core_samples_mask]
		
		#centerPoint.append()

		print "%d reference points contain %d points" %(k,len(xy))
		#print "%f mean pos %f" %xy.
		plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
				 markeredgecolor='k', markersize=14)
		print "center pos %f %f" %(np.mean(xy[:, 0]), np.mean(xy[:, 1]) ) 
	'''
		xy = X[class_member_mask & ~core_samples_mask]
		plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
				 markeredgecolor='k', markersize=6)
				 '''

	plt.title('DBSCAN :Estimated number of clusters: %d' % n_clusters_)



	# Plot the ground truth
	#fig = plt.figure(2, figsize=(4, 3))

	plt.show()
	print "successful"




def main():
	# x = change_to_matrix()
	compute_dbscan()

if __name__ == '__main__':
	main()