import seaborn as sns
import pandas as pd


titanic = sns.load_dataset('titanic')

# print(titanic.describe())
# print(titanic.info())
# print(titanic.head(10))
# print(titanic.tail(10))
# print(len(titanic))
# print(titanic.shape)

print(titanic['adult_male'])
