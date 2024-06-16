#!/usr/bin/env python
# coding: utf-8

# importing libraries

# In[6]:


import pandas as pd


# Importing data set

# In[4]:


data= pd.read_csv(r"C:/Users/User/Desktop/Udemy  Projects/Udemy Data Analysis Projects/Project 1/Project+1+-+Weather+Dataset.csv")


# checking for Errors

# In[5]:


data


# Analysing Data and checking data 

# to find first 5 rows

# In[7]:


data.head()


# shape of data set

# In[9]:


data.shape


# Index Of data frame

# In[10]:


data.index


# columns of Data set

# In[13]:


data.columns


# data types of Columns in data set

# In[14]:


data.dtypes


# find unique values( Displays unique values)

# Syntax : data['column name'].unique()

# In[17]:


data['Weather'].unique()


# nunique() used for whole data set 

# In[18]:


data.nunique()


# Shows non Null Values (.count)

# In[20]:


data.count()


# .value_counts() only for Single Columns

# In[21]:


data['Weather'].value_counts()


# .info Gives you information.

# In[22]:


data.info()


# Question)1. Find all Unique'Wind speed' Values in the data.

# In[23]:


data.head(2)


# In[24]:


data.nunique()


# In[25]:


data['Wind Speed_km/h'].nunique()


# In[26]:


data['Wind Speed_km/h'].unique() #Answer


# Question)2. find the number of times when the 'weather is exactly clear'.

# In[27]:


data.head(2)


# In[31]:


#Value_Counts()
data.Weather.value_counts()


# In[32]:


# Filtering
#data.head(2)
data[data.Weather == 'Clear']


# In[33]:


# groupby()
#data.head(2)
data.groupby('Weather').get_group('Clear')


# Question) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'

# In[34]:


data.head(2)


# In[36]:


#Answer
data[data['Wind Speed_km/h']== 4]


# Question) 4. Find out all the Null Values in the data.

# In[37]:


data.isnull().sum()


# In[38]:


data.notnull().sum()


# Question) 5. Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[39]:


data.head(2)


# In[40]:


data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)


# In[41]:


data.head()


# Question) 6. What is the mean 'Visibility' ?

# In[42]:


data.head(2)


# In[45]:


data.Visibility_km.mean()


# Question) 7. What is the Standard Deviation of 'Pressure' in this data?

# In[48]:


data.Press_kPa.std()


# Question) 8. Whats is the Variance of 'Relative Humidity' in this data ?

# In[49]:


data['Rel Hum_%'].var()


# Question) 9. Find all instances when 'Snow' was recorded.

# In[52]:


# value_counts()
#data.head(2)
data['Weather Condition'].value_counts()


# In[53]:


#Filtering
data[data['Weather Condition'] == 'Snow']


# In[54]:


# str.contains
data[data['Weather Condition'].str.contains('Snow')].tail(50)


# Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[55]:


data.head(2)


# In[56]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# Question) 11. What is the Mean value of each column against each 'Weather Conditon' ?

# In[58]:


data.head(2)


# In[59]:


data.groupby('Weather Condition').mean()


# Question 12. What is the Minimum & Maximum value of each column against each 'Weather Conditon' ?

# In[60]:


data.head(2)


# In[61]:


data.groupby('Weather Condition').min()


# In[62]:


data.groupby('Weather Condition').max()


# Question 13. Show all the Records where Weather Condition is Fog.

# In[63]:


data[data['Weather Condition']== 'Fog']


# Question 14. Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[65]:


data[(data['Weather Condition']=='Clear')| (data['Visibility_km']> 40)].tail(50)


# Question 15. Find all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'

# In[66]:


data.head(2)


# In[67]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)|(data['Visibility_km'] > 40)]


# BY  -  U.V. Sri Harsha
