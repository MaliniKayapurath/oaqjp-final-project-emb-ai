import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the Watson NLP emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Handle blank input
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Request payload
    myobj = {"raw_document": {"text": text_to_analyse}}
    
    # Custom header specifying the model ID
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send POST request
    response = requests.post(url, json=myobj, headers=header)

    # Handle API returning status_code 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parse JSON response
    response_dict = json.loads(response.text)
    
    # Extract emotions from API response
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Build result dictionary
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    
    # Find dominant emotion
    dominant_emotion = max(result, key=result.get)
    result['dominant_emotion'] = dominant_emotion
    
    return result
