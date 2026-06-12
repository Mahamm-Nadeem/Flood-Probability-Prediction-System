from flask import Flask, request, jsonify
import numpy as np
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        prediction = float(np.clip(prediction, 0, 1))

        return jsonify({
            "probability": prediction
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)