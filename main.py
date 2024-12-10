from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

LOCAL_MODEL_PATH = "SoulSync_Model.h5"

def load_local_model(model_path):
    try:
        model = load_model(model_path)
        print(f"Model successfully loaded from {model_path}")
        return model
    except Exception as e:
        print(f"Failed to load model from local file: {e}")
        raise

try:
    loadedModel = load_local_model(LOCAL_MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    loadedModel = None

def validateInput(userInput, inputType, validRange=None):
    try:
        userInput = inputType(userInput)
        if validRange and userInput not in validRange:
            raise ValueError(f"Input must be within range {validRange}")
        return userInput
    except ValueError as e:
        raise ValueError("Invalid input") from e

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to SoulSync!"})

@app.route('/predict', methods=['POST'])
def predict():
    if not loadedModel:
        return jsonify({"message": "Model is not loaded"}), 500

    try:
        data = request.json
        userInput = {
            "Gender": validateInput(data.get("Gender"), int, range(0, 2)),
            "WorkOrStudent": validateInput(data.get("WorkOrStudent"), int, range(0, 2)),
            "Pressure": validateInput(data.get("Pressure"), int, range(1, 6)),
            "Satisfaction": validateInput(data.get("Satisfaction"), int, range(1, 6)),
            "SleepDr": validateInput(data.get("SleepDr"), int, range(0, 4)),
            "DietHabits": validateInput(data.get("DietHabits"), int, range(0, 3)),
            "SuicidalTh": validateInput(data.get("SuicidalTh"), int, range(0, 2)),
            "WSHours": validateInput(data.get("WSHours"), int, range(0, 13)),
            "FinancialStress": validateInput(data.get("FinancialStress"), int, range(1, 6)),
            "FamHistory": validateInput(data.get("FamHistory"), int, range(0, 2)),
        }

        input_df = pd.DataFrame([userInput])
        inputData = input_df.values.reshape(1, -1)
        prediction = loadedModel.predict(inputData)

        result = "Depression" if prediction[0][0] > 0.5 else "No Depression"
        return jsonify({"message": "Prediction successful", "result": result}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
