# import necessary libraries:
import pandas as pd
import joblib
from flask import Flask, request,jsonify

#Creat local api using Flask:

app = Flask(__name__)

load_model = joblib.load('price_prediction_model.sav', mmap_mode ='r')

@app.route('/api',methods=['POST'])
def price_prediction():
    data = request.form
    df = pd.DataFrame([data])
    preds = load_model.predict(df)
    return jsonify({'prediction': preds[0]})

if __name__ == '__main__':
    app.run(port=5000)