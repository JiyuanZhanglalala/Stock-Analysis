#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import yfinance as yf
import plotly.express as px


# In[3]:


import datetime
Current_Date = datetime.datetime.today()


# In[4]:


Current_Date


# In[5]:


yf.download


# In[6]:


yf.Ticker("NIO").get_cashflow


# In[7]:


yf.Ticker("NIO").info


# In[8]:


yf.download("NIO",period = "ytd", interver="1m")


# In[9]:


NIO=yf.download("NIO",period = "ytd", interver="1m")


# In[10]:


NIO.columns


# In[11]:


NIO=NIO.reset_index()


# In[12]:


NIO.columns


# In[13]:


#NIO.to_csv('testNIO.csv')


# # Recommendations for buying or selling a company’s stock is provided by different Finacial Firms.

# In[14]:


yf.Ticker("NIO").recommendations


# # plot

# In[15]:


fig = px.line(NIO, x='Date', y='Close')
fig.show()


# In[16]:


pwd


# In[ ]:





# In[ ]:




