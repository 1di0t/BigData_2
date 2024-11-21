# Mile per gallon data

import pandas as pd
import seaborn as sns # based on pandas 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)
#score increase and mse decrease with random_state=45

#model construction and training
model = LinearRegression()
model.fit(X_train,y_train)

#model prediction
y_pred = model.predict(X_test)

#model evaluation
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print("===============================================")
print(f"R2_Score Error : {r2}")
print("===============================================")
print(f"Mean Squared Error : {mse}")
print("===============================================")


#visualization
plt.figure(figsize=(10,6))
plt.scatter(y_test,y_pred,color='orange',alpha=0.7)
plt.plot([y.min(),y.max()],[y.min(),y.max()],color='blue')
plt.title('Linear Regression Model')
plt.xlabel('Real')
plt.ylabel('Predicted')
plt.show()

