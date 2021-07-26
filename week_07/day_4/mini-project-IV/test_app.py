import pickle
# import numpy as np
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# create Flask object
app = Flask(__name__)

model = None

def load_model():
    global model
    # model variable refers to the global variable
    with open('model.sav', 'rb') as f:
        model = pickle.load(f)

# create home endpoint
@app.route('/')
def home_endpoint():
    return 'Use /predict to predict the outcome'

# create predict endpoint
@app.route('/predict', methods=['POST'])
def get_prediction():
    # works only for a single sample
    if request.method == 'POST':
        query = request.get_json() # get data posted as json
        data = pd.json_normalize(query)
        prediction = model.predict(data) # runs globally loaded model on the data
    return str(prediction[0])

# declare the main function
if __name__ == '__main__':
    load_model() # load model at the beginning once only
    app.run(port=5000, debug=True)