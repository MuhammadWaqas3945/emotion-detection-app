from flask import Flask, request, jsonify, render_template
from emotion_detection_service.emotion_detection import detect_emotion

import os

app = Flask(__name__, template_folder='../routes')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_api():
    data = request.get_json()
    text = data.get("text", "")
    emotion = detect_emotion(text)
    return jsonify({'emotion': emotion})

if __name__ == '__main__':
    app.run(debug=True)
