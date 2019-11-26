#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataCrimes = pd.read_csv('D:/Hasil Akhir - Sheet1.csv', encoding="ISO-8859-1")


# In[6]:


dataCrimes.info()


# In[7]:


dataCrimes.head(10)


# In[8]:


dataCrimes.shape


# In[9]:


dataCrimes.describe()


# In[10]:


correlation = dataCrimes.corr(method='kendall')
correlation


# In[ ]:




