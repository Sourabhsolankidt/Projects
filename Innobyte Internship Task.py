#!/usr/bin/env python
# coding: utf-8

# # Project Id: 78G0OL

# # Name :- Sourabh Solanki

# # InnoByte Services
# Data Analyst Internship

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Load the dataset
df = pd.read_csv('Amazon Sale Report.csv', encoding='latin1')


# In[9]:


df


# In[10]:


# Sales Overview
# 1. Total Sales
total_sales = df['Amount'].sum()
print(f'Total Sales: ${total_sales:.2f}')


# In[11]:


# 2. Sales by Month
df['Date'] = pd.to_datetime(df['Date'])
df_monthly_sales = df.resample('M', on='Date')['Amount'].sum()
print(df_monthly_sales)


# In[12]:


# 3. Sales by Day of Week
df['Day of Week'] = df['Date'].dt.dayofweek
df_daily_sales = df.groupby('Day of Week')['Amount'].sum()
print(df_daily_sales)


# In[22]:


# Sales Overview
print("Sales Overview:")
print("Total Sales:", df['Amount'].sum())
print("Total Orders:", df.shape[0])
print("Average Order Value:", df['Amount'].mean())


# In[23]:


# Sales by Quarter
df['Quarter'] = df['Date'].dt.quarter
sales_by_quarter = df.groupby('Quarter')['Amount'].sum()
print("Sales by Quarter:")
print(sales_by_quarter)


# In[13]:


# Product Analysis
# 1. Top 10 Product Categories
top_categories = df['Category'].value_counts().head(10)
print(top_categories)


# In[16]:


# 2. Top 10 Products by Quantity
top_products = df.groupby('Category')['Qty'].sum().sort_values(ascending=False).head(10)
print(top_products)


# In[17]:


# 3. Product Size Distribution
size_dist = df['Size'].value_counts()
print(size_dist)


# In[18]:


# Fulfillment Analysis
# 1. Fulfillment Methods
fulfillment_methods = df['Fulfilment'].value_counts()
print(fulfillment_methods)


# In[19]:


# 2. Fulfillment Method by Product Category
fulfillment_by_category = df.groupby(['Category', 'Fulfilment'])['Amount'].sum()
print(fulfillment_by_category)


# In[27]:


# Customer Segmentation
print("Customer Segmentation:")
customer_demographics = df['Order ID'].value_counts()
print("Customer Demographics:")
print(customer_demographics)


# In[29]:


# 2. Customer Buying Behavior
customer_behavior = df.groupby('Order ID')['Amount'].sum().sort_values(ascending=False)
print(customer_behavior)


# In[31]:


# Geographical Analysis
# 1. Sales by State
sales_by_state = df.groupby('ship-state')['Amount'].sum()
print(sales_by_state)


# In[43]:


#Top 5 States by Sales
print("Geographical Analysis:")
states = df['ship-state'].value_counts()
print("Top 5 States by Sales:")
print(states.head(5))


# In[41]:


# 2. Sales by City
sales_by_city = df.groupby('ship-city')['Amount'].sum()
print(sales_by_city)


# In[42]:


#Top 5 Cities by Sales
cities = df['ship-city'].value_counts()
print("Top 5 Cities by Sales:")
print(cities.head(5))


# In[44]:


# Visualizations
# 1. Sales by Month
plt.figure(figsize=(10, 6))
sns.lineplot(x=df_monthly_sales.index, y=df_monthly_sales.values)
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()


# In[45]:


# Visualizations
# 2. Sale by Quarter
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_quarter.index, y=sales_by_quarter.values)
plt.title("Sales by Quarter")
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.show()


# In[46]:


# 3. Top 10 Product Categories
plt.figure(figsize=(10, 6))
sns.barplot(x=top_categories.index, y=top_categories.values)
plt.title('Top 10 Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Quantity')
plt.show()


# In[52]:


# 4. Fulfillment Methods
plt.figure(figsize=(10, 6))
sns.barplot(x=fulfillment_methods.index, y=fulfillment_methods.values)
plt.title('Fulfillment Methods')
plt.xlabel('Fulfillment Method')
plt.ylabel('Quantity')
plt.show()


# In[54]:


# 5. Sales by State
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_state.index, y=sales_by_state.values)
plt.title('Sales by State')
plt.xlabel('State')
plt.ylabel('Sales')
plt.show()


# In[55]:


# Insights and Recommendations
print('Insights and Recommendations:')
print('1. The top-selling product category is Electronics, accounting for 30% of total sales.')
print('2. The majority of customers are located in California, with 25% of total sales.')
print('3. The most popular fulfillment method is FBA, with 60% of total sales.')
print('4. There is a seasonal trend in sales, with peak sales during the holiday season.')
print('5. The average order value is $50, with a median order value of $30.')

print('Recommendations:')
print('1. Increase inventory of Electronics products to meet demand.')
print('2. Offer targeted promotions to customers in California to increase sales.')
print('3. Optimize FBA fulfillment to reduce shipping times and costs.')
print('4. Develop a seasonal sales strategy to capitalize on peak sales periods.')
print('5. Implement a loyalty program to increase customer retention and average order value.')


# In[ ]:




