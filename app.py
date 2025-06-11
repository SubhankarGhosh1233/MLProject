from flask import Flask,request,render_template,jsonify

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    #print(request.form)  # Debugging: Check received form data
    
    try:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score', 0)),
            writing_score=float(request.form.get('reading_score', 0))
        )
        
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        return jsonify({'prediction': results[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)

