import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("loan_dataset.csv")

df = df.dropna()

le = LabelEncoder()

df['Self_Employed'] = le.fit_transform(df['Self_Employed'])

df['Loan_Status'] = le.fit_transform(df['Loan_Status'])

X = df[
    [
        'ApplicantIncome',
        'LoanAmount',
        'Self_Employed',
        'Credit_History',
        'CIBIL_Score'
    ]
]

y = df['Loan_Status']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)

joblib.dump(model, "model.pkl")

print("Model Trained Successfully")