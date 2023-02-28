#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
cric_data = np.loadtxt("cric.tsv", skiprows=1)
cric_data


# In[13]:


np.mean(cric_data[2,2])


# In[15]:


Sachin= cric_data[:,1]
Dravid=cric_data[:,2]
India=cric_data[:,3]
Sachin


# In[18]:


print(np.mean(Sachin))
print(np.mean(Dravid))
print(np.mean(India))


# In[19]:


print(np.median(Sachin))
print(np.median(Dravid))
print(np.median(India))


# In[20]:


print(np.average(Sachin))
print(np.average(Dravid))
print(np.average(India))


# In[ ]:




