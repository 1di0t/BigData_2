# Mile per gallon data

import pandas as pd
import seaborn as sns # based on pandas 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#load mpg dataset
mpg = sns.load_dataset('mpg')


#drop rows with NaN values
mpg.dropna(axis=0,inplace=True)
#drop name column
mpg.drop(columns=['name'],inplace=True)


#print(mpg['origin'].value_counts())


#one hot encoding for origin column
mpg= pd.get_dummies(mpg,columns=['origin'],drop_first=True)

#print(mpg.head(20))


#split data
X = mpg.drop(columns=['mpg'],axis=1)
y = mpg['mpg']

