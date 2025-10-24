from flask import Flask, render_template, request
import os
from preprocess_audio import preprocess_audio
from transcribe_tamil import transcribe_audio

app = Flask(__name__, template_folder='templates', static_folder='static')
UPLOADS_DIR = 'uploads'
PREPROCESSED_DIR = 'preprocessed'
OUTPUTS_DIR = 'outputs'

# Ensure directories exist
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(PREPROCESSED_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return 'No file part', 400
    file = request.files['audio']
    if file.filename == '':
        return 'No selected file', 400
    filepath = os.path.join(UPLOADS_DIR, file.filename)
    file.save(filepath)
    # Preprocess and transcribe
    preprocessed_path = os.path.join(PREPROCESSED_DIR, os.path.splitext(file.filename)[0] + '_preprocessed.wav')
    preprocess_audio(filepath, preprocessed_path)
    output_path = os.path.join(OUTPUTS_DIR, os.path.splitext(file.filename)[0] + '_preprocessed.txt')
    transcribe_audio(preprocessed_path, output_path)
    # Return the transcription text
    with open(output_path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True)
