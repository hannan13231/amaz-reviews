import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import CountVectorizer
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
count_vector = pickle.load(open('count_vector.pkl', 'rb'))

@app.route('/')
def view():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/sentiment')
def sentiment():
    return render_template('form.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['text']
    rating = int(request.form['rating'])
    review = str(review)
    text = count_vector.transform([review])
    
    output = model.predict(text)
    
    if (output == 1 and rating >= 3):
        res_val = "Positive"
    elif (output == 0 and rating <= 3):
        res_val = "Negative"
    else:
        res_val = "Rating which does not match with"

    return render_template('form.html', prediction_text='Customer has given a {} review'.format(res_val))

if __name__ == "__main__":
    app.run()