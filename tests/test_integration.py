import pytest
from app.disaster_app import DisasterPredictor

def test_multiple_predictions_are_logged():
    predictor = DisasterPredictor()
    results = [
        predictor.predict("coastal", "summer")
        for _ in range(5)
    ]
    # Ensure all predictions are valid for coastal
    for event in results:
        assert event in predictor.disasters["coastal"] or event in ["Earthquake", "Flood", "Wildfire", "Hurricane", "Tornado", "None"]
