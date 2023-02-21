# import necessary libraries:
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Open the data file and make sure that there is no missing data:
df = pd.read_csv('input.csv')
df.isnull().any()

#change categorical data to numeric data:
df = pd.get_dummies(df, columns=['province' , 'building_condition', 'building_type','kitchen_type','heating_type'],drop_first=True)


#Define Variables:
x = df.drop(['price'], axis=1)
y = df['price']

#Split the dataset:
x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=41, test_size=0.2)

#Load and fit the model:
ml = LinearRegression()
ml.fit(x_train, y_train)

#Test the model:
y_prediction = ml.predict(x_test)
ml.score(x_test, y_test)

#Plot model:
plt.scatter(y_prediction , y_test, color = 'red')
