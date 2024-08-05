#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(*n):
    return sum(n)


# In[5]:


def mult(n1 , n2 ):
    return n1 * n2


# In[6]:


def check():
    num = int(input("enter your num "))
    if num % 2 == 0 :
        return "Even"
    else:
        return "Odd"

