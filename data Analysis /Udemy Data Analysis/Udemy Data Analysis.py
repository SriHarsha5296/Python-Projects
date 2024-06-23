#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
data = pd.read_csv(r"C:/Users/User/Desktop/Udemy  Projects/Udemy Data Analysis Projects/Project 7/Project+7+-+Udemy+Dataset.csv")
data.head()


# 1. What are all different subjects for which Udemy is offering courses ?

# In[4]:


data.subject.unique()


# 2. Which subject has the maximum number of courses.

# In[7]:


data.subject.value_counts()


# 3. Show all the courses which are Free of Cost.

# In[8]:


data[data.is_paid == False]


# 4. Show all the courses which are Paid.

# In[9]:


data[data.is_paid == True]


# 5. Which are Top Selling Courses ?

# In[10]:


data.sort_values('num_subscribers' , ascending = False)


# 6. Which are Least Selling Courses ?

# In[11]:


data.sort_values('num_subscribers')


# 7. Show all courses of Graphic Design where the price is below 100 ?

# Correct Solution : 
# data1 = data[data.price != 'Free']    - Removing all rows which contains Free and creating a new dataframe 'data1'.
# data1.price = data1.price.astype(int) - Changing the price column datatype to 'int'.
# data1[(data1.subject == 'Graphic Design') & (data1.price < 100) ] - Applying the logic now
# And, the result would be 450 rows.

# In[12]:


data[(data.subject == 'Graphic Design') & (data.price < '100') ]


# In[13]:


data[(data.subject == 'Graphic Design') & (data.price == '100') ]


# 8. List out all the courses that are related with 'Python'.

# In[14]:


len(data[data.course_title.str.contains('Python')])


# 9. What are courses that published in year 2015 ?

# In[15]:


data.dtypes


# In[16]:


data['published_timestamp'] = pd.to_datetime(data.published_timestamp)


# In[17]:


data['Year'] = data['published_timestamp'].dt.year


# In[18]:


data[data.Year == 2015]


# 10. What are the Max. Number of Subscribers for Each Level of courses ?

# In[19]:


data.level.unique()


# In[20]:


data.groupby('level')['num_subscribers'].max()


# In[21]:


data.groupby('level').max()


# In[ ]:





# In[ ]:





# By Sri Harsha.

# In[ ]:





# In[ ]:





# In[ ]:




