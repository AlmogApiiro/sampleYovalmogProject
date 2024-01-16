# Project Setup Guide
### Clone the Repository
```bash
git clone <repository_url>
cd <repository_name>
```
### Create a Virtual Environment
```bash
# On Windows use python instead of python3
python3 -m venv venv
```
### Activate the Virtual Environment
```bash
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```

<br>

# Running the Application

### Start the Flask server:
```bash
# On Windows use python instead of python3

# OCR model
python3 ocr_app.py

# Image Classification model
python3 app.py
```

### Open the client script:
```bash
# On Windows use python instead of python3

python3 webcam_client.py
```