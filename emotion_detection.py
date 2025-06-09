def emotion_detection(text):
    text_lower = text.lower()
    emotions = {
        "dominant_emotion": "neutral",
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0
    }

    if "happy" in text_lower or "joy" in text_lower:
        emotions["dominant_emotion"] = "joy"
        emotions["joy"] = 0.9
    elif "sad" in text_lower or "unhappy" in text_lower:
        emotions["dominant_emotion"] = "sadness"
        emotions["sadness"] = 0.9
    elif "angry" in text_lower or "mad" in text_lower:
        emotions["dominant_emotion"] = "anger"
        emotions["anger"] = 0.9
    elif "fear" in text_lower or "scared" in text_lower:
        emotions["dominant_emotion"] = "fear"
        emotions["fear"] = 0.9
    elif "disgust" in text_lower or "gross" in text_lower:
        emotions["dominant_emotion"] = "disgust"
        emotions["disgust"] = 0.9
    else:
        emotions["dominant_emotion"] = "neutral"

    return emotions
