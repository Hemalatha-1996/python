# %% [markdown]
# ## EDA And Feature Engineering Flight Price Prediction
# check the dataset info below
# https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction

# %% [markdown]
# ### FEATURES
# The various features of the cleaned dataset are explained below:
# 1) Airline: The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.
# 2) Flight: Flight stores information regarding the plane's flight code. It is a categorical feature.
# 3) Source City: City from which the flight takes off. It is a categorical feature having 6 unique cities.
# 4) Departure Time: This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.
# 5) Stops: A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.
# 6) Arrival Time: This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.
# 7) Destination City: City where the flight will land. It is a categorical feature having 6 unique cities.
# 8) Class: A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.
# 9) Duration: A continuous feature that displays the overall amount of time it takes to travel between cities in hours.
# 10)Days Left: This is a derived characteristic that is calculated by subtracting the trip date by the booking date.
# 11) Price: Target variable stores information of the ticket price.

# %%
#importing basics libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# %%
df=pd.read_excel('flight_price.xlsx')
df.head()

# %%
df.tail()

# %%
## get the basics info about data
df.info()

# %%
df.describe()

# %%
df.head()

# %%
## Feature Engineering
df['Date']=df['Date_of_Journey'].str.split('/').str[0]
df['Month']=df['Date_of_Journey'].str.split('/').str[1]
df['Year']=df['Date_of_Journey'].str.split('/').str[2]

# %%
df.info()

# %%
df['Date']=df['Date'].astype(int)
df['Month']=df['Month'].astype(int)
df['Year']=df['Year'].astype(int)

# %%
df.info()

# %%
## Drop Date Of Journey

df.drop('Date_of_Journey',axis=1,inplace=True)

# %%
df.head()

# %%
df['Arrival_Time']=df['Arrival_Time'].apply(lambda x:x.split(' ')[0])

# %%
df['Arrival_hour']=df['Arrival_Time'].str.split(':').str[0]
df['Arrival_min']=df['Arrival_Time'].str.split(':').str[1]

# %%
df.head(2)

# %%
df['Arrival_hour']=df['Arrival_hour'].astype(int)
df['Arrival_min']=df['Arrival_min'].astype(int)

# %%
df.drop('Arrival_Time',axis=1,inplace=True)

# %%
df.head(2)

# %%
df['Departure_hour']=df['Dep_Time'].str.split(':').str[0]
df['Departure_min']=df['Dep_Time'].str.split(':').str[1]

# %%
df['Departure_hour']=df['Departure_hour'].astype(int)
df['Departure_min']=df['Departure_min'].astype(int)

# %%
df.info()

# %%
df.drop('Dep_Time',axis=1,inplace=True)

# %%
df.head(2)

# %%
df['Total_Stops'].unique()

# %%
df[df['Total_Stops'].isnull()]

# %%
df['Total_Stops'].mode()

# %%
df['Total_Stops'].unique()

# %%
df['Total_Stops']=df['Total_Stops'].map({'non-stop':0,'1 stop':1,'2 stops':2,'3 stops':3,'4 stops':4,np.nan:1})

# %%
df[df['Total_Stops'].isnull()]

# %%
df.head(2)

# %%
df.drop('Route',axis=1,inplace=True)

# %%
df.head(2)

# %%
df['Duration'].str.split(' ').str[0].str.split('h').str[0]

# %%
df['Airline'].unique()

# %%
df['Source'].unique()

# %%
df['Additional_Info'].unique()

# %%
from sklearn.preprocessing import OneHotEncoder

# %%
encoder=OneHotEncoder()

# %%
encoder.fit_transform(df[['Airline','Source','Destination']]).toarray()

# %%
pd.DataFrame(encoder.fit_transform(df[['Airline','Source','Destination']]).toarray(),columns=encoder.get_feature_names_out())

# %%


# %%


# %%


# %%


# %%


# %%



