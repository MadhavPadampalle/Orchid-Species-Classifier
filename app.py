# app.py
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('orchid_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def getKmers(sequence, size=4):
    return [sequence[x:x+size] for x in range(len(sequence) - size + 1)]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sequence = request.form['sequence']
    k_mers = getKmers(sequence)
    joined_seq = ' '.join(k_mers)
    vect = vectorizer.transform([joined_seq])
    prediction = model.predict(vect)[0]
    return render_template('index.html', prediction=f'Predicted Species: {prediction}')

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
