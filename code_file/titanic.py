import seaborn as sns # based on pandas 
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#load titanic dataset
titanic = sns.load_dataset('titanic')
#add category Unkown
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
#fill NaN with Unknown
titanic['deck'].fillna('Unknown',inplace=True)

#fill NaN value to median of age
titanic['age'].fillna(titanic['age'].median(),inplace=True)
#print(titanic.info())

X = titanic[['age']]
y = titanic['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#model construction
model = LogisticRegression()

#model training
model.fit(X_train,y_train)

plt.figure(figsize=(10,6))
plt.scatter(X_test,y_test,color='orange',label='Real')
plt.scatter(X_test,model.predict(X_test),color='green',label='Predicted',alpha=0.3)
plt.title('Logistic Regression Model')
plt.xlabel('Age')
plt.ylabel('Survived')
plt.legend()
plt.show()