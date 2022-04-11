# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:57:30 2022

@author: revan
"""

import os
import pandas as pd
import numpy as np
os.chdir("C:/Users/revan/Desktop/Experiments") #cd command

family = pd.read_csv("exp.csv") #read and import .csv files 

#family is a dataframe ("pandas.core.frame.DataFrame")

''' 
   Unnamed: 0     Name  Age  Height gender
0           1      Rev   19     5.4      m
1           2      siv   50     5.7      m
2           3    ranji   42     5.0      f
3           4  ranjith   42     5.5      m
4           5    rahul   30     5.4      m
5           6     reva   30     5.3      f

there is always a presence of a unwanted column unnamed it acts just the order no: 
    so inorder to remove we set the index = 0
 
'''

family = pd.read_csv("exp.csv",index_col= 0)

'''
      Name  Age  Height gender
1      Rev   19     5.4      m
2      siv   50     5.7      m
3    ranji   42     5.0      f
4  ranjith   42     5.5      m
5    rahul   30     5.4      m
6     reva   30     5.3      f

'''

# lllry family = pd.read_csv("exp.csv", index_col =1)
'''
         Unnamed: 0  Age  Height gender
Name                                   
Rev               1   19     5.4      m
siv               2   50     5.7      m
ranji             3   42     5.0      f
ranjith           4   42     5.5      m
rahul             5   30     5.4      m
reva              6   30     5.3      f
'''


#print(family)

#---------------------------------------------------------------------------------------

'''
 Two ways to copy dataframe
 
 1 . Shallow copy
        syntax: 
              
            family_copy = family
                     
                      or
                      
            family_copy = family.copy(deep = False)
            
            """ deep = False => shallow copy"""
    
            
 so it creates a new variable that shares the reference of the previous dataframe
 
 Since its the reference any changes made to the copy reflects in the original dataframe
 
-------------------------------------------------------------------------------------            

 2. Deep copy
    set deep = True
    
    will have actual copy of the dataframe
            
'''

#----------------------------------------------------------------------------------------

'''
Indexing methods

1. row indexing                      
                      
   syntax: 
     
     Dataframe.index
     
   ex: 
       
       f = family.copy(deep = True)
       f.index
       
       """
       output :-
       
       RangeIndex(start=0, stop=6, step=1)
       
       """
      
--------------------------------------------------------------------------------------
2. column indexing

     syntax: 
        
         Dataframw.columns
         
     ex:
          f.colummns
          
    output : Index(['Unnamed: 0', 'Name', 'Age', 'Height', 'gender'], dtype='object')
    
    
    
    
3. f.size # gives the total size of the dataframe
 
4. f.shape #gets the dimensions
-------------------------------------------------------------------------------------------

Memory usage

syntax:
    dataframe.memory_usage([index,deep])
ex:
    
f.memory_usage()

########## 
output:
    Index         128
    Unnamed: 0     48
    Name           48
    Age            48
    Height         48
    gender         48
    dtype: int64
    ##################

produces memory used by each column
--------------------------------------------------------------------------------------------

Array dimensions/ no. of axis

f.ndim
  
output :- 2
ie., rows and columns
--------------------------------------------------------------------------------------------
'''


#-------------------------------------------------------------------------------------------

#indexing  and   selecting data

'''
[] : slicing operator
. : used for indexing
------------------------------------------------------------------------------------

1 . Dataframe.head([n]) :- returns the first n rows from the dataframe

by default it will give the first 5 rows

f.head(5): returns first 6 rows (ie., from 0 to 5)
    
    Unnamed: 0     Name  Age  Height gender
 0           1      Rev   19     5.4      m
 1           2      siv   50     5.7      m
 2           3    ranji   42     5.0      f
 3           4  ranjith   42     5.5      m
 4           5    rahul   30     5.4      m
 5           6     reva   30     5.3      f
 
 -------------------------------------------------------------------------
 2. Dataframe.tail([n]):- returns the last n rows for the object based on position

default n = 5
ie., last 5 values

f.tail(6):-

          Unnamed: 0     Name  Age  Height gender
       0           1      Rev   19     5.4      m
       1           2      siv   50     5.7      m
       2           3    ranji   42     5.0      f
       3           4  ranjith   42     5.5      m
       4           5    rahul   30     5.4      m
       5           6     reva   30     5.3      f
-----------------------------------------------------------------------------------------
'''
#fastest  way to access scalar functions
'''
1. at[row_label,col_label] :- provides label based scalar lookups

ex: 
    f.at[0,'Name'] :-
    'Rev'

    f.at[0,'Age'] :-
    19
    
-------------------------------------------------------------------------------
2 iat[row_index, col_index] :- provides integer-based lookups


ex:-

f = pd.read_csv("exp.csv",index_col=0)


      Name  Age  Height gender
1      Rev   19     5.4      m
2      siv   50     5.7      m
3    ranji   42     5.0      f
4  ranjith   42     5.5      m
5    rahul   30     5.4      m
6     reva   30     5.3      f


f.iat[1,2]

output:-

5.7

-------------------------------------------------------------------------------
'''
#------------------------------------------------------------------------------
'''
.loc[row_label,col_label] Operator

always slicing operator should be used 

can access a group of rows and column by labels

ex:- 

f.loc[:,"Name"]

o/p:-

1        Rev
2        siv
3      ranji
4    ranjith
5      rahul
6       reva
Name: Name, dtype: object


------------------------------------------------------------------------------
f.loc[:2,"Name"]
Out[28]: 
1    Rev
2    siv
Name: Name, dtype: object

f.loc[1:2,"Name"]
Out[29]: 
1    Rev
2    siv
Name: Name, dtype: object

f.loc[2:3,"Name"]
Out[30]: 
2      siv
3    ranji
Name: Name, dtype: object

f.loc[2:2,"Name"]
Out[31]: 
2    siv
Name: Name, dtype: object


------------------------------------------------------------------------------

f.loc[:,["Name","Age"]]
Out[35]: 
      Name  Age
1      Rev   19
2      siv   50
3    ranji   42
4  ranjith   42
5    rahul   30
6     reva   30


f.loc[2:2,["Name","Age"]]
Out[36]: 
  Name  Age
2  siv   50


------------------------------------------------------------------------------




































                   