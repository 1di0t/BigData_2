import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


titanic = sns.load_dataset('titanic')
#add category Unkown
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
#fill NaN with Unknown
titanic['deck'].fillna('Unknown',inplace=True)

#Calculation of survival rates by gender
survived_gender = titanic.groupby(by='sex')['survived'].mean().reset_index()

print(survived_gender)
print(survived_gender.info())

sns.barplot(survived_gender,x="sex",y="survived",color="#ea0060")
plt.title("survival rates by gender")
plt.ylabel("survival rate")
plt.show()
