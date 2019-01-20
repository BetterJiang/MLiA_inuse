# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:13:43 2017
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""

f=open('./notfound.txt', 'r')

with open('./file.txt', 'r') as f:
    print(f.read())


try:
    with open('./file', 'r') as f:
        pass
    # do with file handle
except Exception as e:
    print(e)
    # do with exception
