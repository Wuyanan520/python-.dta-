# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:14:18 2016

@author: wyn_pc
"""


import pandas as pd


M = pd.read_stata('Wxt.dta')#4068406
A = pd.read_stata('A.dta')#406*1
A = A.fillna(0)
M.columns = [e for e in range(406)]
A.columns = [0]
M1 = M.dot(A)
M1.to_stata('m.dta')

a = pd.DataFrame([[1,2],[1,2]])
b = pd.DataFrame([[1,2,3],[1,2,3]])
c = a.dot(b)