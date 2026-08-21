from flask import Flask, request, render_template
import joblib
app = Flask(__name__)
#load the trained model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
#home page route
@app.route('/')
def home():
    return render_template('index.html')
#predict route
@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    message_vectorized = vectorizer.transform([message])
    prediction = model.predict(message_vectorized)
    if prediction[0] == 1:
        result = "SPAM"
        color = "red"
        meessage = "This is a spam email."
    else:
        result = "HAM"
        color = "green"
        meessage = "This is a legitimate email."
    return render_template('index.html', prediction=result, color=color, message=meessage)
if __name__ == '__main__':
    app.run(debug=True)