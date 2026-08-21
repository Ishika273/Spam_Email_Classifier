import pandas as pd
import joblib

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
data = pd.read_csv("dataset/spam.csv", encoding='latin-1')
print(data.head())
print(data.info())
print(data.columns)
print(data.shape)
data = data[['v1', 'v2']]
data.columns = ['label', 'message']
print(data.head())
#check for null values
print(data.isnull().sum())
#remove duplicates
data= data.drop_duplicates()
print(data.shape)
#convert the labels to binary values
data['label'] = data['label'].map({'ham': 0, 'spam': 1})
print(data.head())
#feature and labels
x = data['message']
y = data['label']
print(x.head())
print(y.head())
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(x)
print(x.shape)
#Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train.shape)
print(x_test.shape)
#create a Multinomial Naive Bayes model
model = MultinomialNB()
#train the model
model.fit(x_train, y_train)
#make predictions
y_pred = model.predict(x_test)
#evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy )
#save model
joblib.dump(model, 'spam_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
print("Model saved successfully.")