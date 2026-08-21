#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
df = pd.read_csv("C:/Users/Nimisha Tripathy/Downloads/customer_shopping_behavior.csv")
df


# In[33]:


df.head()


# In[34]:


df.info()


# In[35]:


df.describe(include = 'all')


# In[36]:


df.isnull().sum()


# In[37]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))


# In[38]:


df.isnull().sum()


# In[39]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df.columns


# In[40]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
df.columns


# In[41]:


#create a column age_group

labels = ['Young Adult','Adult','Middle-aged','Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)
df[['age','age_group']].head(10)


# In[42]:


df


# In[43]:


#create column purchase_frequency_days

frequency_mapping = {
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quaterly' : 90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 months' : 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[44]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[45]:


df


# In[46]:


df[['discount_applied','promo_code_used']].head(10)


# In[47]:


(df['discount_applied'] == df['promo_code_used']).all()


# In[48]:


df = df.drop('promo_code_used', axis=1)


# In[49]:


df.columns


# In[50]:


get_ipython().system('pip install psycopg2-binary')


# In[51]:


get_ipython().system('pip install psycopg2-binary sqlalchemy')


# In[52]:


from sqlalchemy import create_engine


# In[61]:


#Step 1: Connect To PostgreSQL
#Replace placeholders with your actual details

username = "postgres"
password = "bangtan7"
host = "localhost"
port = "5432"
database = "Customer_Behavior"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

#Step 2: Load datdframe into PostgreSQL
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")


# In[ ]:


#import pandas as pd
#from sqlalchemy import create_engine
#from urllib.parse import quote_plus

#username = "postgres"
#password = quote_plus("Bangtan7@#")   # important if special chars exist
#host = "localhost"
#port = "5432"
#database = "testdb"

#engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

#table_name = "customer"
#df.to_sql(table_name, engine, if_exists="replace", index=False)

#print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




