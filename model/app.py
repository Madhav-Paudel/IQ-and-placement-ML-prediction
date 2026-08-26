from flask import Flask, request, render_template
import pickle
from pathlib import Path

app = Flask(__name__)

MODELS_PATH = Path(__file__).resolve().parent / "models"
MODEL_PATH = MODELS_PATH / "model.pkl"
FALLBACK_MODEL_PATH = MODELS_PATH / "fallback_model.pkl"


def train_model():
    model = {"threshold_iq": 95, "threshold_cgpa": 7.0}
    with open(FALLBACK_MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    return model


def load_model():
    if MODEL_PATH.exists():
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)

    if FALLBACK_MODEL_PATH.exists():
        with open(FALLBACK_MODEL_PATH, "rb") as f:
            return pickle.load(f)

    return train_model()


def predict_placement(iq, cgpa):
    model = load_model()

    if hasattr(model, "predict"):
        prediction = model.predict([[iq, cgpa]])[0]
        return "Placed" if prediction == 1 else "Not Placed"

    iq_threshold = model["threshold_iq"]
    cgpa_threshold = model["threshold_cgpa"]
    if iq >= iq_threshold and cgpa >= cgpa_threshold:
        return "Placed"
    return "Not Placed"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            iq = float(request.form["iq"])
            cgpa = float(request.form["cgpa"])
            result = predict_placement(iq, cgpa)
        except Exception:
            result = "Please enter valid numbers"
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
