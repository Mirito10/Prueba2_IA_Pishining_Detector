from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

app = Flask(__name__)

model = joblib.load('models/phishing_detector_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

def check_email(email_body):
    email_vectorized = vectorizer.transform([email_body])
    prediction = model.predict(email_vectorized)
    return prediction[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_email', methods=['POST'])
def check_email_route():
    try:
        email_body = request.form['email_body']
        print("Cuerpo de correo recibido:", email_body)

        result = check_email(email_body)
        
        if result == 1:
            message = "Correo potencialmente malicioso (phishing)"
        else:
            message = "Correo legítimo"
        
        return jsonify({'result': message})
    except Exception as e:
        return jsonify({'result': f"Error: {e}"})

if __name__ == '__main__':
    app.run(debug=True)
