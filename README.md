# 💳 Online Payment Fraud Detection App

## 📌 Overview
This project is a **machine learning-powered fraud detection system** designed to identify fraudulent online payment transactions in real-time.

It demonstrates an **end-to-end data science workflow** — from data cleaning and feature engineering to model building and deployment using Streamlit.

The primary objective is to **minimize financial risk** by accurately detecting fraud while maintaining a simple and interactive user experience.

---

## 🚀 Key Features
- 🔍 Real-time fraud detection
- 📊 Engineered features to capture suspicious behavior
- ⚡ Random Forest model for stable performance
- 🖥️ Interactive Streamlit web application
- 📈 Fraud probability displayed as percentage
- ✅ Clear classification: Fraudulent or Legitimate

---

## 🧠 Machine Learning Approach

### 1. Data Preprocessing
- Removed irrelevant columns:
  - `nameOrig`, `nameDest`, `step`, `isFlaggedFraud`
- Encoded categorical variable:
  - `type` → numerical values
- Ensured clean and structured dataset for modeling

---

### 2. Feature Engineering
Created key features to detect anomalies:

- `balanceDiffOrig = oldbalanceOrg - newbalanceOrig`  
- `balanceDiffDest = newbalanceDest - oldbalanceDest`  

These help identify **inconsistent balance movements**, which are strong indicators of fraud.

---

### 3. Model Training & Selection

| Model                  | Fraud Recall |
|-----------------------|-------------|
| Logistic Regression   | ~40%        |
| Random Forest         | ~71%        |
| HistGradientBoosting  | ~77%        |

✅ **Selected Model: Random Forest**  
Chosen for its balance between performance, interpretability, and deployment stability.

---

### 4. Evaluation Focus
- Confusion Matrix  
- Precision & Recall  
- Emphasis on **Recall (Fraud Detection Rate)**  

> Missing a fraudulent transaction is more costly than a false alarm.

---

## 🖥️ Application (Streamlit)

The app allows users to:

- Input transaction details  
- Simulate real-world payment scenarios  
- Get instant predictions:
  - Fraud probability (%)
  - Fraud / Legitimate classification  

---

## 📂 Project Structure
