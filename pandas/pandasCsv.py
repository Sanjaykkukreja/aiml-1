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
print (df.values)
'''
[['hyundai' 'sedan' 'verna']
 ['hyndai' 'suv' 'creta']
 ['honda' 'hatchback' 'brio']
 ['honda' 'sedan' 'civic']
 ['honda' 'suv' 'crv']]
'''
