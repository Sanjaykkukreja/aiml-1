#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:22:47 2020
@author: mrizwan
"""
import pandas as pd

# Initialize dataframes
df1 = pd.read_csv('one.csv')
print(df1)
'''
   year   name   id education
0  2010   andy  101  bachelor
1  2012  peter  102    master
2  2009   mark  103    school
'''
df2 = pd.read_csv('two.csv')
print(df2)
'''
    id   name country  age    city   status
0  101   andy     usa   31     nyc   single
1  102  peter      uk   29  london   single
2  103   mark     aus   33  sydney  married
3  104    riz     ind   34   blore  married
'''

# Merge two dfs based on it key id
df = pd.merge(df1,df2, on=['id', 'name'])
print(df)
'''
   year   name   id education country  age    city   status
0  2010   andy  101  bachelor     usa   31     nyc   single
1  2012  peter  102    master      uk   29  london   single
2  2009   mark  103    school     aus   33  sydney  married
'''

# Merge based on inner method
# Merges common element of data frame
df = pd.merge(df1,df2, how='inner', on='id')
print(df)
'''
   year name_x   id education name_y country  age    city   status
0  2010   andy  101  bachelor   andy     usa   31     nyc   single
1  2012  peter  102    master  peter      uk   29  london   single
2  2009   mark  103    school   mark     aus   33  sydney  married
'''

# Merge based on oute method
# Merges all element of data frame
df = pd.merge(df1,df2, how='outer', on='id')
print(df)
'''
     year name_x   id education name_y country  age    city   status
0  2010.0   andy  101  bachelor   andy     usa   31     nyc   single
1  2012.0  peter  102    master  peter      uk   29  london   single
2  2009.0   mark  103    school   mark     aus   33  sydney  married
3     NaN    NaN  104       NaN    riz     ind   34   blore  married
'''

# Creating a new column by applying condition on a column
x_dict = {'single': 1, 'married':2}
df['x'] = df['status'].map(x_dict)
print(df)
'''
     year name_x   id education name_y country  age    city   status  x
0  2010.0   andy  101  bachelor   andy     usa   31     nyc   single  1
1  2012.0  peter  102    master  peter      uk   29  london   single  1
2  2009.0   mark  103    school   mark     aus   33  sydney  married  2
3     NaN    NaN  104       NaN    riz     ind   34   blore  married  2
'''