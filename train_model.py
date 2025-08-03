import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
df = pd.read_csv('PhishingData.csv')
#print(df)
x = df.drop(columns=['Result'])
y = df['Result']
#print(y)
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)
joblib.dump(model, 'phishing_detector.pkl')
