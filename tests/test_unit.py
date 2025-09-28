import pytest
from app.disaster_app import DisasterPredictor

def test_predict_returns_valid_disaster():
    predictor = DisasterPredictor()
    result = predictor.predict("coastal", "summer")
    assert result in predictor.disasters["coastal"] or result in ["Earthquake", "Flood", "Wildfire", "Hurricane", "Tornado", "None"]
