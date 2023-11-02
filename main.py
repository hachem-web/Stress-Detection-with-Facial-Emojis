from flask import Flask, request, redirect, url_for, render_template
import tensorflow as tf
import numpy as np
import cv2
from io import BytesIO

app = Flask(__name__)

MODEL_PATH = "stressDetecttor_2"
model = tf.saved_model.load(MODEL_PATH)

class_names = ['nostress', 'stress']

def extract_face(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) == 0:
        return None
    (x, y, w, h) = faces[0]
    return image[y:y+h, x:x+w]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        files = request.files.getlist("file")
        results = []
        for file in files:
            img_bytes = BytesIO(file.read())
            file_bytes = np.frombuffer(img_bytes.getvalue(), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            face_image = extract_face(image)

            if face_image is not None:
                resized_face = cv2.resize(face_image, (48, 48))
                img_array = tf.keras.preprocessing.image.img_to_array(resized_face)
                img_array = tf.expand_dims(img_array, 0)
                predictions = model(img_array)
                score = tf.nn.softmax(predictions[0])
                predicted_class = class_names[np.argmax(score)]
                confidence_percentage = 100 * np.max(score)
                result_str = f"{predicted_class}  {confidence_percentage:.2f}% "
                results.append(result_str)
            else:
                results.append("verifier cette image ")

        # Remove any empty results from the list
        results = [result for result in results if result]

        return redirect(url_for('accueil', results=results))

    return render_template("index.html")

@app.route('/accueil')
def accueil():
    results = request.args.getlist('results')
    return render_template('accueil.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
