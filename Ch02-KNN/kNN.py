# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:53:32 2017
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

kNN: k Nearest Neighbors

Input:
    inX: vector to compare with the existing dataSet (1xN)
    dataSet: our full matrix of training examples, size m data set of known vectors (NxM)
    labels: dataSet labels (1xM vector)
    k: the number of nearest neighbors to use in the voting for comparison (should be an odd number)

Output:
    take a majority vote, the most popular class label

"""

import os
import operator
import numpy as np


def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):  # inX = [1.0, 1.6]
    Nsize = dataSet.shape[0]
    diffMat = np.tile(inX, (Nsize, 1)) - dataSet
    sqdiffMat = diffMat ** 2
    sqDistances = sqdiffMat.sum(axis=1)  # axis = 1 each item sum up all dims.
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    # 升序, 同 np.argsort(distances)，第几个下标就对应第几大，是第几大对应的下标。
    classCount = {}
    # dict['key']只能获取存在的值，如果不存在则触发KeyError
    # dict.get(key, default=None)，如果不存在则返回一个默认值，如果设置了则是设置的，否则就是None
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    # operator.itemgetter(1) is sorted values, operator.itemgetter(0) keys.
    return sortedClassCount[0][0]


def file2matrix(filename):
    # get the number of lines in the file
    with open(filename, 'r') as fr:
        numberOfLines = len(fr.readlines())
    returnMat = np.zeros((numberOfLines, 3))  # prepare matrix to return
    classLabelVector = []  # prepare labels to return
    with open(filename, 'r') as fr:
        i = 0
        for line in fr.readlines():
            line = line.strip()
            listFromLine = line.split('\t')
            returnMat[i, :] = listFromLine[0:3]
            classLabelVector.append(int(listFromLine[-1]))
            i += 1
    return returnMat, classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(axis=0)  # for each column
    maxVals = dataSet.max(axis=0)
    ranges = maxVals - minVals
    normdataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normdataSet = (dataSet-np.tile(minVals, (m, 1)))/np.tile(ranges, (m, 1))
    # element wise divide
    return normdataSet, ranges, minVals


def datingClassTest():
    """
    这里不够严谨，应该是先分train 跟test集合，然后再各自normalize
    """
    hoRatio = 0.10  # hold out 10% #load data set from file
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        clf = classify0(normMat[i, :], normMat[numTestVecs:m, :],
                        datingLabels[numTestVecs:m], 3)
        print("The classifier came back with: %d, the real answer is: %d"
              % (clf, datingLabels[i]))
        if (clf != datingLabels[i]):
            errorCount += 1.0
    print("The total error count is: %f \n" % (errorCount))
    print("The total error rate is: %f \n" % (errorCount/float(numTestVecs)))


def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, rangeVals, minVals = autoNorm(datingDataMat)
    inArr = np.array([ffMiles, percentTats, iceCream])
    inX = (inArr - minVals)/rangeVals
    classifierResult = classify0(inX, normMat, datingLabels, 3)
    print("You will probably like this person: ",
          resultList[classifierResult - 1])


def img2vector(filename):
    """
    32 * 32 = 1024
    """
    returnVect = np.zeros((1, 1024))
    with open(filename, 'r') as fr:
        for i in range(32):
            lineStr = fr.readline()
            for j in range(32):
                returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    """
    # hwLabels存储0～9对应的index位置，trainingMat存放的每个位置对应的图片向量.
    """
    # 1. read trainingData # Get contents of directory
    hwLabels = []
    trainingFileList = os.listdir('./trainingDigits')  # load the training set
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]  # take off .txt
        classNumStr = int(fileStr.split('_')[0])  # split 1_03, 0_24
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('./trainingDigits/%s' % fileNameStr)
    # 2. read testData
    testFileList = os.listdir('./testDigits')  # iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]  # take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorTest = img2vector('testDigits/%s' % fileNameStr)
        # 没有标准化数据。
        clf = classify0(vectorTest, trainingMat, hwLabels, 3)
        if (clf != classNumStr):
            errorCount += 1.0
            print("the classifier came back with: %d, the real answer is: %d"
                  % (clf, classNumStr))
    errorRate = errorCount / float(mTest)
    print("\n the total number of errors is: %2d" % errorCount)
    print("\n the total error rate is: %f" % (errorCount/float(mTest)))
    return errorCount, errorRate




