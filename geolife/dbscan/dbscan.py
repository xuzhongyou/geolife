from sklearn.cluster import DBSCAN
import sys
sys.path.append("..")
from data.load_database import *
import numpy as np
import pprint
import matplotlib.pyplot as plt
import pickle
import json

def read_data_from_db(userid):
	database = dbconn()
	cursor = database.cursor()
	sql = "SELECT lat,lon FROM gps WHERE user_id = %d"%(userid)
	# sql = "SELECT lat,lon FROM gps LIMIT 0,257"	
	cursor.execute(sql)
	X = cursor.fetchall()
	X=np.array(X,np.float)
	return X

def read_time_from_db(LAT=0,LON=0,record_id=0):
	database = dbconn()
	cursor = database.cursor()
	sql = "SELECT time_s FROM gps WHERE record_id = %i"%(0)
	# sql = "SELECT time_s,time_l FROM gps WHERE lat = %s AND lon = %s"%(LAT,LON)
	cursor.execute(sql)
	data = cursor.fetchall()
	print data
	return data


out_user = dict()
center_points = list()
def dbscan(userid,X):

	db = DBSCAN(eps=0.15,min_samples=4).fit(X)
	# print db.labels_     zeros_like
	core_samples_mask = np.zeros_like(db.labels_,dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	lables = db.labels_ 
	labels_list = list(lables)
	# print labels_list.count(-1)
	out_user.setdefault(userid,0)
	out_user[userid] = labels_list.count(-1)
	print out_user

	# print labels_list.index(-1)
	print lables
	n_clusters_ = len(set(lables)) -(1 if -1 in lables else 0)
	unique_lables = set(lables)
	cols = plt.cm.Spectral(np.linspace(0,1,len(unique_lables)))
	# center_points = []
	for k,col in zip(unique_lables,cols):
		if k == -1:
			col = 'k'
		class_member_mask = (lables == k)
		k_x = X[class_member_mask & core_samples_mask]
		plt.plot(k_x[:,0],k_x[:,1],'o',markerfacecolor = col,
			markeredgecolor = 'k' , markersize = 5)
		center_points.append([np.mean(k_x[:,1]),np.mean(k_x[:,0])])
	plt.title('DBSCAN :Estimated number of clusters: %d' % n_clusters_)
	# plt.show()
	


def write_out_user(out_user):
	with open('out_user.txt','ab+') as f:
		pickle.dump(out_user,f)

# read file
def read_out_user():
	with  open('out_user.txt', 'rb') as f:
		obj_dict = pickle.load(f)
	print obj_dict
	return obj_dict 

def write_to_map(center_points):
	with open('clustering_points.js', 'w') as f:
		f.write('var data = {"data": %s}' % json.dumps(center_points))


def main():
	for userid in range(117):
		X = read_data_from_db(userid)
		dbscan(userid,X)
	write_to_map(center_points)
	print center_points
	# obj_dict = read_out_user()
	# write_out_user(out_user)  




if __name__ == '__main__':
	main()