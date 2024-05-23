# MediClaimAutomation

A Flask application designed to automate parts of the medical claim process. The application features authentication system,ensuring secure access and data protection. It integrates a machine learning (ML) model trained on historical insurance claim data to predict outcomes .  
MediClaimAutomation utilizes a large language model (LLM) to generate clear, understandable explanations of the ML model's predictions. 

This project includes Flask routes for handling API requests, JWT (JSON Web Token) for secure authentication, and joblib for managing ML model operations. Additionally, the application logs important events and errors, facilitating troubleshooting and monitoring of system performance.

## Project Structure
This section outlines the directory layout of the MediClaimAI project, providing an overview of where specific parts of the application are located.

MediClaimAI/
│
├── app/ # Main application folder
│ ├── init.py # Initializes the Flask app
│ ├── main/ # Handles core functionalities like predictions
│ │ ├── init.py # Contains prediction routes and logic
│ ├── auth/ # Manages user authentication
│ │ ├── init.py # Setup for authentication routes and JWT configuration
│ ├── generative_ai/ # For generative AI functionalities
│ │ ├── init.py # Code to integrate and handle LLM for explanations
│
├── data/ # Folder for datasets
│ ├── insurance_data_cleaned.csv # Cleaned dataset for training and predictions
│
├── models/ # For storing ML model files
│ ├── insurance_claim_pipeline.joblib # Pipeline model file
│
├── logs/ # For logging application events
│ ├── application.log # Log file for the Flask application
│
├── scripts/ # code for doing data science stuff, bulding and training the model
│ ├── claim.py # Script related bulding and training the model
│
├── requirements.txt # Python dependencies for the project
├── run.py # Entry point for the Flask application
└── README.md # Project overview, setup instructions, and usage


### Explanation of Key Components

- **`app/`**: Contains all Flask application modules including initialization, main functionalities, authentication, and generative AI integrations.
- **`data/`**: Stores datasets used for training and predictions.
- **`models/`**: Contains serialized machine learning models.
- **`logs/`**: Stores application log files.
- **`scripts/`**: Includes additional Python scripts for various tasks such as data preprocessing or model development.
- **`requirements.txt`**: Lists all necessary Python packages for setting up the project environment.
- **`run.py`**: The script used to start the Flask application server.
- **`README.md`**: Provides detailed information about the project, including setup, usage, and documentation.

