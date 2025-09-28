import random
from app.utils import log_event

class DisasterPredictor:
    def __init__(self):
        # Possible disasters
        self.disasters = {
            "coastal": ["Hurricane", "Flood", "Tornado", "None"],
            "mountain": ["Earthquake", "Wildfire", "Flood", "None"],
            "city": ["Flood", "Earthquake", "None"],
            "desert": ["Wildfire", "Earthquake", "None"],
        }

    def predict(self, location: str, season: str):
        """Predict a disaster based on location and season."""

        location = location.lower()

        # Default disasters if location is unknown
        possible = self.disasters.get(location, ["Earthquake", "Flood", "Wildfire", "Hurricane", "Tornado", "None"])

        # Season influences probabilities
        if season.lower() in ["summer", "spring"]:
            weights = [0.15, 0.25, 0.3, 0.1, 0.05, 0.15]  # Wildfires/Floods more likely
        elif season.lower() in ["winter"]:
            weights = [0.25, 0.3, 0.1, 0.2, 0.05, 0.1]   # Floods/Earthquakes more likely
        else:
            weights = [0.2] * len(possible)  # Equal probability if unknown season

        # Adjust weights to match disaster list
        while len(weights) > len(possible):
            weights.pop()
        while len(weights) < len(possible):
            weights.append(0.1)

        disaster = random.choices(possible, weights=weights, k=1)[0]
        log_event(f"Prediction for {location.title()} in {season.title()}: {disaster}")
        return disaster
