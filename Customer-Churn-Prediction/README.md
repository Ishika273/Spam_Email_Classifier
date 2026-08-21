# Customer Churn Prediction

A Machine Learning web application built using Flask and Logistic Regression to predict whether a customer will churn or stay.

## Project Overview

This project predicts customer churn using customer information such as tenure, monthly charges, contract type, internet service, and payment method.

The model was trained on the Telco Customer Churn dataset and deployed using Flask.

## Features

- Customer churn prediction
- Interactive web interface
- Logistic Regression model
- Flask-based deployment
- Real-time prediction results

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-Learn
- HTML
- CSS

---

## Project Structure

```text
Customer-Churn-Prediction/
│
├── dataset/
├── notebooks/
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── README.md
└── model.pkl
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Machine Learning Model

### Logistic Regression

Model Performance:

- Accuracy: 82.19%
- Precision (Churn): 0.69
- Recall (Churn): 0.60
- F1-Score (Churn): 0.64

### Classification Report

| Class | Precision | Recall | F1-Score |
|---------|---------|---------|---------|
| No Churn (0) | 0.86 | 0.90 | 0.88 |
| Churn (1) | 0.69 | 0.60 | 0.64 |

Overall Accuracy: **82.19%**

## Input Features

- Tenure
- Monthly Charges
- Gender
- Partner
- Dependents
- Contract Type
- Internet Service
- Online Security
- Tech Support
- Payment Method

## Output

- Customer Will Stay
- Customer Will Churn

## Future Improvements

- Improved UI Design
- Hyperparameter Tuning
- Cloud Deployment
- Probability-Based Churn Prediction

## Author

Ishika Gupta
AI Internship Project