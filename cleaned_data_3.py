# import required librairies
import pandas as pd
import requests
import sqlite3
# import numpy as np


# # pull from API
url = "http://localhost:8080/medish_centrum_randstad/api/netlify?page=1"
page1 = requests.get(url).json()
# create df
page1 = requests.get(url).json()
df = pd.DataFrame(page1['data'])

# # manipulating data.
# remove duplicate rows and inform about the removal
duplicate_rows_df = df[df.duplicated()]
if duplicate_rows_df.shape == (0, 8):
    print ('There are no unexcpected duplicates')
else:
    print ('Unexcpected duplicates have been deleted')
    df=df.drop_duplicates()

# the df will be the old df where we apply changed with a lambda to apply pd.to_numeric where non numbers will be coerced to NaN for those columns were dtype is object.  
df = df.apply(lambda x: pd.to_numeric(x, errors='coerce') if x.dtype == 'object' else x)
# change the dtype to float 64
df = df.apply(lambda x: pd.astype('float64') if x.dtype == 'object' else x)


# add the New Feature BMI (kg/m^2) we do this before the rest of the manipulations 
df['bmi'] = df['mass']/(df['length']/100)**2

## the IQR clipping for outliers 
# Computing IQR
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Clipping the IQR*|15.*IQD|
mean = df.mean()
df = df.clip(lower=mean-1.5*IQR, upper=mean+1.5*IQR, axis=1)

# replace NaN with mean
# Compute the mean of each column and replace NaN values with the mean
df.fillna(df.mean(), inplace=True)

## saving the new df to SQL
dbName = "rest_server/medisch_centrum_randstad/db.sqlite3"
# Connect to SQLite database
dbConnection = sqlite3.connect(dbName)
# save df to SQLlite
df.to_sql('cleaned_data_3', dbConnection, if_exists='replace', index = False)
# close the SQLite database connection
dbConnection.close()