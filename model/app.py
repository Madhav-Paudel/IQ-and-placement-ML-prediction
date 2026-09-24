from flask import Flask, request, render_template
import pickle
from pathlib import Path

app = Flask(__name__)

MODELS_PATH = Path(__file__).resolve().parent / "models"
MODEL_PATH = MODELS_PATH / "model.pkl"


class ModelLoadError(Exception):
    pass


def load_model():
    if not MODEL_PATH.exists():
        raise ModelLoadError("The main model is unavailable.")

    try:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    except (OSError, pickle.PickleError, EOFError, ImportError, AttributeError) as error:
        raise ModelLoadError("The main model could not be loaded.") from error

    if isinstance(model, dict):
        if not {"threshold_iq", "threshold_cgpa"}.issubset(model):
            raise ModelLoadError("The main model has an invalid format.")
    elif not callable(getattr(model, "predict", None)):
        raise ModelLoadError("The main model has an invalid format.")

    return model


def predict_placement(iq, cgpa):
    model = load_model()

    if isinstance(model, dict):
        iq_threshold = model["threshold_iq"]
        cgpa_threshold = model["threshold_cgpa"]
        return "Placed" if iq >= iq_threshold and cgpa >= cgpa_threshold else "Not Placed"

    try:
        prediction = model.predict([[iq, cgpa]])
        return "Placed" if int(prediction[0]) == 1 else "Not Placed"
    except (IndexError, TypeError, ValueError, AttributeError) as error:
        raise ModelLoadError("The main model could not make a prediction.") from error

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            iq = float(request.form["iq"])
            cgpa = float(request.form["cgpa"])
            result = predict_placement(iq, cgpa)
        except ModelLoadError as error:
            result = str(error)
        except Exception:
            result = "Please enter valid numbers"
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
