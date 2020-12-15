from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__,template_folder="template",static_folder="static")

#model = joblib.load('cars_price_modal.pkl')

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

"""
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven2=np.log(Kms_Driven)
        Fuel_Type=int(request.form['Fuel_Type_Petrol'])
        Year=2020-Year
        Seller_Type=int(request.form['Seller_Type_Individual'])
        Transmission_Mannual=int(request.form['Transmission_Mannual'])
        Owner = int(request.form['Owner'])

        prediction=model.predict([[Year,Present_Price,Kms_Driven2,Fuel_Type,Seller_Type,Transmission_Mannual,Owner]])

        output=round(prediction[0],2)

        if output<0:
            return render_template('result.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('result.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')
"""

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load("C:/Users/Bale/PycharmProjects/Car-Price/cars_price_modal.pkl")
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==7):
            result = ValuePredictor(to_predict_list,7)
            if result<0:
                return render_template('result.html',prediction_texts="Sorry you cannot sell this car")
            else:
                return render_template('result.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')  

if __name__ == "__main__":
    app.run(debug=True)
