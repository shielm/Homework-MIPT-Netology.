#!/usr/bin/env python
# coding: utf-8

# # Задание 1. Со словами "test", "testing".

# In[ ]:


word1 = 'test'
word2 = 'testing'

lenght1 = len(word1)
lenght2 = len(word2)

if lenght1%2==0:
    print(word1[int(lenght1/2-1):int(lenght1/2+1)])
else:
    print(word1[int(lenght1/2)])
    
if lenght2%2==0:
    print(word2[int(lenght2/2-1):int(lenght2/2+1)])
else:
    print(word2[int(lenght2/2)])


# # Задание 1.1. С открытым вводом.

# In[14]:


word = str(input())

lenght = len(word)

if lenght%2==0:
    print(word[int(lenght/2-1):int(lenght/2+1)])
else:
    print(word[int(lenght/2)])

