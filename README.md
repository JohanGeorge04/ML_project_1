# Diabetes Prediction — XGBoost + FastAPI

A simple end-to-end project for predicting diabetes risk using an XGBoost model and serving it via FastAPI.  
You can train the model locally, run an API for predictions, test it with a client script, package it using Docker, and deploy it on Render.

---

## 🚀 Project Structure

```
├── diabetes_dataset.csv     # Training data
├── train.py                 # Train and save the model
├── predict.py               # FastAPI prediction API
├── test.py                  # Simple API client (URL can be changed)
├── pyproject.toml           # Dependencies (managed by uv)
├── Dockerfile               # Docker setup for deployment
```

---

## 📌 1. Environment Setup (using uv)

### Initialize the project
```bash
uv init
```

### Add dependencies
```bash
uv add fastapi uvicorn numpy pandas scikit-learn xgboost
```

### (Optional) Activate virtual environment
```bash
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows
```

---

## 📌 2. Train the Model

```bash
uv run train.py
```

This loads `diabetes_dataset.csv`, trains the XGBoost model, and saves it.

---

## 📌 3. Start the FastAPI Server Locally

```bash
uv run uvicorn predict:app --reload
```

Local Swagger documentation will be available at:

```
http://localhost:8000/docs
```

---

## 📌 4. Test the API Locally

```bash
uv run test.py
```

✅ You can change the API URL inside `test.py` if you want to test against the deployed cloud version.

---

# 📦 5. Docker Usage (Local First)

### Build the image
```bash
docker build -t diabetes-api .
```

### Run the container
```bash
docker run -p 8000:8000 diabetes-api
```

---

# 🌐 6. Deploying to Render (Using Docker)

The project is deployed on Render using the included **Dockerfile**.

### Steps:

1. Push your repository to GitHub  
2. On Render → **New Web Service**  
3. Choose **Docker** as the runtime  
4. Render auto-detects your Dockerfile  
5. Set the exposed port to `8000`  
6. Deploy 🚀

---

# ✅ Hosted API (Render)

**Base URL:**  
https://ml-project-1-ie2r.onrender.com

**Swagger UI:**  
https://ml-project-1-ie2r.onrender.com/docs

Use these URLs if you update `test.py` to test the deployed version.

