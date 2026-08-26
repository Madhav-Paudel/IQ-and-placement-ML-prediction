# Placement Predictor

A beginner-friendly machine learning deployment project that predicts whether a student is likely to be placed using IQ and CGPA as input features.

This project was created while learning from CampusX YouTube tutorials and following the CampusX **100 Days of Machine Learning** series. It is an educational project built to practice the complete flow from defining a prediction problem to serving a model through a web application and deploying it with Vercel.

> **Disclaimer:** This project is for learning and demonstration purposes only. Placement outcomes depend on many factors and cannot be reliably determined from IQ and CGPA alone.

## Features

- Simple browser-based prediction form
- Flask web application
- Accepts IQ and CGPA values
- Supports loading a serialized model from `model.pkl`
- Creates and uses a fallback model when a trained model file is unavailable
- Basic automated tests with pytest
- Vercel deployment configuration included

## Project Structure

```text
model/
├── app.py                 # Main Flask application and prediction logic
├── models/
│   ├── model.pkl          # Optional trained model file
│   └── fallback_model.pkl # Fallback model generated automatically
├── templates/
│   └── index.html         # Prediction form
├── static/
│   └── style.css          # Application styles
├── api/
│   └── index.py           # Vercel entry point
└── tests/
    └── test_app.py        # Prediction tests
├── requirements.txt       # Python dependencies
├── .gitignore             # Files excluded from Git
├── README.md              # Project documentation
└── vercel.json            # Vercel deployment configuration
```

## How This Project Was Created

The project followed a practical, step-by-step learning workflow based on the CampusX tutorials and the 100 Days of Machine Learning series:

1. **Learned the machine learning workflow**
   - Understood how a real-world problem can be converted into a prediction problem.
   - Identified student placement as the target use case.
   - Selected IQ and CGPA as the input features and placement status as the prediction output.

2. **Defined the prediction behavior**
   - Created the `predict_placement(iq, cgpa)` function.
   - Used a simple fallback rule that predicts `Placed` when IQ is at least `95` and CGPA is at least `7.0`.
   - Returned `Not Placed` when either threshold is not met.

3. **Added model loading support**
   - Implemented support for an optional trained model stored in `models/model.pkl`.
   - If that file is unavailable, the application checks for `models/fallback_model.pkl`.
   - If neither file exists, the application generates the fallback model automatically using Python's `pickle` module.

4. **Built the Flask application**
   - Created a Flask app with a home route at `/`.
   - Added a form for entering IQ and CGPA.
   - Added POST request handling to process user input.
   - Added validation so invalid numeric input produces a clear message.
   - Displayed the prediction result directly in the browser.

5. **Prepared the application for deployment**
   - Created `api/index.py` as the serverless entry point.
   - Added `vercel.json` to route incoming requests to the Flask application.
   - Added the required dependencies to `requirements.txt`.
   - Added separate template and static directories for maintainable frontend files.

6. **Added basic testing**
   - Created pytest tests for both higher and lower student input values.
   - Verified that the prediction function returns one of the supported results: `Placed` or `Not Placed`.

## Technologies Used

- Python
- Flask
- Pytest
- Pickle
- Vercel
- HTML and CSS

## Local Setup

### Prerequisites

- Python 3.9 or newer
- `pip`
- Git, if you want to clone the project

### Installation

1. Open a terminal in the `model` directory.

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment.

   On Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   source venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If you want the application to load the included `models/model.pkl`, install a compatible scikit-learn version as well:

   ```bash
   pip install scikit-learn==1.6.1
   ```

   Without scikit-learn, remove or rename `models/model.pkl` to use the built-in fallback model instead.

## Run the Application

Start the Flask development server:

```bash
python app.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

Enter an IQ value and CGPA, then select **Predict** to see the result.

## Run the Tests

From the `model` directory, run:

```bash
pytest
```

## Deployment on Vercel

This project includes a Vercel configuration through `vercel.json`.

1. Install and sign in to the Vercel CLI, or connect the repository through the Vercel dashboard.
2. Set the project root to the `model` directory if the repository contains other folders.
3. If deploying with the included `models/model.pkl`, make sure the required scikit-learn dependency is listed in `requirements.txt` before deploying.
4. Deploy the project:

   ```bash
   vercel
   ```

5. Follow the prompts provided by Vercel.
6. Vercel uses `api/index.py` as the Python entry point and routes requests according to `vercel.json`.

For production deployment, use:

```bash
vercel --prod
```

## Application Flow

```text
User enters IQ and CGPA
          |
          v
Flask receives the POST request
          |
          v
Application loads models/model.pkl,
models/fallback_model.pkl, or creates a fallback model
          |
          v
Prediction is calculated
          |
          v
Placed / Not Placed is shown in the browser
```

## Current Limitations

- The fallback model is threshold-based and is not a replacement for a properly trained model.
- The current tests check the output format but do not yet assert specific predictions for each input.
- IQ and CGPA alone are not sufficient features for a reliable placement prediction.
- Input-range validation can be improved for values outside realistic IQ and CGPA ranges.
- Pickle files should only be loaded from trusted sources.

## Future Improvements

- Train and save a real machine learning model using a properly prepared dataset.
- Add more relevant features such as skills, internships, projects, communication ability, and academic history.
- Add stronger input validation and user-friendly error messages.
- Improve the test suite with exact expected predictions and route-level tests.
- Add a clear model evaluation section with metrics such as accuracy, precision, recall, and F1-score.
- Improve the user interface and add explanatory prediction details.

## Learning Reference

The project was developed as part of my learning journey through CampusX YouTube content and the CampusX 100 Days of Machine Learning series. The tutorials provided the learning direction for understanding machine learning concepts, building a small application, and deploying it for practical use.

## License

This project is available for educational and personal learning purposes. Add a license file if you plan to distribute or reuse it formally.
