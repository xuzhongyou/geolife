import sys 
sys.path.append("..")
from datetime import datetime
from data.load_database import *
import numpy as np


time_list = list()
diff_list = list()
def read_time():
	database = dbconn()
	cursor = database.cursor()
	sql = "SELECT lat,lon,time_s,time_l FROM gps where userid= 0"
	cursor.execute(sql)
	data = cursor.fetchall()
	# print type(data[0][3])
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

def cal

def filter(data_mat):
	pass




def main():
	read_time()
	print time_list
	print diff_list


if __name__ == '__main__':
	main()