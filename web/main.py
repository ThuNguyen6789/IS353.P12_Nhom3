from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    model = joblib.load('../src/model.pkl')
    data = {key: float(value) for key, value in request.form.items()}
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)