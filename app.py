from flask import Flask, request, render_template
import joblib  # For loading .joblib models
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model_path = "tuned_random_forest.joblib"  # Specify the path to your model file
model = joblib.load(model_path)  # Use joblib to load the model

@app.route("/")
def home():
    # Render the home page with no prediction initially
    return render_template("index.html", prediction=None, error=None)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Map 'type' input (L, M, H) to numerical values
        type_map = {"L": 0, "M": 1, "H": 2}
        type_value = type_map.get(request.form.get("type"))

        if type_value is None:
            raise ValueError("Invalid type selected. Please choose L, M, or H.")

        # Extract and validate other features
        air_temperature_c = float(request.form["air_temperature_c"])
        process_temperature_c = float(request.form["process_temperature_c"])
        rotational_speed_rpm = float(request.form["rotational_speed_rpm"])
        torque_nm = float(request.form["torque_nm"])
        tool_wear_min = float(request.form["tool_wear_min"])

        # Ensure values are within valid ranges
        if not (0 <= air_temperature_c <= 100):
            raise ValueError("Air Temperature must be between 0 and 100.")
        if not (0 <= process_temperature_c <= 100):
            raise ValueError("Process Temperature must be between 0 and 100.")

        # Combine features into a single array for prediction
        features = [
            type_value,
            air_temperature_c,
            process_temperature_c,
            rotational_speed_rpm,
            torque_nm,
            tool_wear_min,
        ]

        # Predict using the model
        prediction = model.predict([features])[0]

        # Map the prediction result to a failure type
        failure_mapping = {
            1: "No Failure",
            2: "Power Failure",
            3: "Tool Wear Failure",
            4: "Overstrain Failure",
            5: "Random Failures",
            6: "Heat Dissipation Failure",
        }
        result = failure_mapping.get(prediction, "Unknown Failure Type")
        
        # Return the prediction result and form inputs
        return render_template(
            "index.html",
            prediction=result,
            error=None,
            type=request.form["type"],
            air_temperature_c=request.form["air_temperature_c"],
            process_temperature_c=request.form["process_temperature_c"],
            rotational_speed_rpm=request.form["rotational_speed_rpm"],
            torque_nm=request.form["torque_nm"],
            tool_wear_min=request.form["tool_wear_min"],
        )

    except Exception as e:
        # Handle errors and display error messages
        return render_template(
            "index.html",
            prediction=None,
            error=str(e),
            type=request.form.get("type"),
            air_temperature_c=request.form.get("air_temperature_c"),
            process_temperature_c=request.form.get("process_temperature_c"),
            rotational_speed_rpm=request.form.get("rotational_speed_rpm"),
            torque_nm=request.form.get("torque_nm"),
            tool_wear_min=request.form.get("tool_wear_min"),
        )

if __name__ == "__main__":
    # Run the app in debug mode for development
    app.run(debug=True)
