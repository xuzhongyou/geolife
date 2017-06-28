# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:50:44 2017

@author: xuzhongyou
"""
import MySQLdb
from datetime import * 

def dbconn():
    return MySQLdb.connect(host='127.0.0.1',
                          	 db='geolife',
                           user='root',
                         passwd='1234',
                           port=3306)

def load_into_db(filedir):
	f = open(filedir).readlines()
	temp_list = list()
	for index,line in enumerate(f):
		data = line.strip().split(',')
		# print data 
		a = map(int,data[3].split('-'))
		b = map(int,data[4].split(':'))
		c = map(int,data[5].split('-'))
		d = map(int,data[6].split(':'))
		time_s = datetime(a[0],a[1],a[2],b[0],b[1],b[2]) 
		time_l = datetime(c[0],c[1],c[2],d[0],d[1],d[2])
		#print time_s,time_l
		newdata = [data[0],data[1],data[2],time_s,time_l]
		# print newdata
		temp_list.append(newdata)
		if len(temp_list) > 0 :
			try:
				insert_into_db(temp_list)
				print "Having inserted {0}".format(index)
				temp_list = list()
			except Exception,e:
				print index,e



def insert_into_db(temp_list):
		database = dbconn()
		cursor = database.cursor()
		for datum in temp_list:
			cursor.execute('INSERT INTO gps VALUES (NULL,\'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\')'.format(
								datum[0].encode('UTF-8'),
								datum[1].encode('UTF-8'),
								datum[2].encode('UTF-8'),
								datum[3],
								datum[4]
								)
							)
			database.commit()
		cursor.close()
		database.close()

def import_test():
	print 'import successfully'

# def main():
# 	filedir = 'Preclusterdata2.0.txt'
# 	load_into_db(filedir)

# if __name__ == '__main__':
# 	main()