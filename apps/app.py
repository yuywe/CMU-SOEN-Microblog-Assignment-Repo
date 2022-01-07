from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
     clf = joblib.load('apps/model.pkl')
	 # Add features to the predictor based on the model features you have chosen
     # TODO: eplace FEATURE_NAME with the name of the feature
     # You should add a variable for each feature in the microblog
     FEATURE_NAME = int(request.args.get('FEATURE_NAME'))

     # Add your features to the query by replacing FEATURE_NAME with your features
     # You should add all your features to this dataframe following the pattern given
     query_df = pd.DataFrame({'FEATURE_NAME': pd.Series(FEATURE_NAME),})
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)