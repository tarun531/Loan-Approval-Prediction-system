from flask import Flask, render_template, request
import joblib
import easyocr
import re
import os

app = Flask(__name__)

model = joblib.load("model.pkl")

UPLOAD_FOLDER = "uploads"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

reader = easyocr.Reader(['en'])

def verify_pan(text):

    pattern = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"

    match = re.search(pattern, text)

    if match:
        return match.group()
    else:
        return None

@app.route('/')

def home():

    return render_template("index.html")

@app.route('/predict', methods=['POST'])

def predict():

    income = float(request.form['income'])

    loan = float(request.form['loan'])

    self_employed = int(
        request.form['self_employed']
    )

    cibil = int(
        request.form['cibil']
    )

    if cibil >= 700:
        credit_history = 1
    else:
        credit_history = 0

    file = request.files['pan']

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    result = reader.readtext(
        filepath,
        detail=0
    )

    extracted_text = " ".join(result)

    pan_number = verify_pan(
        extracted_text
    )

    if not pan_number:

        return render_template(
            "result.html",
            status="PAN Verification Failed",
            pan="Invalid PAN"
        )

    prediction = model.predict([
        [
            income,
            loan,
            self_employed,
            credit_history,
            cibil
        ]
    ])

    if prediction[0] == 1:
        status = "LOAN APPROVED"
    else:
        status = "LOAN REJECTED"

    return render_template(
        "result.html",
        status=status,
        pan=pan_number,
        score=cibil
    )

if __name__ == "__main__":
    app.run(debug=True)