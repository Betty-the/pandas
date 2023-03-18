#!/usr/bin/env python
# coding: utf-8

# In[12]:


#import pandas as pd


# In[3]:


# create a list of names of 5 students
names = ['Betty', 'Gertrude', 'Beatrice', 'Caleb', 'Philemon']


# In[4]:


# create a DataFrame using the list of names
students = pd.DataFrame(names, columns=['Name'])


# In[5]:


print(students)


# In[ ]:


import pandas as pd


# In[33]:


# List of team names
teams_list = ["Hearts of Oak", "Asante Kotoko", "Ebusua Dwarfs", "Sekondi Hassacas", "Okwahu United", "Tano Bofoakwa", "BA United"]


# In[ ]:


#Create a dictionary to store data
data = {}
for team in teams_list:
    data[team] = [12, 8, 9, 7, 10]


# In[ ]:


#Create the DataFrame
teams = pd.DataFrame(data)


# In[ ]:


#Rename the index column to "Match"
teaams.index.name = "Match"


# In[32]:


#Print the DataFrame
print(teams)


# In[13]:


import pandas as pd

# Create a dictionary of West African countries
west_africa_dict = {
    'Country': ['Nigeria', 'Ghana', 'Ivory Coast', 'Senegal', 'Mali'],
    'Capital': ['Abuja', 'Accra', 'Yamoussoukro', 'Dakar', 'Bamako'],
    'Population': [200963599, 31072940, 26378274, 16296364, 20250833]
}

# Create a DataFrame from the dictionary
countries = pd.DataFrame(west_africa_dict)

# Print the DataFrame
print(countries)


# In[15]:


import pandas as pd


# In[16]:


# Create a list of dictionaries with the data
data = [
    {'Rank': 1, 'Team': 'Hearts of Oak', 'Points': 120, 'Wins': 35, 'Draws': 80},
    {'Rank': 2, 'Team': 'Asante Kotoko', 'Points': 90, 'Wins': 55, 'Draws': 60},
    {'Rank': 3, 'Team': 'Ebusua Dwarfs', 'Points': 90, 'Wins': 60, 'Draws': 60},
    {'Rank': 4, 'Team': 'Sekondi Hassacas', 'Points': 80, 'Wins': 43, 'Draws': 55},
    {'Rank': 5, 'Team': 'Okwahu United', 'Points': 78, 'Wins': 39, 'Draws': 53},
    {'Rank': 6, 'Team': 'Tano Bofoakwa', 'Points': 70, 'Wins': 50, 'Draws': 49},
    {'Rank': 7, 'Team': 'BA United', 'Points': 71, 'Wins': 55, 'Draws': 44}
]


# In[ ]:


# Create a DataFrame from the data
df = pd.DataFrame(data)


# In[ ]:


# Print the DataFrame


# In[17]:


print(df)


# In[18]:


# Print the team name along with goals for, goals against, and points
for index, row in df.iterrows():
    team = row['Team']
    gf = row['Wins']
    ga = row['Draws']
    pts = row['Points']
    print(f"{team}: GF={gf}, GA={ga}, PTS={pts}")


# In[30]:


print("Teams that considered more than 30 goals:")
for team in data:
    if team["GA"] > 30:
        print(team["Team"])


# In[28]:


print("Teams that had less than 80 goals:")
for team in data:
    if team["GF"] < 80:
        print(team["Team"])
        


# In[29]:


print("Teams that had less than 60 goals:")
for team in data:
    if team["PTS"] < 60:
        print(team["Team"])

