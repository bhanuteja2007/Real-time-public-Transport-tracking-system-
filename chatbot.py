from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)
# Example intents and responses
responses = {
    "greeting": ["Hello! How can I assist you with Punjab Transport Tracking today?"],
    "bus_status": ["You can track your bus in real-time via the Punjab Transport official website or mobile app."],
    "schedule": ["Bus schedules are available on our website. Please specify your route or bus number for details."],
    "fare": ["Fares depend on the route and distance. Please provide your source and destination."],
    "complaint": ["To register a complaint, please visit the Punjab Transport portal or call the customer helpline."],
    "thanks": ["You're welcome! If you have more questions, feel free to ask."],
    "default": ["Sorry, I didn't understand that. Could you please rephrase?"]
}

# Simple intent recognition using keywords
def get_intent(text):
    text = text.lower()
    if any(greet in text for greet in ["hello", "hi", "hey"]):
        return "greeting"
    elif re.search(r"\btrack.*bus\b", text):
        return "bus_status"
    elif re.search(r"\bschedule\b", text):
        return "schedule"
    elif re.search(r"\bfare\b", text):
        return "fare"
    elif any(word in text for word in ["complaint", "problem", "issue"]):
        return "complaint"
    elif any(word in text for word in ["thank", "thanks"]):
        return "thanks"
    else:
        return "default"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    intent = get_intent(user_input)
    response = responses[intent][0]
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
