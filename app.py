from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive 😊"
    elif analysis.sentiment.polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

@app.route('/get_sentiment', methods=['POST'])
def sentiment():
    data = request.get_json()
    message = data.get("message", "")
    sentiment_result = get_sentiment(message)
    return jsonify({"sentiment": sentiment_result})

if __name__ == '__main__':
    app.run(debug=True)
