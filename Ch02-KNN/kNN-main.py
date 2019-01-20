# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:13:59 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""

import kNN

group, labels = kNN.createDataSet()
dataSet, labels = kNN.createDataSet()

kNN.classify0([0,9], group, labels, 3)

