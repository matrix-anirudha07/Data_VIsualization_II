#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#line chart


# In[4]:


apples = [25.6,37.8,44.1,22.1,29.7,56.7,77.6,43.5]


# In[5]:


plt.plot(apples)


# In[6]:


plt.plot(apples);


# In[7]:


# Customizing the Axis


# In[8]:


years = [2014,2015,2016,2017,2018,2019,2020,2021]
apples = [25.6,37.8,44.1,22.1,29.7,56.7,77.6,43.5]
plt.plot(years,apples)


# In[9]:


# Labels on Axis


# In[10]:


plt.plot(years,apples)
plt.xlabel('years')
plt.ylabel('yield (tons per hectare)');


# In[11]:


# Plotting multiple lines


# In[12]:


years = range(2001, 2007)
pineapples= [22,26,34,36,44,55]
oranges = [31,28,29,34,30,49]


# In[13]:


plt.plot(years, pineapples)
plt.plot(years, oranges)
plt.xlabel('Years')
plt.ylabel('Yield (tons per hectare)');


# In[14]:


# chart title & Legend || #Line marker
#https://matplotlib.org/stable/api/markers_api.html


# In[15]:


plt.plot(years,pineapples, marker = "$a$", c = 'y', ls = '-', lw = '3',ms ='7', mec = 'r',mew = '2', mfc = 'b', alpha = 0.9)
plt.plot(years,oranges, marker = "$f$", c = 'g', ls = '--', lw = '4',ms ='6', mec = 'y',mew = '1.5', mfc = 'g', alpha = 0.8)

plt.xlabel('Years')
plt.ylabel('Yields (Ton per hectare)')

plt.title('Crops yield in Maharashtra')
plt.legend(['Pineapples', 'Oranges']);


# In[16]:


plt.figure(figsize=(6,5))
plt.plot(years,pineapples, marker = "$a$", c = 'y', ls = '-', lw = '3',ms ='7', mec = 'r',mew = '2', mfc = 'b', alpha = 0.9)
plt.plot(years,oranges, marker = "$f$", c = 'g', ls = '--', lw = '4',ms ='6', mec = 'y',mew = '1.5', mfc = 'g', alpha = 0.8)

plt.xlabel('Years')
plt.ylabel('Yields (Ton per hectare)')

plt.title('Crops yield in Maharashtra')
plt.legend(['Pineapples', 'Oranges']);


# In[17]:


sns.set_style('darkgrid')


# In[18]:


plt.plot(years,pineapples, 's-r')
plt.plot(years,oranges, '1--b')

plt.xlabel('Years')
plt.ylabel('Yields (Ton per hectare)')

plt.title('Crops yield in Maharashtra')
plt.legend(['Pineapples', 'Oranges']);


# In[19]:


import matplotlib


# In[20]:


matplotlib.rcParams['font.size'] = 14


# In[21]:


plt.plot(years,pineapples, 's-r')
plt.plot(years,oranges, '1--b')

plt.xlabel('Years')
plt.ylabel('Yields (Ton per hectare)')

plt.title('Crops yield in Maharashtra')
plt.legend(['Pineapples', 'Oranges']);


# In[22]:


# ScatterPlot


# In[24]:


df = sns.load_dataset('iris')
df


# In[26]:


df.species.unique()


# In[27]:


plt.plot(df.sepal_length,df.sepal_width);


# In[34]:


sns.scatterplot(data=df, x='sepal_length', y='sepal_width');


# In[53]:


plt.figure(figsize=(9,7))
plt.title('Sepal Dimensions')
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species',s=70,alpha=0.75);


# In[54]:


# Histogram


# In[63]:


import numpy as np


# In[67]:


plt.title('Distribution of Sepal_Width')
plt.hist(df.sepal_width, bins=np.arange(2,5,0.25));


# In[70]:


setosa_df = df[df.species=='setosa']
versicolor_df = df[df.species=='versicolor']
virginica_df = df[df.species=='virginica']


# In[71]:


setosa_df


# In[111]:


plt.hist(setosa_df.sepal_width, alpha = 0.8, bins=np.arange(2,5,0.25))
plt.hist(virginica_df.sepal_width, alpha = 0.3, bins=np.arange(2,5,0.25))
plt.legend(['setosa','virginica']);


# In[120]:


plt.hist([setosa_df.sepal_width,
         virginica_df.sepal_width,
         versicolor_df.sepal_width],
         alpha = 0.9, bins=np.arange(2,5,0.25),
         stacked = True)
plt.legend(['Setosa','Versicolor','virginica'])
plt.title("Distribution of species_width");


# In[ ]:


# Bar Chart


# In[130]:


plt.bar(years,pineapples);


# In[131]:


plt.plot(years,pineapples);


# In[134]:


plt.plot(years,pineapples, 'o--r')
plt.bar(years,pineapples)


# In[156]:


plt.bar(years,pineapples)


# In[157]:


plt.bar(years,oranges)


# In[160]:


plt.plot(years,oranges, 'o--r')
plt.plot(years,pineapples, 's--b')
plt.bar(years,oranges)
plt.bar(years,pineapples, bottom=oranges); 
plt.legend(['oranges','pineapples']);


# In[162]:


df1 = sns.load_dataset('tips')
df1


# In[177]:


plt.bar(df1_day.index, df1_day.total_bill)


# In[188]:


plt.figure(figsize=(7,5))
sns.barplot(data=df1, x='day', y='total_bill', hue='sex')


# In[ ]:


#Heatmap


# In[191]:


df2=sns.load_dataset('flights')
df2


# In[196]:


plt.plot(df2.passengers);


# In[200]:


flights_df = sns.load_dataset('flights').pivot('year','month','passengers')
flights_df


# In[204]:


sns.heatmap(flights_df);
plt.title("No.of Passengers(1000s)");


# In[215]:


sns.heatmap(flights_df,fmt='d',annot=True,cmap='Greens');
plt.title("No.of Passengers(1000s)");


# In[216]:


#Plotting multiple charts 


# In[251]:


fig, axes = plt.subplots(2,3, figsize=(18,10))
axes[0,0].plot(years,oranges,'o--r')
axes[0,0].plot(years,pineapples,'s--b')
axes[0,0].set_title("Yield of Fruits")
axes[0,0].set_xlabel('Years')
axes[0,0].set_ylabel('yield(tons per hectare)')
axes[0,0].legend(['oranges','pineapples'])

axes[0,1].set_title('Sepal_length vs. Sepal_width')
sns.scatterplot(data=df, x='sepal_length', 
                y='sepal_width', hue='species',
                s=100,ax=axes[0,1])

axes[0,2].set_title('Distribution of Sepal_width')
axes[0,2].hist([setosa_df.sepal_width,virginica_df.sepal_width,versicolor_df.sepal_width],
                stacked= True, bins=np.arange(2,5,0.25))

axes[1,0].set_title("Smoking Bills")
sns.barplot(data=df1,x='day',y='total_bill',hue='sex', ax=axes[1,0])

axes[1,1].set_title("No. of Passengers")
sns.heatmap(flights_df,fmt='d',annot=True,cmap='Greens', ax=axes[1,1])

plt.tight_layout(pad=2);


# In[233]:


axes.shape


# In[ ]:





# In[ ]:





# In[ ]:




