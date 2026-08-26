import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import predict_placement


def test_predict_placement_for_good_student():
    result = predict_placement(120, 9.2)
    assert result in {"Placed", "Not Placed"}


def test_predict_placement_for_low_student():
    result = predict_placement(60, 5.0)
    assert result in {"Placed", "Not Placed"}
