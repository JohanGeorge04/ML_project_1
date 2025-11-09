Diabetes Prediction — XGBoost + FastAPI

A simple end-to-end project for predicting diabetes risk using an XGBoost model and serving it via FastAPI.
You can train the model locally, run an API for predictions, test it with a client script, and optionally deploy using Docker.

🚀 Project Structure
├── diabetes_dataset.csv     # Training data
├── train.py                 # Train and save the model
├── predict.py               # FastAPI prediction API
├── test.py                  # Simple API client
├── pyproject.toml           # Dependencies (managed by uv)
├── Dockerfile               # Docker setup

📌 1. Environment Setup (using uv)
Initialize the project
uv init

Add dependencies
uv add fastapi uvicorn numpy pandas scikit-learn xgboost

(Optional) Activate virtual environment
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows

📌 2. Train the Model

Run the training script:

uv run train.py


This loads diabetes_dataset.csv, trains the XGBoost model, and saves the output model file.

📌 3. Start the FastAPI Server
uv run uvicorn predict:app --reload


API Endpoints:

Root: http://localhost:8000/

Swagger Docs: http://localhost:8000/docs

📌 4. Test the API
uv run test.py


The test script sends a sample input to the API and prints the prediction response.

📦 5. Docker Usage
Build
docker build -t diabetes-api .

Run
docker run -p 8000:8000 diabetes-api
