import cv2
import requests
import signal
import sys

url = "http://127.0.0.1:5000/process_video"

# Open the webcam
cap = cv2.VideoCapture(0)

def cleanup_and_exit(signal, frame):
    print("Exiting gracefully...")
    cap.release()
    cv2.destroyAllWindows()
    sys.exit(0)

# Set up a signal handler for KeyboardInterrupt
signal.signal(signal.SIGINT, cleanup_and_exit)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to bytes
    _, img_encoded = cv2.imencode('.jpg', frame)
    video_data = img_encoded.tobytes()

    # Send the frame as video input to the server
    response = requests.post(url, data=video_data)

    if response.status_code == 200:
        result = response.json()
        value = result.get("text_output")
        if value is not None: 
            print("Text Output:", result['text_output'])
        else:
            print("Text Output:", result['ocr_result'])
    else:
        print("Error:", response.status_code, response.text)