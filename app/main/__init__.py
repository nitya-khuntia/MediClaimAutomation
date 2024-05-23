from flask import request, jsonify, Blueprint
import pandas as pd
import joblib


# Define the main blueprint
main = Blueprint('main', __name__)

# Health check endpoint
@main.route('/', methods=['GET'])
def home():
    return "Welcome to the Insurance Claim Prediction API!"  # Basic response for a GET request

# Load the trained pipeline
pipeline_path = 'model/insurance_claim_pipeline.joblib'  # Ensure the correct path
pipeline = joblib.load(pipeline_path)


# Prediction endpoint
@main.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract and validate input data
        data = request.get_json(force=True)  # Parse JSON from the POST request
        # Add 'claim' to the expected features
        expected_features = ['age', 'bmi', 'bloodpressure', 'children', 'gender', 'diabetic', 'smoker', 'region', 'claim']
        if not all(feature in data for feature in expected_features):
            return jsonify({"error": "Missing required features for prediction."}), 400  # Handle missing features

        # Convert to DataFrame and make predictions
        data_df = pd.DataFrame([data])  # Ensure proper data structure
        prediction = pipeline.predict(data_df)  # Make the prediction

        # Send the prediction result
        response = {'prediction': prediction[0]}  # Return the first prediction
        return jsonify(response)
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500