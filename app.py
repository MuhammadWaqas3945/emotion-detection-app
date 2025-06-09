from flask import Flask, render_template, request
from emotion_detection_service.emotion_detection import emotion_detection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    text = ""
    if request.method == 'POST':
        text = request.form.get('text', '')
        result = emotion_detection(text)
    return render_template('index.html', result=result, text=text)

if __name__ == '__main__':
    app.run(debug=True)
