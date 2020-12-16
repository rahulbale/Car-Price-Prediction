from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
import sklearn
import joblib

app = Flask(__name__,template_folder="template",static_folder="static")

model = joblib.load('cars_price_modal')

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')


"""
@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])

        Present_Price=float(request.form['Present_Price'])

        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven2=np.log(Kms_Driven)
        Fuel_Type=int(request.form['Fuel_Type'])

        Year=2020-Year

        Seller_Type=int(request.form['Seller_Type'])

        Transmission_Mannual=int(request.form['Transmission'])

        Owner = int(request.form['Owner'])

        prediction=model.predict([[Year,Present_Price,Kms_Driven2,Fuel_Type,Seller_Type,Transmission_Mannual,Owner]])

        output=round(prediction[0],2)
        
        return render_template('result.html',prediction_texts="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
   
"""
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven2=np.log(Kms_Driven)
        Owner=int(request.form['Owner'])
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
        elif(Fuel_Type_Petrol=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1        
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
        Year=2020-Year
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
        
        output=round(prediction[0],2)
        
        if output<0:
            return render_template('result.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('result.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
