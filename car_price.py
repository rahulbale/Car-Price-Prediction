import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,RandomizedSearchCV
from sklearn.linear_model import LinearRegression
import joblib

df=pd.read_csv('car_data.csv')


final_set=df[[ 'Year', 'Selling_Price', 'Present_Price', 'Kms_Driven','Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]

final_set['Current_Year']=2020

final_set['No_of_total_years']=final_set['Current_Year']-final_set['Year']
final_set.drop(['Year','Current_Year'],axis=1,inplace=True)


final_set=pd.get_dummies(final_set,drop_first=True)

X=final_set.iloc[:,1:]
y=final_set.iloc[:,0]


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size =0.2,random_state=0)


lin=LinearRegression()

lin.fit(X_train,y_train)

filename = 'car_price_modal'
joblib.dump(lin,filename)
