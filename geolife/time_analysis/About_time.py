import sys 
sys.path.append("..")
from datetime import datetime
from data.load_database import *
import numpy as np
from distance import *

time_list = list()
diff_list = list()


def read_data_from_db():
	database = dbconn()
	cursor = database.cursor()
	sql = "SELECT lat,lon,time_s,time_l FROM gps where userid= 0"
	cursor.execute(sql)
	data = cursor.fetchall()
	print data
	return data


'''
Function: read_time_to_matrix

[[  39.98430324  116.30691753   12.            2.88333333]
 [  39.99058599  116.31282403   26.            4.13333333]
 [  40.00815346  116.32036573   38.            9.7       ]
 ..., 
 [  40.00461483  116.32234355    5.            2.88333333]
 [  39.98341191  116.32692183   48.            3.06666667]
 [  40.03493982  116.27468666  180.            4.73333333]]

'''
def read_time_to_matrix():
	data = read_data_from_db()
	data_mat = list()
	for datum in data:
		diff_time = (datum[3]-datum[2]).seconds/60
		diff_list.append(diff_time)
		hour = datum[2].hour + float(datum[2].minute)/60
		time_list.append(hour)
		data_mat.append([float(datum[0]),float(datum[1]),float(diff_time),float(hour)])    
		# print time_lsit.append(datum[2].time)
	data_mat = np.array(data_mat)
	# print type(data_mat)
	print data_mat
	return data_mat

def read_data_to_traffic_matrix():
	data = read_data_from_db()
	traffic_matrix =list()
	for index,datum in enumerate(data):
		if index == len(data) - 1 :
			break
		else :
			distance_ = calcDistance(float(datum[0]),float(datum[1]),
				float(data[index+1][0]),float(data[index+1][1]))
			time_ = (data[index+1][2]-datum[3]).seconds/60
			hour2 = data[index+1][2].hour + float(datum[2].minute)/60
			hour1 = datum[3].hour + float(datum[3].minute/60)
			traffic_matrix.append([distance_,time_,hour1,hour2])
	print traffic_matrix
	return traffic_matrix




def filter(data_mat):
	pass




def main():
	# read_time()
	# print time_list
	# print diff_list
	read_data_to_traffic_matrix()


if __name__ == '__main__':
	main()