# 🚀 Loan Approval Prediction System using PAN Verification & Machine Learning

## 📌 Project Overview

This project demonstrates a complete Machine Learning-based Loan Approval Prediction System where user financial information and PAN card verification are used to determine whether a person is eligible for a loan or not.

Unlike traditional ML projects that only focus on model training, this system includes:

* PAN Card OCR Verification
* Credit Score Analysis
* Employment Verification
* Flask Web Application
* Real-time Loan Prediction
* Interactive User Interface

The application simulates a real-world banking loan approval workflow.

---

# 🎯 Key Features

✅ PAN Card Verification using OCR
📊 Machine Learning-based Loan Prediction
💳 CIBIL / Credit Score Analysis
👨‍💼 Self Employed & Salaried Verification
🌐 Flask-based Web Application
📁 Realistic Banking Dataset
🚀 Real-time Prediction Results
🎨 Modern Responsive UI

---

# 🧠 Architecture / Workflow

```text
User Input + PAN Upload
            ↓
OCR Extracts PAN Number
            ↓
PAN Validation using Regex
            ↓
ML Model Analysis
(Income + Employment + CIBIL + Loan Amount)
            ↓
Loan Eligibility Prediction
            ↓
Display Result on Web Dashboard
```

---

# ⚙️ Tech Stack

| Category        | Tools                    |
| --------------- | ------------------------ |
| Programming     | Python                   |
| ML Framework    | Scikit-learn             |
| Backend         | Flask                    |
| OCR             | EasyOCR                  |
| Frontend        | HTML, CSS, Bootstrap     |
| Data Processing | Pandas, NumPy            |
| Model           | Random Forest Classifier |
| Deployment      | Render / GitHub          |

---

# 📂 Project Structure

```text
Loan-Approval-System/
│
├── app.py
├── train_model.py
├── model.pkl
├── loan_dataset.csv
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── uploads/
```

---

# 🔄 How It Works (Step-by-Step)

## 1️⃣ User Uploads PAN Card

The user uploads a PAN card image through the web interface.

---

## 2️⃣ OCR Text Extraction

EasyOCR extracts text from the uploaded PAN image.

Example:

```text
ABCDE1234F
```

---

## 3️⃣ PAN Validation

Regex validates PAN format.

Example pattern:

```python
[A-Z]{5}[0-9]{4}[A-Z]{1}
```

---

## 4️⃣ User Enters Financial Details

The system collects:

* Applicant Income
* Loan Amount
* Employment Type
* CIBIL Score

---

## 5️⃣ Machine Learning Prediction

Random Forest Classifier analyzes:

* Income
* CIBIL Score
* Employment Status
* Credit History
* Loan Amount

Then predicts:

✅ Loan Approved
❌ Loan Rejected

---

## 6️⃣ Result Display

The web application displays:

* PAN Number
* CIBIL Score
* Loan Approval Status

Example:

```text
LOAN APPROVED
PAN: ABCDE1234F
CIBIL Score: 790
```

---

# 🚀 How to Run This Project

## 🔹 Prerequisites

* Python 3.x
* VS Code
* Git
* pip

---

## 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/tarun531/Loan-Approval-Prediction-system.git

cd Loan-Approval-Prediction-system
```

---

## 🔹 Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 🔹 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 Step 4: Train Machine Learning Model

```bash
python train_model.py
```

This generates:

```text
model.pkl
```

---

## 🔹 Step 5: Run Flask Application

```bash
python app.py
```

---

## 🔹 Step 6: Open Browser

```text
http://127.0.0.1:5000
```

---

# 📊 Machine Learning Workflow

## Input Features

* Applicant Income
* Loan Amount
* Self Employed Status
* Credit History
* CIBIL Score

## Target Output

* Loan Approved / Rejected

---

# 📸 Expected Output

## Approved Case

```text
LOAN APPROVED
PAN Number: ABCDE1234F
CIBIL Score: 790
```

---

## Rejected Case

```text
LOAN REJECTED
Reason:
Low Income & Poor Credit Score
```

---

# 🏆 Key Learning Outcomes

* End-to-end ML project development
* OCR integration using EasyOCR
* Flask web development
* Loan approval prediction using ML
* PAN verification using Regex
* UI integration with backend
* Real-world banking workflow simulation

---

# 🔥 Why This Project is Important

Most beginner ML projects only train models.

This project demonstrates:

* Real-world ML workflow
* User verification system
* OCR document processing
* Backend + Frontend integration
* Real-time predictions
* Production-style application design

---

# 👨‍💻 Author

## Tarun Sunkam

GitHub:
https://github.com/tarun531

---

# ⭐ Future Improvements

* Aadhaar Verification
* Face Matching
* Real CIBIL API Integration
* MySQL Database
* Admin Dashboard
* Docker Deployment
* Cloud Hosting
* CI/CD Pipeline

---

# 💡 Final Note

This project represents a real-world AI-powered banking loan approval system that combines Machine Learning, OCR, and Web Development technologies to simulate industry-level loan verification and approval workflows.
