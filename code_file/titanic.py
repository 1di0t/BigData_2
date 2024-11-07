import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


titanic = sns.load_dataset('titanic')
#add category Unkown
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
#fill NaN with Unknown
titanic['deck'].fillna('Unknown',inplace=True)

#Removal of missing values
titanic.dropna(subset=['age'],axis=0,inplace=True)
print(titanic.info())


#Calculation of survival rates by age
titanic['age'] = titanic['age'].astype(float)

sns.histplot(data=titanic,x='age',weights='survived',bins=8,color="#ea0060")
plt.ylabel("survival rate")
plt.show()
