# Mile per gallon data

import seaborn as sns # based on pandas 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

mpg = sns.load_dataset('mpg')

mpg.dropna(axis=0,inplace=True)
print(mpg['origin'].value_counts())
