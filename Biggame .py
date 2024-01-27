#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


d1 = pd.read_excel("big_game/All Places Census 2016 Population Estimates.xlsx")
d2 = pd.read_excel("big_game/All states Census 2017 Population Estimates.xlsx")
d3 = pd.read_excel("big_game/Big Game Census data.xlsx")

#Converting it into CSV Files
d1.to_csv("2016.csv", index=None, header=True)
d2.to_csv("2017.csv", index = None, header=True)
d3.to_csv("big_census.csv", index = None, header=True)


# In[4]:


data2016 = pd.read_csv('2016.csv')
data2017 = pd.read_csv('2017.csv')
bigCensus = pd.read_csv('big_census.csv')


# In[5]:


data2016.info()


# In[6]:


data2017.info()


# In[8]:


bigCensus.info()


# In[9]:


bigCensus.head()


# In[13]:


data2016.isnull().sum()


# In[14]:


data2017.isnull().sum()


# In[15]:


bigCensus.isnull().sum()


# In[16]:


bigCensus = bigCensus.drop([bigCensus.index[118], bigCensus.index[119], bigCensus.index[120]])


# In[17]:


bigCensus.isnull().sum()


# In[18]:


bigCensus.to_csv('Big_Game.csv', index=None, header=True)


# In[ ]:




