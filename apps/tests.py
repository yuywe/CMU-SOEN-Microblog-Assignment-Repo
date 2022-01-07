from unittest import TestCase
import joblib
from flask import Flask, jsonify, g
import requests
import pandas as pd
import numpy as np
import requests

app = Flask(__name__)

# run by running the docker build command
class ModelTest(TestCase):
    def test_model_returns_one(self):
        clf = joblib.load('apps/model.pkl')
        # TODO: replace FEATURE_NAME with the name of a feature and FEATURE_VALUE with the value that corresponds with that feature.
        # You should add as many entries in the dictionary as there are features in your model
        query_df = pd.DataFrame({'FEATURE_NAME': pd.Series(FEATURE_VALUE),})
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        self.assertEqual(prediction, 1)
    
    def test_request_returns_one(self):
        # TODO: replace FEATURE_NAME with the name of a feature and FEATURE_VALUE with the value that corresponds with that feature.
        # You should add as many url parameters as there are features in your model
        r = requests.get("http://localhost:5000/predict?FEATURE_NAME=FEATURE_VALUE")
        self.assertEqual(r.json(), 1)
