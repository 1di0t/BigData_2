import seaborn as sns
import pandas as pd


titanic = sns.load_dataset('titanic')

print(f"기본 버전: {titanic['deck']}")
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
print(f"카테고리 추가 버전: {titanic['deck']}")
titanic['deck'].fillna('Unknown',inplace=True)
print(f"언노운 재배치 버전: {titanic['deck']}")

print(titanic.info())