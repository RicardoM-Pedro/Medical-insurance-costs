#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

# Enable inline plotting for Jupyter Notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# Load the dataset
data = pd.read_csv('medical_insurance_costs.csv')

# View the first few rows of the dataset
print(data.head())

# General information about the dataset
print(data.info())

# Descriptive statistics of the numerical data
print(data.describe())

# Count of unique values in each categorical column
print(data.nunique())

# Analysis of average charges by region
average_charges_by_region = data.groupby('region')['charges'].mean()
print(average_charges_by_region)

# Analysis of the relationship between smoking habits and medical charges
average_charges_by_smoker = data.groupby('smoker')['charges'].mean()
print(average_charges_by_smoker)

# Visualizing the distribution of ages
plt.hist(data['age'], bins=20, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

# Visualizing the relationship between BMI and Medical Charges
plt.scatter(data['bmi'], data['charges'], alpha=0.5)
plt.xlabel('BMI')
plt.ylabel('Medical Charges')
plt.title('Relationship between BMI and Medical Charges')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




