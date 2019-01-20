# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 08:26:52 2017
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""

import kNN
from imp import reload
reload(kNN)

group, labels = kNN.createDataSet()

kNN.classify0([2, 3], group, labels, 3)
kNN.classify0([0.5, 0.6], group, labels, 3)

filename = 'datingTestSet2.txt'

datingDataMat, datingLabels = kNN.file2matrix(filename)

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
%matplotlib qt5

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
plt.show()


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2],
           c=15.0 * np.array(datingLabels))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2],
           s=15.0 * np.array(datingLabels), c=15.0 * np.array(datingLabels))
plt.show()


kNN.classifyPerson()


filename = './testDigits/0_13.txt'
testVector = kNN.img2vector(filename)
testVector[0, 0:31]

kNN.handwritingClassTest()

