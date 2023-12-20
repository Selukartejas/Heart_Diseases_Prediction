import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
# print("hello world")

df =pd.read_csv("heart_disease_data.csv")
df['target'].value_counts()
df=df.drop(["exang","slope","fbs","restecg"],axis =1)
X = df.drop(columns='target', axis=1)
Y = df['target']
df.var()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
cls = LogisticRegression()
cls.fit(X_train, Y_train)

# accuracy on training data
X_train_prediction = cls.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training data : ', training_data_accuracy)

# print('Accuracy on Test data : ', X_train_prediction)
 
X_test_prediction = cls.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on Test data : ', test_data_accuracy)
# if (X_test_prediction[0]== 0):
#   print('The Person does not have a Heart Disease')
# else:
#   print('The Person has Heart Disease')
filename = 'finalmodel1.sav'
joblib.dump(cls,filename)
