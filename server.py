from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')  # uses the provided templates/index.html

# Route for emotion detection
@app.route('/emotionDetector')
def emotionDetector():
    # Get the statement from the URL query string
    statement = request.args.get('textToAnalyze')

    # Call the emotion detector function
    result = emotion_detector(statement)

    # Build customer-friendly text
    text_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )

    # Return the text response
    return text_response

if __name__ == "__main__":
    app.run(debug=True, port=5001)