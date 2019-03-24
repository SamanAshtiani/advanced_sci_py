#!/usr/bin/env python3

import pandas as pd
import numpy as np


#examples to start working on actual datasets
df = pd.DataFrame({'a':np.random.uniform(5,size=15), 'b': np.random.uniform(5,size=15)})
columns = [('a', 'c'), ('b', 'c')]
df.columns = pd.MultiIndex.from_tuples(columns)


df1 = pd.DataFrame({'col1':[1,2,3], 'col2':[4,5,6]}, index=['s1', 's2', 's3'])
df2 = pd.DataFrame({'col2':[10, 11, 12], 'col1': [7,8,9], 'col3':[13, 14, 15]}, index = ['s4', 's5', 's6'])
df3 = pd.DataFrame({'col4':[16,17]}, index=['third_1', 'third_2'])
pd.concat([df1,df2, df3])
