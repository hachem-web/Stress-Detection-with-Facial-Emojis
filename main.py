# Import necessary modules
from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from io import BytesIO

# Create a Flask app
app = Flask(__name__)

# Load the trained model
MODEL_PATH = "stressDetecttor_2"
model = tf.saved_model.load(MODEL_PATH)

# Define class names (replace with your own)
class_names = ['nostress', 'stress']

# Define the route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    prediction_result = None

    if request.method == "POST":
        # Get the uploaded image file
        file = request.files["file"]

        if file:
            # Convert the FileStorage object to BytesIO
            img_bytes = BytesIO(file.read())

            # Load and preprocess the image
            img = tf.keras.utils.load_img(img_bytes, target_size=(48, 48))
            img_array = tf.keras.utils.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0)

            # Make predictions using the model
            predictions = model(img_array)
            score = tf.nn.softmax(predictions[0])

            # Get the predicted class label and confidence
            predicted_class = class_names[np.argmax(score)]
            confidence_percentage = 100 * np.max(score)

            # Create a prediction result string
            prediction_result = f"This image most likely belongs to {predicted_class} with a {confidence_percentage:.2f}% confidence."

    return render_template("index.html", prediction_result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)
