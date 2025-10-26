from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__, template_folder='templates')

# Check if model file exists before loading
model_path = "ecg_model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()  # dummy model for demo

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"result": str(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


