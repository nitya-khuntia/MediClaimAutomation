from flask import Blueprint, request, jsonify
import pandas as pd
import openai
import os

# Initialize the blueprint for Generative AI integration
generative_ai = Blueprint('generative_ai', __name__)

# Configure OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

dataset=pd.read_csv('data/insurance_data_cleaned.csv')

# Assuming 'dataset_context' holds a summary or key information about the dataset
dataset_context = "Summary of the insurance claim dataset including key trends and outliers. {dataset}"

@generative_ai.route('/generate_explanation', methods=['POST'])
def generate_explanation():
    try:
        # Fetch the data from the request (ensure it's a JSON request)
        data = request.get_json()
        
        # Combine dataset context with the specific prediction details
        prompt = f"""Explain this insurance claim prediction with accurate reasons based on your understanding
          of the data being provided to you, in a simple and short way to a layman. Actually a ML model is
            trained on the dataset to generate the prediction
           and the prediction will be provided to you. In this prompt the summary of dataset is provided to you 
            in form of {dataset_context}.Prediction will be provided as : {data['prediction']}.
            """

        # If the user provides a custom prompt, append it
        if 'custom_prompt' in data:
            prompt += " " + data['custom_prompt']

        # Send the request to OpenAI's GPT-3
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Choose the appropriate engine (like "davinci" or others)
            messages=[{"role": "user", "content":prompt}]
            # stream=True
        )

        # Return the generated explanation
        return jsonify({
            'explanation': response.choices[0].message.content.strip()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle unexpected errors
