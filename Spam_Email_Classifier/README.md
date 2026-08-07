# 📧 Spam Email Classifier

## About the Project

This project is a Spam Email Classifier developed using Machine Learning. It can identify whether a message is **Spam** or **Ham (Not Spam)**. The model is trained on a spam email dataset and deployed using Flask so that users can check any message through a simple web interface.

This project helped me understand the complete Machine Learning workflow, including data preprocessing, model training, saving the trained model, and deploying it as a web application.

---

## Features

- Classifies messages as Spam or Ham
- Simple and easy-to-use web interface
- Built using Machine Learning
- Real-time prediction using Flask

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML
- CSS

---

## Project Structure

```
Spam_Email_Classifier
│── app.py
│── train.py
│── spam.csv
│── spam_model.pkl
│── vectorizer.pkl
│── templates/
│     └── index.html
│── static/
│     └── style.css
│── README.md
```

---

## How to Run

1. Install the required libraries.
2. Run the application using:

```bash
python app.py
```

3. Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Future Improvements

- Improve the user interface.
- Add confidence score for predictions.
- Support multiple languages.
- Deploy the project online.

---

## Author

**Ishika Gupta**
B.Tech Computer Science & Engineering