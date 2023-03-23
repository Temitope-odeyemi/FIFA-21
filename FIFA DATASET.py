#!/usr/bin/env python
# coding: utf-8

# In[36]:


#importing neccssary libries needed

import pandas as pd
import numpy as np


# ### Variable Description

# Here is a brief documentation for each column name in the given dataset:
# 
# - photoUrl: The URL of the player's photo.
# - LongName: The full name of the player.
# - playerUrl: The URL of the player's page on sofifa.com.
# - Nationality: The nationality of the player.
# - Positions: The positions the player can play.
# - Name: The short name of the player.
# - Age: The age of the player.
# - OVA: The overall rating of the player in FIFA 21.
# - POT: The potential rating of the player in FIFA 21.
# - Team & Contract: The team the player is playing for in FIFA 21, along with their contract details.
# - ID: The unique identifier for the player.
# - Height: The height of the player in feet and inches.
# - Weight: The weight of the player in pounds.
# - foot: The preferred foot of the player.
# - BOV: The best overall rating the player has achieved in their career.
# - BP: The best position the player has played in their career.
# - Growth: The difference between the potential rating and overall rating of the player.
# - Joined: The date the player joined their current team in FIFA 21.
# - Loan Date End: The date the player's loan contract ends.
# - Value: The market value of the player in FIFA 21.
# - Wage: The weekly wage of the player in FIFA 21.
# - Release Clause: The release clause value of the player in FIFA 21.
# - Attacking: The attacking attributes of the player.
# - Crossing: The crossing attribute of the player.
# - Finishing: The finishing attribute of the player.
# - Heading Accuracy: The heading accuracy attribute of the player.
# - Short Passing: The short passing attribute of the player.
# - Volleys: The volleys attribute of the player.
# - Skill: The skill attributes of the player.
# - Dribbling: The dribbling attribute of the player.
# - Curve: The curve attribute of the player.
# - FK Accuracy: The free kick accuracy attribute of the player.
# - Long Passing: The long passing attribute of the player.
# - Ball Control: The ball control attribute of the player.
# - Movement: The movement attributes of the player.
# - Acceleration: The acceleration attribute of the player.
# - Sprint Speed: The sprint speed attribute of the player.
# - Agility: The agility attribute of the player.
# - Reactions: The reactions attribute of the player.
# - Balance: The balance attribute of the player.
# - Power: The power attributes of the player.
# - Shot Power: The shot power attribute of the player.
# - Jumping: The jumping attribute of the player.
# - Stamina: The stamina attribute of the player.
# - Strength: The strength attribute of the player.
# - Long Shots: The long shots attribute of the player.
# - Mentality: The mentality attributes of the player.
# - Aggression: The aggression attribute of the player.
# - Interceptions: The interceptions attribute of the player.
# - Positioning: The positioning attribute of the player.
# - Vision: The vision attribute of the player.
# - Penalties: The penalties attribute of the player.
# - Composure: The composure attribute of the player.
# - Defending: The defending attributes of the player.
# - Marking: The marking attribute of the player.
# - Standing Tackle: The standing tackle attribute of the player.
# - Sliding Tackle: The sliding tackle attribute of the player.
# - Goalkeeping: The goalkeeping attributes of the player.
# - GK Diving: The goalkeeper diving attribute of the player.
# - GK Handling: The goalkeeper handling attribute of the player.
# - GK Kicking: The goalkeeper kicking attribute of the player.
# - GK Positioning: The goalkeeper positioning attribute of the player.
# - GK Reflexes: This refers to the goalkeeper's ability to react and make saves quickly.
# - Total Stats: This refers to the overall rating of the player based on their performance in all areas of the game.
# - Base Stats: This refers to the player's rating in the six main areas of the game: Pace, Shooting, Passing, Dribbling, Defending, and Physicality.
# - W/F: This refers to the player's weaker foot ability.
# - SM: This refers to the player's skill moves ability.
# - A/W: This refers to the player's attacking work rate. It measures how frequently the player participates in attacking actions, such as making runs or positioning themselves in the opponent's half.
# - D/W: This refers to the player's defensive work rate. It measures how frequently the player participates in defensive actions, such as tracking back or making tackles.
# - IR: This refers to the player's injury resistance. It measures the player's ability to avoid injuries and how quickly they recover from them.
# - PAC: This refers to the player's pace or speed attribute. It measures how quickly the player can move with and without the ball.
# - SHO: This refers to the player's shooting ability. It measures the player's accuracy and power when shooting the ball.
# - PAS: This refers to the player's passing ability. It measures the player's accuracy and range when passing the ball.
# - DRI: This refers to the player's dribbling ability. It measures the player's agility, balance, and ball control when dribbling the ball.
# - DEF: This refers to the player's defensive ability. It measures the player's ability to tackle, intercept, and defend against opposing players.
# - PHY: This refers to the player's physicality or strength. It measures the player's ability to win physical battles and maintain possession of the ball.
# - Hits: This refers to the number of times the player's profile has been viewed on the website.

# In[37]:


#to display the entire column
pd.set_option('display.max_columns', None)

#To read the dataset in a dataframe using pandas 
df = pd.read_csv('fifa21.csv', low_memory=False)


# In[38]:


#To see number or rows and columns in the df
df.shape


# In[39]:


#To check column index names
df.columns


# In[40]:


#To check for information of each columns
df.info()


# # DATA CLEANING

