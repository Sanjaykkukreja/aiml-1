#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:15:23 2020
@author: mrizwan
Description:Handling CSV in Pandas
Outputs are defined in the docstrings for easy understandin
"""
import pandas as pd
df = pd.read_csv('data.csv')
print (df)
'''
   hyundai  hatchback    i10
0  hyundai      sedan  verna
1   hyndai        suv  creta
2    honda  hatchback   brio
3    honda      sedan  civic
4    honda        suv    crv
'''

# convert to matrix format
print (df.values)
'''
[['hyundai' 'sedan' 'verna']
 ['hyndai' 'suv' 'creta']
 ['honda' 'hatchback' 'brio']
 ['honda' 'sedan' 'civic']
 ['honda' 'suv' 'crv']]
'''

# adding header to dataframe
df = pd.read_csv('data.csv',
                 names = ['manufacturer','class','model'])
print(df)
'''
  manufacturer      class  model
0      hyundai  hatchback    i10
1      hyundai      sedan  verna
2       hyndai        suv  creta
3        honda  hatchback   brio
4        honda      sedan  civic
5        honda        suv    crv
'''

# print few random lines
print (df.sample(3))
'''
  manufacturer      class  model
0      hyundai  hatchback    i10
2       hyndai        suv  creta
1      hyundai      sedan  verna
'''

# print column with header name
print (df['model'])
'''
0      i10
1    verna
2    creta
3     brio
4    civic
5      crv
Name: model, dtype: objec
'''

# print column with header name 
# (this can be used when header name is not same as python obj)
print (df.model)
'''
0      i10
1    verna
2    creta
3     brio
4    civic
5      crv
Name: model, dtype: object
'''

# evaluvate the value of the column
print (df.manufacturer == 'honda')
'''
0    False
1    False
2    False
3     True
4     True
5     True
Name: manufacturer, dtype: bool
'''

# filter the data based on value in a column
print (df[df.manufacturer == 'honda'])
'''
  manufacturer      class  model
3        honda  hatchback   brio
4        honda      sedan  civic
5        honda        suv    crv
'''

# matrix representation with NumPy slicing
# fetch all data in rows (same as df.values)
print (df.values[:,])
'''
[['hyundai' 'hatchback' 'i10']
 ['hyundai' 'sedan' 'verna']
 ['hyndai' 'suv' 'creta']
 ['honda' 'hatchback' 'brio']
 ['honda' 'sedan' 'civic']
 ['honda' 'suv' 'crv']]
'''

# print all rows of 1st column
print (df.values[:,0])
'''
['hyundai' 'hyundai' 'hyndai' 'honda' 'honda' 'honda']
'''

# print all cols from 2nd to 4th row
print (df.values[1:4])
'''
[['hyundai' 'sedan' 'verna']
 ['hyndai' 'suv' 'creta']
 ['honda' 'hatchback' 'brio']]
'''

# print only 3rd column from 2nd to 4th row
print (df.values[1:4,2])
['verna' 'creta' 'brio']

# print last column for all rows
print (df.values[:,-1])
['i10' 'verna' 'creta' 'brio' 'civic' 'crv']