# coding: utf8
from __future__ import division
from sklearn import preprocessing
import numpy as np
from np import array

#https://migege.com/post/matrix-multiplication-in-numpy
s2 = [
        [0.512,0.309,0.111,0.054,0.014],
        [0.318,0.527,0.120,0.025,0.011],
        [0.361,0.473,0.093,0.064,0.0101],
        [0.393,0.479,0.113,0.014,0.002]
    ]

w2 = [0.3845,0.3845,0.1433,0.0878]

#list to array
arrs2 = np.array(s2)
arrw2 = np.array(w2)

#矩阵乘法:等价于矩阵arrs2 * arrw2
#模糊综合评价向量
y2 = arrs2.dot(arrw2)

#S:模糊矩阵	list
#W:权重向量集 list
#return list
def SW(S,W):
	#list to array
	arrs2 = np.array(s2)
	arrw2 = np.array(w2)
	#矩阵乘法:等价于矩阵arrs2 * arrw2
	#模糊综合评价向量
	return arrs2.dot(arrw2)