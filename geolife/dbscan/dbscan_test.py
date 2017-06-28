#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
'''
%matplotlib inline
将matplotlib的图表直接嵌入到Notebook之中
'''
#二分类的线性可分数据集
#factor 为内圈和外圈的尺寸因子<1,生成环形数据。
#x为生成样本数据集，y为数据集的标签
X1, y1=datasets.make_circles(n_samples=5000, factor=.6,
                                      noise=.05)
#n_samples为待生成的样本总数
#n_features每个样本的特征数
#centers生成样本的中心
#cluster_std为类别的方差
X2, y2 = datasets.make_blobs(n_samples=1000, n_features=2, centers=[[1.2,1.2]], cluster_std=[[.1]],
               random_state=9)

X = np.concatenate((X1, X2))

'''
this is a test
plt.scatter(X[:, 0], X[:, 1],c='r', marker='o')
plt.show()
'''


'''
This is KMeans
y_pred = KMeans(n_clusters=3, random_state=9).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
'''


'''
这样的分类的效果并不好
y_pred = DBSCAN(eps = 0.1).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
'''

y_pred = DBSCAN(eps = 0.1, min_samples = 10).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()