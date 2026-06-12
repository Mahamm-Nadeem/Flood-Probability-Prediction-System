# Flood Probability Prediction System

A machine learning repository dedicated to analyzing environmental, geographical, and infrastructural risk factors to predict flood probabilities. This project implements a full data science pipeline—ranging from exploratory data analysis (EDA) and rigorous statistical checks to feature engineering and predictive model evaluation.

## Dataset & Features

The system evaluates a comprehensive matrix of macro and micro environmental features to establish risk probabilities:

* **Climate & Weather:** Precipitation, Monsoon Intensity, El Niño Effects.
* **Geographical Factors:** Topography Drainage, River Management, Coastal Vulnerability, Watersheds.
* **Land & Infrastructure:** Deforestation, Urbanization, Agricultural Practices, Dams Quality, Siltation.
* **Socio-Economic & Policy Factors:** Landslides, Ineffective Disaster Preparedness, Drainage Systems, Encroachments, Political Factors.

---

## 🛠️ Project Pipeline

### 1. Exploratory Data Analysis (EDA)

* **Statistical Profiling:** Evaluation of dataset shapes, central tendencies, and missing value checks.
* **Distribution Analysis:** Visualization of feature distributions to detect skewness and variance.
* **Correlation Matrix:** Large-scale heatmaps analyzing multicollinearity and structural relationships between target variables and environmental indices.

### 2. Data Preprocessing & Validation

* **Feature Scaling:** Standardization/Normalization of highly varying scales across geographical and meteorological metrics.
* **Data Splitting:** Clean partitioning into training and testing segments to validate generalized predictive accuracy and prevent overfitting.

### 3. Machine Learning Modeling

* **Regression Pipeline:** Training models to predict continuous probability scores (`FloodProbability`).
* **Performance Evaluation:** Rigorous benchmarking using standard data science metrics:
* **Mean Squared Error (MSE)** & **Root Mean Squared Error (RMSE)** to measure residual variance.
* **R-squared ($R^2$) Score** to calculate the proportion of variance explained by the environmental features.



---

## 💻 Tech Stack

* **Environment:** Jupyter Notebook / Python 3
* **Data Manipulation:** `pandas`, `numpy`
* **Visualization:** `matplotlib`, `seaborn`
* **Machine Learning:** `scikit-learn`

---

## 🚀 Getting Started

### Prerequisites

Make sure you have a Python environment set up with the required libraries. You can install them via pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter

```

### Running the Notebook

1. Clone this repository locally.
2. Ensure your dataset file is placed in the designated directory referenced inside the notebook.
3. Launch Jupyter Notebook or JupyterLab:
```bash
jupyter notebook

```


4. Open `Flood Probability Prediction System 1.ipynb` and execute the cells sequentially to reproduce the analysis, visualizations, and model metrics.
