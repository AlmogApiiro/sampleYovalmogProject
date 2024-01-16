from flask import Flask, render_template, request, jsonify
import time
import cv2
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

app = Flask(__name__)
model = tf.keras.Sequential([hub.KerasLayer("https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4", input_shape=(224,224,3))])

def predict_image(image_data):
    # Convert the image data to a NumPy array
    image_array = cv2.imdecode(np.frombuffer(image_data, np.uint8), -1)

    # Resize the image to match the input size expected by the model
    resized_image = cv2.resize(image_array, (224, 224))

    # Normalize pixel values to be between 0 and 1
    normalized_image = resized_image / 255.0

    # Add an extra dimension to the image array to match the model's expected format
    input_image = tf.expand_dims(normalized_image, axis=0)

    # Make the prediction
    result = model.predict(input_image)

    # Get the predicted label
    predicted_label_index = np.argmax(result, axis=-1)
    
    # Decode the label using ImageNet labels (for demonstration purposes)
    labels_path = tf.keras.utils.get_file('ImageNetLabels.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
    with open(labels_path) as f:
        labels = f.read().splitlines()

    predicted_label = labels[predicted_label_index[0]]

    return predicted_label

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_video', methods=['POST'])
def process_video():
    # Receive video input (in a real scenario, you would process the video here)
    video_data = request.data

    # Mock video processing delay
    time.sleep(2)

    # Use the machine learning model to predict the content of the image
    prediction_result = predict_image(video_data)

    # Return the text output
    return jsonify({'text_output': prediction_result})

if __name__ == '__main__':
    app.run(debug=True)