# There are two types of data issues that need to be assessed when trying to clean a dataset
# 
# - Data Quality Issues: Also called dirty data, these are data that has issues with data content (e.g: duplicate rows, null values)
# - Data Tidiness Issues: Also called messy data, these are data that has issues with the data structure (e.g: the columns and rows)
# In this datasets, the cleaning done are;
# 
# 1. Fixing the /n and 1. in club column
# 2. Checking and filling of null values
# 3. Checking for duplicates
# 4. Changing datatypes
# 5. Removing euro sign, K and M in some columns
# 6. Dropping columns that would not be used

# ### Checking for duplicates

# In[41]:


df[df.duplicated()]


# Since there are no duplicate rows, we can move on.

# ### Dropping columns that won't be needed

# In[42]:


df.drop(columns=['ID', 'LongName', 'photoUrl', 'playerUrl'], axis=1, inplace =True)


# ### Replacing /n string in the club column

# In[43]:


df['Club']= df['Club'].str.replace('\n\n\n\n', '') #Removing the \n in front of the column
df['Club'] = df['Club'].str.lstrip('1. ') #Removing the 1. count in front of the column


# ### Removing the ★ in W/F, SM and IR column

# In[44]:


# Using a def function to remove the star

def remove_star(x):
    x = x.replace('★', '')
    return x

#Use the function on the affected columns
df['IR'] = df['IR'].apply(remove_star)
df['SM'] = df['SM'].apply(remove_star)
df['W/F'] = df['W/F'].apply(remove_star)


# ### Cleaning Hit column

# In[45]:


# Checking to see the number of null values

df['Hits'].isnull().sum()


# In[46]:


# Filling the null values with 0
df['Hits']= df['Hits'].fillna(0)


# In[47]:


# Creating a function that will remove 'K' and convert it to thousand (1000) and integers
def hit_cleaning(val):
    if 'K' in str(val):
        val=val.replace('K', '')
        return int(float(val)*1000)
    else:
        return int(val)


# In[48]:


# Applying the change to the column
df['Hits'] = df['Hits'].apply(hit_cleaning)


# ### Converting Joined column to a datatime dtype, then creating a month column

# In[49]:


df['Joined'] = pd.to_datetime(df['Joined'])


# In[50]:


df['Joined Month'] = df['Joined'].dt.month_name()


# ### Renaming OVA column by removing ↓ from the column name

# In[51]:


df.rename(columns = {'↓OVA': 'OVA'}, inplace = True)


# ### Changing Preferred Foot, A/W and D/W column to catergory intead of object

# In[52]:


df['Preferred Foot'] = df['Preferred Foot'].astype('category')
df['A/W'] = df['A/W'].astype('category')
df['D/W'] = df['D/W'].astype('category')


# ### Cleaning the Weight column
# 

# In[53]:


df['Weight'].unique()


# In[54]:


#Using a def function to remove the rows that are not in kg

def weight_kg(x):
    if 'lbs' in x:
        x = x.replace('lbs', '')
        x = float(x) * 0.45359237
        x = int(x)
        return x
    else:
        return int(x[:-2])


# In[55]:


#Applying the function to the column

df['Weight'] = df['Weight'].apply(weight_kg)


# ### Cleaning Wage, Value and Release Clause columns
# 

# In[56]:


#Using a def function to remove the euro sign, 'K' which means thousand and 'M' which means millions and converting the columns to a float

def convert(x):
    x= x.replace('€', '') # Remove the currency sign in front of the digit
    if x[-1] == 'K': #Checking if the last digit in the column ends with K
        return float(x[:-1]) * 1000 #Remove the last digit, convert to float, then multiply by 1000
    elif x[-1] == 'M': #Checking if the last digit in the column ends with M
        return float(x[:-1]) * 1000000 #Remove the last digit, convert to float, then multiply by 1000000
    else:
        return float(x) #If cells does not start or end with €, K and M, then convert to float


# In[57]:


df['Value'] = df['Value'].apply(convert)
df['Wage'] = df['Wage'].apply(convert)
df['Release Clause'] = df['Release Clause'].apply(convert)


# ### Cleaning the Height column
# 

# In[58]:


df['Height'].unique()


# #### The height column are in cm and inches

# In[59]:


# Changing the entire column to feet using a def function

def feet(x):
    if x.endswith('cm'): #If unit ends with cm
        x = int(x[:-2]) # change cells ending with cm to an integer
        x = x / 30.48 # change it to feet
    else:
        x = x.strip('"').split("'") # change unit in inches to feet
        x = float(x[0]) + float(x[1])/12
    return x


# In[60]:


df['Height'] = df['Height'].apply(feet)


# In[61]:


df['Contract']


# In[62]:


# Creating another Contract column 
df['Contract Status'] = df['Contract']


# In[63]:


# Using a def function to show the status of the player
def status(x):
    if 'On Loan' in x:
        x = 'Loan'
        return x
    elif '2' in x:
        x = 'Active'
        return x
    else:
        x = 'Free'
        return x


# In[64]:


df['Contract Status'] = df['Contract Status'].apply(status) #Apply the def function to the contract status column


# In[65]:


df['Contract Status'] = df['Contract Status'].astype('category') # changing the contract status column to category


# ### Cleaning Loan Date End Column

# In[66]:


# Since it was found out from df.info above that there are null values in this column, lets find out how many it is
df['Loan Date End'].isnull().sum()


# In[67]:


# Filling the 17966 cells empty cells with 
df['Loan Date End'].fillna('Signed', inplace=True)


# ### Preveiwing the cleaned FIFA'21 dataset

# In[68]:


df.head(10)


# ### Saving the cleaned file in a csv file

# In[72]:


df.to_csv('FIFA21 CLEANED DATA', index=False)

