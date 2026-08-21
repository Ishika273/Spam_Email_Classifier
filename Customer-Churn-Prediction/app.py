import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

with open('notebooks/rf_model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        tenure = float(request.form['tenure'])
        monthly_charges = float(request.form['monthly_charges'])
        gender = request.form['gender']
        partner = request.form['partner']
        dependents = request.form['dependents']
        contract = request.form['contract']
        internet_service = request.form['internet_service']
        online_security = request.form['online_security']
        tech_support = request.form['tech_support']
        payment_method = request.form['payment_method']

        data = {
            'SeniorCitizen': 0,
            'tenure': tenure,
            'MonthlyCharges': monthly_charges,
            'TotalCharges': tenure * monthly_charges,
            'gender_Male': 1 if gender == 'Male' else 0,
            'Partner_Yes': 1 if partner == 'Yes' else 0,
            'Dependents_Yes': 1 if dependents == 'Yes' else 0,
            'PhoneService_Yes': 1,
            'MultipleLines_No phone service': 0,
            'MultipleLines_Yes': 0,
            'InternetService_Fiber optic': 1 if internet_service == 'Fiber optic' else 0,
            'InternetService_No': 1 if internet_service == 'No' else 0,
            'OnlineSecurity_No internet service': 1 if online_security == 'No internet service' else 0,
            'OnlineSecurity_Yes': 1 if online_security == 'Yes' else 0,
            'OnlineBackup_No internet service': 0,
            'OnlineBackup_Yes': 0,
            'DeviceProtection_No internet service': 0,
            'DeviceProtection_Yes': 0,
            'TechSupport_No internet service': 1 if tech_support == 'No internet service' else 0,
            'TechSupport_Yes': 1 if tech_support == 'Yes' else 0,
            'StreamingTV_No internet service': 0,
            'StreamingTV_Yes': 0,
            'StreamingMovies_No internet service': 0,
            'StreamingMovies_Yes': 0,
            'Contract_One year': 1 if contract == 'One year' else 0,
            'Contract_Two year': 1 if contract == 'Two year' else 0,
            'PaperlessBilling_Yes': 0,
            'PaymentMethod_Credit card (automatic)': 1 if payment_method == 'Credit card (automatic)' else 0,
            'PaymentMethod_Electronic check': 1 if payment_method == 'Electronic check' else 0,
            'PaymentMethod_Mailed check': 1 if payment_method == 'Mailed check' else 0
        }

        input_data = pd.DataFrame([data])
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            prediction = "Customer will Churn"
        else:
            prediction = "Customer will Stay"

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)