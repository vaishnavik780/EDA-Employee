#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# In[2]:


df = pd.read_csv("full_employee_data.csv")


# In[4]:


print(df.head())


# In[5]:


print(df.tail())


# In[6]:


print(df.columns)


# In[7]:


filtered_df = df[df['Salary'] > 80000]
print(filtered_df)


# In[8]:


employee_count = df['Department'].value_counts()
print(employee_count)


# In[9]:


filtered_df = df[(df['PerformanceRating'] > 4) & (df['Salary'] > 70000)]
print(filtered_df)


# In[10]:


print(df.isnull().sum())


# In[11]:


average_salary = df['Salary'].mean()
print(f"Average Salary: {average_salary}")


# In[12]:


marital_status_count = df['MaritalStatus'].value_counts()
print(marital_status_count)


# In[13]:


no_health_insurance = df[df['HealthInsurance'] == 'No']
print(no_health_insurance)


# In[15]:


average_work_hours = df.groupby('Department')['WorkHours'].mean()
print(average_work_hours)


# In[16]:


software_engineers = df[df['JobTitle'] == 'Software Engineer']
print(software_engineers)


# In[20]:


plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Department', y='Salary', ci=None, palette='Set2')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.show()


# In[21]:


marital_status_counts = df['MaritalStatus'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(marital_status_counts, labels=marital_status_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Distribution of Marital Status')
plt.show()


# In[22]:


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Experience', y='Salary', hue='Department', palette='Set1')
plt.title('Salary vs. Experience')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.show()


# In[ ]:





# In[24]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='WorkMode', palette='Set2')
plt.title('Number of Employees by Work Mode')
plt.xlabel('Work Mode')
plt.ylabel('Count')
plt.show()


# In[25]:


# Convert 'JoiningDate' to datetime
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='JoiningDate', y='PerformanceRating', marker='o', color='b')
plt.title('Performance Rating Over Time')
plt.xlabel('Joining Date')
plt.ylabel('Performance Rating')
plt.xticks(rotation=45)
plt.show()


# In[2]:


plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=10, kde=false, color='skyblue')
plt.title('Employee Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[27]:


plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Department', palette='muted')
plt.title('Number of Employees by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[29]:


df['Bonus'] = pd.to_numeric(df['Bonus'], errors='coerce')

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Department', y='Bonus', ci=None, palette='Blues')
plt.title('Bonus by Department')
plt.xlabel('Department')
plt.ylabel('Bonus')
plt.xticks(rotation=45)
plt.show()


# In[31]:


plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Department', y='Salary', palette='Set3')
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




