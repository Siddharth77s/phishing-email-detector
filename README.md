# 📧 Phishing Email Detector | Machine Learning App 🔐

This project is a simple yet powerful **phishing email detection system** built using **Natural Language Processing (NLP)** and **Random Forest Classification**. It allows users to input an email's subject and body, and the app predicts whether the email is a phishing attempt or a legitimate message.

---
<pre><code>``` 📁 phishing-email-detector/ ├── phishing_gui.py # Streamlit web app code ├── phishing_model.ipynb # Model training (Colab / Jupyter Notebook) ├── requirements.txt # List of required Python libraries ├── README.md # Project overview and instructions ``` </code></pre>

---

## 📌 Features
- 🧠 Machine learning model trained on real-world email samples
- ✍️ Takes email **subject + body** as user input
- 🔍 Uses **TF-IDF vectorization** and **n-grams** for feature extraction
- ✅ Classifies emails as either **Phishing** or **Legitimate**
- 🌐 Deployed with a professional GUI using **Streamlit**

---

## 🧪 Sample Test Inputs

| Subject                                       | Body                                               | Result     |
|-----------------------------------------------|----------------------------------------------------|------------|
| "Urgent! Reset Your Password Now"             | "Your account was compromised. Click here to fix." | ⚠️ Phishing |
| "Team Sync at 3 PM"                           | "Join Zoom using the link in the invite."          | ✅ Legit    |
| "Congratulations! You've won a $1000 gift card!" | "Click here to claim your prize now!"             | ⚠️ Phishing |

---

## 🧠 How It Works

1. **TF-IDF Vectorization**: Transforms text data into numerical features
2. **Random Forest Classifier**: Learns from past emails to classify new ones
3. **Streamlit GUI**: Web app where users can input and test email messages

---

## 💻 Run Locally

### 📋 Requirements
- Python 3.8+
- Install dependencies:
```bash
pip install -r requirements.txt
# phishing-email-detector

