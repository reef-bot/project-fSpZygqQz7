```python
# File: moderation_bot/src/machine_learning.py

import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

class ContentModerator:
    def __init__(self):
        self.model = None
        self.vectorizer = None

    def train_model(self, data_path):
        data = pd.read_csv(data_path)
        X = data['content']
        y = data['label']

        self.vectorizer = TfidfVectorizer()
        X = self.vectorizer.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = LogisticRegression()
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model trained with accuracy: {accuracy}")

    def predict(self, text):
        if self.model is None or self.vectorizer is None:
            print("Model has not been trained yet.")
            return

        text = self.vectorizer.transform([text])
        prediction = self.model.predict(text)
        return prediction[0]

# Load data path
data_path = os.path.join(os.path.dirname(__file__), '../data/moderation_data.csv')

# Initialize and train the model
moderator = ContentModerator()
moderator.train_model(data_path)
```