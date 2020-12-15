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



@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])

        Present_Price=float(request.form['Present_Price'])

        Kms_Driven=int(request.form['Kms_Driven'])

        Fuel_Type=int(request.form['Fuel_Type'])

        Years=2020-Year

        Seller_Type=int(request.form['Seller_Type'])

        Transmission_Mannual=int(request.form['Transmission'])

        Owner = int(request.form['Owner'])

        prediction=model.predict([[Years,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission_Mannual,Owner]])

        output=round(prediction[0],2)
        
        return render_template('result.html',prediction_texts="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
   

