# Flood Probability Prediction System

A full-stack, data-driven machine learning application that predicts flood probabilities based on environmental, infrastructure, and climate risk factors. The system features a trained machine learning pipeline, a Flask backend API for serving real-time inferences, and an interactive frontend dashboard for users to input environmental metrics and analyze risk levels.

---

## 📁 Project Structure

The repository is organized into four dedicated operational modules:

* **`backend/`**: A Python Flask web server that handles HTTP requests, processes input data parameters, loads the trained serialized model (`model.pkl`), and returns real-time probability scores.
* **`frontend/`**: A lightweight web interface built with HTML5, CSS3, and JavaScript (`Fetch API`) allowing users to interactively tweak metrics and view analytical risk readouts.
* **`ml/`**: The core data science pipeline containing exploratory data analysis notebooks (`Project_2.ipynb`), data scaling profiles, and the model training script (`train_model.py`).
* **`dataset/`**: The local storage directory designated for housing the raw data matrices and target parameters.

---

## 📊 Features & Core Pipeline

### 1. Interactive UI Dashboard

* Allows custom input configurations across major environmental indicators.
* Provides instant, dynamic visual feedback on calculated risk probabilities.

### 2. Machine Learning Engine

* **Exploratory Data Analysis (EDA):** Performs data-profiling, variance distribution mapping, and evaluates multicollinearity via feature-to-target correlation matrices.
* **Feature Scaler Integration:** Standardizes varying geographical and meteorological telemetry indices for stable inference.
* **Serialized Predictive Model:** Implements a validated scikit-learn regression model compiled into a high-performance pickle (`.pkl`) payload.

### 3. RESTful API Endpoints

* Decoupled backend API architecture structured to intake JSON inputs, feed values cleanly to the inference pipeline, and return prediction responses.

---

## 🛠️ Tech Stack & Requirements

* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **Backend Framework:** Python Flask
* **Data Science & Machine Learning:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
* **Model Serialization:** `pickle`

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python 3.x installed on your machine. Install all runtime dependencies by running:

```bash
pip install -r requirements.txt

```

### 2. Dataset Configuration

Due to GitHub file size limits, the raw data matrix is skipped by version tracking rules.

1. Download the raw data asset file from your source provider.
2. Save the file inside the root of the **`dataset/`** directory.
3. Ensure the file is named exactly: `Flood Prediction Dataset.csv`

### 3. Run the Backend Server

Navigate to the backend directory and launch the Flask development engine:

```bash
cd backend
python app.py

```

The server will initialize locally (typically at `http://127.0.0.1:5000`).

### 4. Launch the Frontend

Open the `frontend/index.html` file directly in any modern web browser to begin testing parameters and generating real-time flood risk reports.
