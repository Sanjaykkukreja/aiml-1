#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:02:15 2020
@author: mrizwan
Description: Modifying data in dataframe (CRUD)
Outputs are defined in the docstrings for easy understandin
"""
import pandas as pd

col = ['manufacturer','class','model']
df = pd.read_csv('data.csv', names = col)
print (df)
'''
  manufacturer      class  model
0      hyundai  hatchback    i10
1      hyundai      sedan  verna
2       hyndai        suv  creta
3        honda  hatchback   brio
4        honda      sedan  civic
5        honda        suv    crv
'''

# Add a new column 'year'
df['year'] = [2011,2015,2019,2012,2009,2010]
print (df)
'''
  manufacturer      class  model  year
0      hyundai  hatchback    i10  2011
1      hyundai      sedan  verna  2015
2       hyndai        suv  creta  2019
3        honda  hatchback   brio  2012
4        honda      sedan  civic  2009
5        honda        suv    crv  2010
'''

# Modify column name class -> type
df = df.rename(columns={'class': 'type'})
print (df)
'''
  manufacturer       type  model  year
0      hyundai  hatchback    i10  2011
1      hyundai      sedan  verna  2015
2       hyndai        suv  creta  2019
3        honda  hatchback   brio  2012
4        honda      sedan  civic  2009
5        honda        suv    crv  2010
'''
# Delete a column using drop
df.drop(['year'], axis=1)
print (df)
'''
  manufacturer       type  model  year
0      hyundai  hatchback    i10  2011
1      hyundai      sedan  verna  2015
2       hyndai        suv  creta  2019
3        honda  hatchback   brio  2012
4        honda      sedan  civic  2009
5        honda        suv    crv  2010
'''
new_df = df.drop(['year'], axis=1)
print (new_df)
'''
  manufacturer       type  model
0      hyundai  hatchback    i10
1      hyundai      sedan  verna
2       hyndai        suv  creta
3        honda  hatchback   brio
4        honda      sedan  civic
5        honda        suv    crv
'''

# Inserting a column at specific index                
new_df.insert(2,'year',[2011,2015,2019,2012,2009,2010])
print (new_df)
'''
  manufacturer       type  year  model
0      hyundai  hatchback  2011    i10
1      hyundai      sedan  2015  verna
2       hyndai        suv  2019  creta
3        honda  hatchback  2012   brio
4        honda      sedan  2009  civic
5        honda        suv  2010   crv
'''

# Propagate a value to a column
# (change entire column with provided data '2013')
new_df.year = 2013
print (new_df)
'''
  manufacturer       type  year  model
0      hyundai  hatchback  2013    i10
1      hyundai      sedan  2013  verna
2       hyndai        suv  2013  creta
3        honda  hatchback  2013   brio
4        honda      sedan  2013  civic
5        honda        suv  2013    crv
'''

# Export dataframe to CSV
new_df.to_csv('out.csv', index=False)
df = pd.read_csv('out.csv')
print (df)
'''
  manufacturer       type  year  model
0      hyundai  hatchback  2013    i10
1      hyundai      sedan  2013  verna
2       hyndai        suv  2013  creta
3        honda  hatchback  2013   brio
4        honda      sedan  2013  civic
5        honda        suv  2013    crv
'''

# Modify dataframe content based on condition
# if type has string 'hatchback'
# rename to H-Back and update the dataframe
def rname_type(i):
    i = i.lower()
    if i == 'hatchback':
        return 'H-Back'
    return i

df = pd.read_csv('out.csv',
                 converters={'type':rname_type})

print (df)
'''
  manufacturer    type  year  model
0      hyundai  H-Back  2013    i10
1      hyundai   sedan  2013  verna
2       hyndai     suv  2013  creta
3        honda  H-Back  2013   brio
4        honda   sedan  2013  civic
5        honda     suv  2013    crv
'''