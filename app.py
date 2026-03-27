from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    input_data = {
    'status': 'A11',
    'duration': int(data['duration']),
    'credit_history': data['credit_history'],
    'purpose': 'A43',
    'amount': int(data['amount']),
    'savings': int(data['savings']),
    'employment_duration': data['employment_duration'],
    'installment_rate': 2,
    'personal_status_sex': 'A93',
    'other_debtors': 'A101',
    'present_residence': 2,
    'property': 'A121',
    'age': int(data['age']),
    'other_installment_plans': 'A143',
    'housing': data['housing'],
    'number_credits': 1,
    'job': 'A173',
    'people_liable': 1,
    'telephone': 'A191',
    'foreign_worker': 'A201'
    }

    df = pd.DataFrame([input_data])

    pred = model.predict(df)[0]

    result = "Low Risk ✅" if pred == 1 else "High Risk ⚠️"

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)