from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'YOUR_IBM_WATSON_NLU_API_KEY'
URL = 'YOUR_IBM_WATSON_NLU_URL'

def analyze_emotion(text):
    headers = {'Content-Type': 'application/json'}
    payload = {
        "text": text,
        "features": {
            "emotion": {}
        }
    }
    response = requests.post(
        f"{URL}/v1/analyze?version=2021-08-01",
        headers=headers,
        auth=('apikey', API_KEY),
        json=payload
    )
    emotion = response.json()['emotion']['document']['emotion']
    return emotion

@app.route('/', methods=['GET', 'POST'])
def home():
    emotion_result = None
    if request.method == 'POST':
        text = request.form['text']
        emotion_result = analyze_emotion(text)
    return render_template('index.html', result=emotion_result)

if __name__ == '__main__':
    app.run(debug=True)
