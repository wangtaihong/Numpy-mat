# coding: utf8
from __future__ import division
import numpy
from numpy import array

##矩阵按列归一化
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

X_list = [
    [1,5,3,7],
    [0.2,1,0.3333333,2],
    [0.3333333,3,1,4],
    [0.1428571,0.5,0.25,1]
]
matCol = normalizedByCol(X_list)
sumRow = matSumRow(matCol)
sumNormal = normalizedByCol(sumRow)