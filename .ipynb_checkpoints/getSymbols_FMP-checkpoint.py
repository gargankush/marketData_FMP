#!/usr/bin/env python
# coding: utf-8

# # Python Script to source stock symbols and their latest information from Financial Modelling Prep API

# ### Import required libraries

# In[ ]:


#!/usr/bin/env python
# Import the required libraries
import os
import pandas as pd
# Checking whether system is using python 3 or python 2
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

#Import json as data from FMP will be in json format
import json


# ### Function to source the symbols from FMP

# In[ ]:


def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


# ### Function to get the API Key stored in the environmental variable. To get details on the procedure refer to my medium post: https://gargankush.medium.com/storing-api-keys-as-environmental-variable-for-windows-linux-and-mac-and-accessing-it-through-974ba7c5109f?source=friends_link&sk=bfae7f0c74502a67cb58f19569e24a76

# In[ ]:


# Get the API Key
def get_API_Key():
    """
    Receive the content of API key sdaved in the Environmental variable: FMP_APIKEY.
    API key is unique for each user

    Parameters
    ----------
    None

    Returns
    -------
    API Key as string
    """
    FMP_API_KEY = os.environ.get('FMP_APIKEY')
    return FMP_API_KEY


# ### Function to convert the json data to csv file

# In[27]:


def json_to_csv(json_data, csv_file):
    df = pd.DataFrame(json_data)
    # Sort the dataframe on exchange
    df.sort_values(by=['exchange'], ascending=True, inplace=True)
    df.to_csv(csv_file, index=None)


# ### Main function to source all the symbols for which data is provided by FMP API

# In[28]:


def main():
    #Output csv file name
    output_file = "symbols_FMP.csv"
    
    # FMP url to fetch the data
    url = ("https://financialmodelingprep.com/api/v3/stock/list?apikey="+get_API_Key())
    
    # Get Symbols in json format
    symbols_json = get_jsonparsed_data(url)
    
    # Convert json format to csv file
    json_to_csv(symbols_json,output_file)
if __name__ == "__main__":
    main()


# ## Congratulations!!! all the symbol data is sourced from API and saved in csv file
