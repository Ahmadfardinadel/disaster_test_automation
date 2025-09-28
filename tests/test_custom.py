from app.disaster_app import DisasterPredictor

def test_mountain_winter_prediction():
    predictor = DisasterPredictor()
    result = predictor.predict("mountain", "winter")
    assert result in predictor.disasters["mountain"] or result in ["Earthquake", "Flood", "Wildfire", "Hurricane", "Tornado", "None"]
