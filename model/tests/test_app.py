import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import app as app_module

app = app_module.app
predict_placement = app_module.predict_placement


@pytest.fixture
def valid_main_model(monkeypatch):
    class FakeClassifier:
        def predict(self, values):
            iq, cgpa = values[0]
            return [1 if iq >= 95 and cgpa >= 7.0 else 0]

    monkeypatch.setattr(
        app_module,
        "load_model",
        lambda: FakeClassifier(),
    )


def test_predict_placement_for_good_student(valid_main_model):
    result = predict_placement(120, 9.2)
    assert result == "Placed"


def test_predict_placement_for_low_student(valid_main_model):
    result = predict_placement(60, 5.0)
    assert result == "Not Placed"


def test_predict_placement_for_minimum_values(valid_main_model):
    assert predict_placement(5, 5) == "Not Placed"


def test_main_model_failure_shows_error(monkeypatch):
    monkeypatch.setattr("app.MODEL_PATH", ROOT / "missing-model.pkl")

    client = app.test_client()
    response = client.post("/", data={"iq": "120", "cgpa": "9.2"})

    assert response.status_code == 200
    assert b"The main model is unavailable." in response.data
    assert b"Prediction:" not in response.data
