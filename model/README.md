# IQ and Placement Prediction

A Flask-based machine learning web application that estimates whether a student is likely to be placed using IQ and CGPA values. The project demonstrates a complete beginner-friendly workflow: loading a serialized model, accepting browser input, returning a prediction, testing the core logic, and deploying the application to Vercel.

> **Educational disclaimer:** This application is intended for learning and demonstration only. IQ and CGPA are not sufficient to determine a person's placement outcome and should not be used for real recruitment or academic decisions.

## Project Overview

The application provides a web form where a user enters:

- **IQ:** the student's intelligence quotient value
- **CGPA:** the student's cumulative grade point average

When the form is submitted, Flask receives the values, converts them to numbers, loads the main prediction model, and displays either `Placed` or `Not Placed`. If the main model cannot be used, Flask displays an error instead.

The application loads the model from `models/model.pkl`. If the model is unavailable or invalid, it displays an error instead of making a prediction.

## Features

- Browser-based prediction form
- Flask backend with GET and POST handling
- Serialized model loading with an explicit error when the model is unavailable
- Input conversion and basic invalid-input handling
- Separate HTML templates and CSS assets
- Automated tests using pytest
- Vercel serverless deployment configuration
- Clear project structure suitable for further machine learning development

## Directory and File Guide

```text
model/
|-- api/
|   `-- index.py
|-- models/
|   |-- model.pkl
|-- static/
|   `-- style.css
|-- templates/
|   `-- index.html
|-- tests/
|   `-- test_app.py
|-- app.py
|-- requirements.txt
|-- vercel.json
|-- .gitignore
`-- README.md
```

### `app.py`

The main Flask application.

- Creates the Flask application instance.
- Defines the `/` route for displaying and processing the form.
- Reads IQ and CGPA values from the submitted form.
- Calls `predict_placement()` to produce a prediction.
- Loads the main model through `load_model()`.
- Renders `templates/index.html` with the prediction result.
- Starts a local development server when executed directly.

### `api/`

This folder contains the Vercel serverless entry point.

#### `api/index.py`

Imports the Flask application from `app.py` so Vercel can serve it as a Python function. The file also supports local execution through Flask's development server.

### `models/`

This folder stores the serialized prediction models used by the application.

#### `models/model.pkl`

The serialized model used for predictions. If it is missing, unreadable, or has an unsupported format, the application displays a model error and does not predict.

### `templates/`

This folder contains Flask's server-rendered HTML templates.

#### `templates/index.html`

The application's main page. It contains the IQ and CGPA input fields, the submission form, and the area where Flask displays the prediction result.

### `static/`

This folder contains browser assets served by Flask.

#### `static/style.css`

Defines the visual presentation of the application, including layout, typography, form controls, buttons, and prediction-result styling.

### `tests/`

This folder contains automated tests.

#### `tests/test_app.py`

Imports the prediction function and checks that it returns one of the supported prediction labels for higher and lower example inputs. These tests focus on the core prediction behavior rather than browser rendering.

### `requirements.txt`

Lists the Python packages required by the application:

- `Flask` for the web server and request handling
- `pytest` for automated tests
- `scikit-learn` for compatibility with serialized machine learning models

### `vercel.json`

Configures Vercel to use `api/index.py` as the Python serverless function and route incoming requests to that function.

### `.gitignore`

Prevents generated files and local-only resources from being committed, including Python cache files, pytest cache files, virtual environments, and IDE settings.

### `README.md`

This document explains the project, its architecture, local setup, testing process, deployment process, and known limitations.

## Application Flow

```text
User opens the application
          |
          v
Flask renders templates/index.html
          |
          v
User submits IQ and CGPA
          |
          v
The / route validates and converts the input
          |
          v
load_model() loads model.pkl
          |
          v
predict_placement() calculates the result
          |
          v
Flask renders Placed or Not Placed
```

## Local Installation

### Prerequisites

- Python 3.9 or newer
- `pip`
- Git, if cloning the repository

### Windows PowerShell

Open PowerShell in this project directory:

```powershell
cd "C:\path\to\IQ-and-placement-ML-prediction"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell prevents script activation, run this only for the current terminal session and then activate the environment again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run Locally

Start the Flask development server:

```bash
python app.py
```

Open the application at:

```text
http://127.0.0.1:5000
```

Enter IQ and CGPA values and submit the form to view the prediction.

## Run Tests

Run the test suite from the project directory:

```bash
python -m pytest
```

The tests currently verify that the prediction function returns a supported result for representative high and low input values.

## Deploy to Vercel

The repository is configured for Vercel using `vercel.json` and `api/index.py`.

### Vercel Dashboard

1. Push the repository to GitHub.
2. Open [Vercel](https://vercel.com) and select **Add New Project**.
3. Import the GitHub repository.
4. Set the framework preset to **Other**.
5. Leave the build command and output directory empty.
6. If the repository contains an outer folder, set the project root to the folder containing `app.py`, `api/`, and `vercel.json`.
7. Click **Deploy**.

### Vercel CLI

Install and sign in to the Vercel CLI:

```bash
npm install -g vercel
vercel login
```

Deploy a preview version:

```bash
vercel
```

Deploy to production:

```bash
vercel --prod
```

Vercel installs the packages from `requirements.txt`, loads `api/index.py`, and routes requests according to `vercel.json`.

## Model Behavior

The application supports either a threshold dictionary containing `threshold_iq` and `threshold_cgpa`, or a scikit-learn model exposing `predict()` with `[IQ, CGPA]` input:

```text
Placed when IQ >= 95 and CGPA >= 7.0
Not Placed otherwise
```

The checked-in `models/model.pkl` is a scikit-learn `LogisticRegression` artifact, so it is loaded through `predict()`. Its output label `1` is displayed as `Placed`; other labels are displayed as `Not Placed`.

## Limitations and Responsible Use

- IQ and CGPA alone cannot reliably predict employment outcomes.
- The supported threshold rule is not a validated production model.
- Input validation does not yet enforce realistic IQ or CGPA ranges.
- The current tests do not evaluate model accuracy or validate the complete browser workflow.
- Pickle files can execute code during loading and must only be loaded from trusted sources.
- The application should not be used to make real hiring, admissions, or academic decisions.

## Potential Improvements

- Train and evaluate a model using a documented dataset.
- Add relevant features such as skills, internships, projects, communication, and academic history.
- Add realistic range validation and clearer form-level error messages.
- Add route tests for GET requests, POST requests, and invalid input.
- Report evaluation metrics such as accuracy, precision, recall, and F1-score.
- Add model versioning and metadata describing the training environment.
- Improve accessibility and provide a clear explanation of each prediction.

## Learning Context

This project was created as an educational exercise while studying the machine learning workflow and Flask deployment process, including material from the CampusX YouTube tutorials and the CampusX 100 Days of Machine Learning series.

## License

This project is intended for educational and personal learning use. Review the repository's `LICENSE` file for the applicable terms.
