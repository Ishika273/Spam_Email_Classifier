import joblib
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
message = input("Enter a message to classify: ")
message_vectorized = vectorizer.transform([message])
prediction = model.predict(message_vectorized)
if prediction[0] == 1:
    print("The message is classified as: SPAM")
else:
    print("The message is classified as: HAM")