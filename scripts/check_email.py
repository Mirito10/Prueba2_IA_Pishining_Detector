import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

model = joblib.load('models/phishing_detector_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

def check_email(email_body):
    email_vectorized = vectorizer.transform([email_body])
    prediction = model.predict(email_vectorized)
    return prediction[0]  

def check_emails_in_csv(csv_file):
    try:
        df = pd.read_csv(csv_file)
        
        if 'body' not in df.columns:
            print("El dataset no contiene la columna 'body'.")
            return
        df['prediction'] = df['body'].apply(check_email)
        
        print(df[['sender', 'body', 'prediction']])
        output_path = 'checked/checked_emails.csv'
        df.to_csv(output_path, index=False)
        print(f"\nResults saved to {output_path}")
        
        phishing_count = (df['prediction'] == 1).sum()
        print(f"\nTotal de correos con pishing encontrados: {phishing_count}\n")
    except Exception as e:
        print(f"Error processing the file: {e}")

if __name__ == '__main__':
    csv_file = input("Enter the path to the email CSV file: ")
    check_emails_in_csv(csv_file)
