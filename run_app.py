from app.disaster_app import DisasterPredictor

def main():
    print("🌍 Interactive Disaster Prediction System")
    print("Answer a few questions to predict the most likely disaster.\n")

    predictor = DisasterPredictor()

    while True:
        # Ask questions
        location = input("Where are you located? (coastal/mountain/city/desert): ").strip()
        season = input("What season is it? (spring/summer/fall/winter): ").strip()

        # Predict
        disaster = predictor.predict(location, season)
        print(f"\n⚠️ Based on your location and season, the predicted disaster is: {disaster}\n")

        # Continue?
        again = input("Do you want another prediction? (yes/no): ").strip().lower()
        if again != "yes":
            print("Exiting Disaster Prediction System...")
            break

if __name__ == "__main__":
    main()
