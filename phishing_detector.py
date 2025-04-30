import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import classification_report

# 1. Email dataset (19 emails and 19 labels)
emails = [
    "Urgent! Your account has been compromised. Click here to reset your password.",
    "Congratulations! You've won a free iPhone. Claim now.",
    "Don't forget about the team lunch on Friday.",
    "Meeting rescheduled to 3 PM, please confirm.",
    "Verify your identity to unlock your account now.",
    "Happy birthday! Hope you have a great day.",
    "Please find the attached project report for review.",
    "Hi, I hope you are doing well. Just checking in about the meeting tomorrow.",
    "Your invoice is due. Pay now to avoid service interruption.",
    "Security alert: Your PayPal account has been temporarily suspended.",
    "Reminder: Your payment was successfully processed for your subscription.",
    "Click here to get a free vacation package!",
    "Important: Update your credit card information immediately to avoid service interruption.",
    "Here is the updated project proposal. Please review it before our next meeting.",
    "Your account has been suspended, please verify your information immediately!",
    "Congratulations! You've won a $1,000 gift card!",
    "Team Meeting Reminder: 3 PM Today",
    "Invoice #12345 - Payment Confirmation",
    "Reminder: Your document is ready for download."
]

# Labels: 1 = phishing, 0 = legitimate
labels = [
    1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0
]

# 2. TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
X = vectorizer.fit_transform(emails)
y = np.array(labels)

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Compute class weights (FIXED with np.array)
class_weights = compute_class_weight(class_weight='balanced', classes=np.unique(y_train), y=y_train)
class_weight_dict = {0: class_weights[0], 1: class_weights[1]}

# 5. Train the model with class weights
model = RandomForestClassifier(random_state=42, class_weight=class_weight_dict)
model.fit(X_train, y_train)

# 6. Evaluate model
y_pred = model.predict(X_test)
print("🔍 Classification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))

# 7. Function to classify user input
def classify_email(email_subject, email_body):
    email_content = email_subject + " " + email_body
    email_vector = vectorizer.transform([email_content])
    prediction = model.predict(email_vector)[0]
    
    print("\n🛡️ RESULT:")
    if prediction == 1:
        print("⚠️ This email is likely a PHISHING attempt!")
    else:
        print("✅ This email seems LEGITIMATE.")

# 8. Test loop for user input
while True:
    print("\n📥 Enter the subject and body of an email to classify it (or type 'exit' to quit):")
    subject = input("Subject: ")
    if subject.strip().lower() == 'exit':
        break

    body = input("Body: ")
    if body.strip().lower() == 'exit':
        break

    classify_email(subject, body)
