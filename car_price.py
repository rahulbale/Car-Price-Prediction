import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pickle


df=pd.read_csv('car_data.csv')


final_set=df[[ 'Year', 'Selling_Price', 'Present_Price', 'Kms_Driven','Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]

final_set['Current_Year']=2020

final_set['No_of_total_years']=final_set['Current_Year']-final_set['Year']
final_set.drop(['Year','Current_Year'],axis=1,inplace=True)


def labelencoding(df,variable):
    label=LabelEncoder()
    df[variable]=label.fit_transform(df[variable])

labelencoding(final_set,'Fuel_Type')
labelencoding(final_set,'Seller_Type')
labelencoding(final_set,'Transmission')

X=final_set.iloc[:,1:]
y=final_set.iloc[:,0]


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size =0.2,random_state=0)

rf_para = {
    "n_estimators":[int(x) for x in np.linspace(start=100,stop=1200,num=12)],
    "max_depth":[int(x) for x in np.linspace(start=5,stop=30,num=6)],
    "min_samples_split":[2,5,10,15,20,100],
    "min_samples_leaf":[1,2,5,10,15],
    "max_features":["auto","sqrt"]
}

rf_reg=RandomForestRegressor()

rf_rand=RandomizedSearchCV(estimator=rf_reg,param_distributions=rf_para,cv=6,
                       n_iter=10,scoring='neg_mean_squared_error',random_state=5,n_jobs=1)

rf_rand.fit(X_train,y_train)

filename = 'car_price_modal.pkl'
pickle.dump(rf_rand, open(filename, 'wb'))
