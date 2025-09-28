import subprocess

def test_app_runs_and_exits():
    process = subprocess.run(
        ["python3", "run_app.py"],
        input="coastal\nsummer\nno\n",   # simulate user input
        capture_output=True,
        text=True
    )
    # The app should show prediction and exit message
    assert "Interactive Disaster Prediction System" in process.stdout
    assert "Exiting Disaster Prediction System" in process.stdout
