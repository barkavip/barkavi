#!/usr/bin/env python
# coding: utf-8

# In[9]:


a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a > 0:

    if b>0:
    
      sum = a + b
      print("sum:", sum)  
    
    else:
    
        print("The Number2 is 0.so we can't perform the operation.")
    
    

else:
    
        print("The Number1 is 0.so we can't perform the operation.")
    
 
 


# In[11]:


def find_max( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
 
 
num = int(input('How many numbers: '))
 
lst = []
 
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
     
print("Maximum element in the list is :", find_max(lst))


# In[14]:


import pandas as pd
dataset=pd.read_csv("fish.csv")
print(dataset)


# In[ ]:




