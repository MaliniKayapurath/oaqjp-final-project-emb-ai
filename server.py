

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page using the provided index.html template."""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Handle GET requests to /emotionDetector.
    Returns emotion analysis for the provided text or an error message
    if input is blank.
    The dominant emotion is displayed in bold.
    """
    statement = request.args.get('textToAnalyze')
    result = emotion_detector(statement)

    # Handle blank input or API error
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Build response with dominant emotion in bold
    text_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )

    return text_response


if __name__ == "__main__":
    app.run(debug=True, port=5001)
