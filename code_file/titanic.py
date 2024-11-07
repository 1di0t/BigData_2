import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


titanic = sns.load_dataset('titanic')
#add category Unkown
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
#fill NaN with Unknown
titanic['deck'].fillna('Unknown',inplace=True)

print(titanic["survived"].value_counts())

#visualization survived count
sns.countplot(data=titanic,x='survived')
plt.title("Survied (0 = No, 1 = Yes)")
plt.xlabel("Survied")
plt.ylabel("Count")
plt.show()