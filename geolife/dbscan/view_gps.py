import sys
sys.path.append("..")
import matplotlib.pyplot as plt
from data.load_database import *
import pprint
import numpy as np



def show_view():
	x = list()
	x = read_from_db()
	x = np.array(x, np.float)
	print x
	plt.plot(x[:, 0], x[:, 1], '*', markerfacecolor='k',
		markeredgecolor='k', markersize=10)
	plt.show()


def read_from_db():
	x = list()
	database = dbconn()
	cursor = database.cursor()
	sql = 'SELECT * FROM gps LIMIT 0,100 '
	cursor.execute(sql)
	data = cursor.fetchall() 
	for datum in data:
		# print datum
		x.append(datum[2:4])
		# print x
	return x



def main():
	show_view()




if __name__ == '__main__':
	main()