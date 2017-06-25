from __future__ import division
import numpy as np
 
def normalizeByArray(featureNum, minmaxArray, newMinValue=0, newMaxValue=1 ):
    def normalizeFunc(x):
        r = {}
        for i in range(featureNum):
            val = ( x[i+1] - minmaxArray[i,0] ) * newMaxValue / (minmaxArray[i,1] - minmaxArray[i,0] ) + newMinValue
            r[i+1] = val
        return r
    return np.frompyfunc(normalizeFunc,1,1)

     
dictData = np.array([
    [1,5,3,7],
    [0.2,1,0.3333333,2],
    [0.3333333,3,1,4],
    [0.1428571,0.5,0.25,1]
])

# dictData = np.array([
#     {1:1,2:5,3:3,4:7},
#     {1:0.2,2:1,3:0.3333333,4:2},
#     {1:0.3333333,2:3,3:1,4:4},
#     {1:0.1428571,2:0.5,3:0.25,4:1}
# ])

firstEle = dictData[0]
featureNum = len(firstEle)  # here we have 6 feature
minmaxValues = np.zeros((featureNum,2))
 
for xDict in dictData:
    for i in range(featureNum):
        if xDict[i+1]<minmaxValues[i,0]:
            minmaxValues[i,0] = xDict[i+1]
        elif xDict[i+1] > minmaxValues[i,1]:
            minmaxValues[i,1] = xDict[i+1]

outDictufuncXArray = normalizeByArray(featureNum,minmaxValues,0,1)(dictData)    #the result is a ufunc object ndarray
dictDataXArray = outDictufuncXArray.astype(dict)    # cast ufunc object ndarray to dict ndarray
 
print(dictDataXArray)
