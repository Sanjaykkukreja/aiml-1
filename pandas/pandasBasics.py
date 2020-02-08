#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:41:00 2020
@author: mrizwan
Description: Basics of Pandas
Outputs are defined in the docstrings for easy understanding
"""
import pandas as pd

data = {
        'apples': [3,2,5,7],
        'oranges': [1,8,4,0]
        }
# initializing dataframe
count = pd.DataFrame(data)
print (count)
'''
   apples  oranges
0       3        1
1       2        8
2       5        4
3       7        0
'''

# updating index
count = pd.DataFrame(data, index=['Mon','Tue','Wed','Thu'])
print (count)
'''
     apples  oranges
Mon       3        1
Tue       2        8
Wed       5        4
Thu       7        0
'''

# locate data by index name (day)
print (count.loc['Wed'])
'''
apples     5
oranges    4
Name: Wed, dtype: int64
'''

# get data of multiple rows by index name
print (count.loc[['Mon', 'Wed']])
'''
     apples  oranges
Mon       3        1
Wed       5        4
'''

# get 1st 2 rows
print (count[0:2])
'''
     apples  oranges
Mon       3        1
Tue       2        8
'''

# get 3rd and 4th rows
print (count[2:4])
'''
     apples  oranges
Wed       5        4
Thu       7        0
'''

# locate row data by its index id
print (count.iloc[1])
'''
apples     2
oranges    8
Name: Tue, dtype: int64
'''

# print matrix length rows x cols
print (count.shape)
'''
(4, 2)
'''
print (count.loc['Mon'].shape)
'''
(2,)
'''
print (count.iloc[0].shape)
'''
(2,)
'''
print (count.iloc[0:2].shape)
'''
(2, 2)
'''
print (count.loc[['Mon','Thu']].shape)
'''
(2, 2)
'''

# print column with heading 'apples'
print (count['apples'])
'''
Mon    3
Tue    2
Wed    5
Thu    7
Name: apples, dtype: int64
'''