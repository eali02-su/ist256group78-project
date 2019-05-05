#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install uber-rides')


# In[18]:


import json
import requests
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token='EmKIRFxYWD3363vLkDkljHArBB-3pJl-D_trqlFo')
client = UberRidesClient(session)
response = client.get_products(37.77, -122.41)
products = response.json.get('products')
#print(response)
print(products)


# In[19]:





# In[ ]:




