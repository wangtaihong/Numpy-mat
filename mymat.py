# coding: utf8
from __future__ import division
from sklearn import preprocessing
import numpy
from numpy import array

#矩阵按列归一化
#X_list:list
#return NParr
def normalizedByCol(X_list):
	X = numpy.array(X_list)
	#阵列n * m
	lw = X.shape
	#矩阵的大小
	# L=X.size
	#矩阵切片，切第一列:
	# slc = X[:, 0:1]
	mul,tempSUM = [],0
	if (len(lw))==1:
		tempsum = 0
		for x in X:
			tempsum += x
		for x in X:
			mul.append(x/tempsum)
		return mul
	for x in xrange(0,lw[0]):
		mul.append([])
	for j in xrange(0,lw[1]):
		temp_ = X[:, j:j+1]
		for tem in temp_:
			tempSUM +=tem[0]
		i = 0
		for te in temp_:
			div = te[0]/tempSUM
			mul[i].append(div)
			i = i+1
		tempSUM=0
	return mul

#矩阵按行相加
#matList
#return list
def matSumRow(matList):
	NParr = numpy.array(matList)
	lw = NParr.shape
	rowSum = []
	for x in xrange(0,lw[0]):
		temp = NParr[x]
		temp_sum = 0
		for x in temp:
			temp_sum += x
		rowSum.append(temp_sum)
	return rowSum


#S:模糊矩阵	list
#W:权重向量集 list
#return list
def SW(S,W):
	arrs2 = numpy.array(S)
	arrw2 = numpy.array(W)
	#矩阵乘法:等价于矩阵arrs2 * arrw2
	#模糊综合评价向量
	return arrs2.dot(arrw2)

# 求特征向量max，C:判断矩阵，W:权重向量集  -- list type
# return number
def MaxEigenvector(C,W):
	W_len,tempsum = len(W),0
	ListArr = numpy.array(C)	
	for x in xrange(0,W_len):
		_temp =0
		for wlen in xrange(0,W_len):
			_temp += ListArr[x][wlen] * sumNormal[wlen]
		tempsum += _temp/sumNormal[x]
	return tempsum/W_len

# X_list = [
#     [1,5,3,7],
#     [0.2,1,0.3333333,2],
#     [0.3333333,3,1,4],
#     [0.1428571,0.5,0.25,1]
# ]
X_list = [
    [1,5,3,7],
    [1/2,1,1/3,2],
    [1/3,3,1,4],
    [1/7,0.5,1/4,1]
]
matCol = normalizedByCol(X_list)
sumRow = matSumRow(matCol)
sumNormal = normalizedByCol(sumRow)
#[0.54672133510117027, 0.1434649054179809, 0.24709006909387379, 0.062723690386975103]

maxeigenvecror = MaxEigenvector(X_list,sumNormal)
#4.4233415679425638