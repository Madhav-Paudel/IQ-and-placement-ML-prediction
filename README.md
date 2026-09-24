# IQ and Placement Prediction

This repository contains a Flask web application that estimates a student's placement status from IQ and CGPA values. It is an educational machine learning deployment project and is not intended for real hiring, admissions, or academic decisions.

## What the Project Does

The application provides a browser form for entering IQ and CGPA values. Flask processes the submitted values and returns one of two results when a compatible model is available:

- `Placed` when the loaded model returns class `1`
- `Not Placed` when the loaded model returns another class

The application uses only the main serialized model. It supports a threshold dictionary or a scikit-learn model with `predict()`. If the model is missing, unreadable, or incompatible, the page shows an error instead of making a prediction.

## Project Structure

```text
IQ and placement/
|-- model/
|   |-- api/index.py              Vercel serverless entry point
|   |-- models/                   Serialized model files
|   |-- static/style.css          Browser styling
|   |-- templates/index.html      Flask HTML template
|   |-- tests/test_app.py         Automated prediction tests
|   |-- app.py                    Flask routes and prediction logic
|   |-- requirements.txt          Python dependencies
|   |-- vercel.json               Vercel routing configuration
|   `-- README.md                 Complete project documentation
`-- README.md                     Repository overview
```

## Important Files

### `model/app.py`

Creates the Flask application, handles the home page form, converts submitted values to numbers, loads the main model, and calculates the prediction. If the model cannot be loaded, the page shows an error and does not make a prediction.

### `model/api/index.py`

Imports the Flask app for Vercel deployment.

### `model/models/`

Contains the serialized model artifact. The application supports a dictionary with `threshold_iq` and `threshold_cgpa` values or a scikit-learn model with `predict()`.

### `model/templates/index.html`

Contains the IQ and CGPA form and displays the result returned by Flask.

### `model/static/style.css`

Contains the application's layout and visual styles.

### `model/tests/test_app.py`

Checks high, low, and minimum input cases, plus the model-error page behavior. In particular, `5,5` must return `Not Placed` when the test model is available.

### `model/requirements.txt`

Lists Flask, pytest, and scikit-learn dependencies.

### `model/vercel.json`

Routes Vercel requests to `api/index.py`.

## Run Locally

From the `model` directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

## Run Tests

```powershell
python -m pytest
```

## Deploy to Vercel

Import the GitHub repository into Vercel and set the project root to `model`. Use the **Other** framework preset, leave the build and output fields empty, and deploy. Vercel uses `model/vercel.json` and `model/api/index.py` to serve the Flask application. Confirm that `models/model.pkl` is a supported threshold-model dictionary before deploying.

## Disclaimer

IQ and CGPA alone cannot reliably predict placement outcomes. This project is for learning and demonstration only.

For complete technical documentation, see [`model/README.md`](model/README.md).
