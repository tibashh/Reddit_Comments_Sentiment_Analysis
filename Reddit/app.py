from flask import Flask, request, jsonify
import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Label mapping
label_map = {-1: "negative", 0: "neutral", 1: "positive"}

# Initialize Flask app
app = Flask(__name__)

# Prediction logic
def predict_sentence(text):
    X_new = vectorizer.transform([text])
    pred = model.predict(X_new)[0]

    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(X_new)[0]
        prob_dict = {label_map[label]: round(probs[i], 3)
                     for i, label in enumerate(model.classes_)}
    else:
        prob_dict = None

    return int(pred), label_map[pred], prob_dict

# ✅ Optional root route
@app.route('/', methods=['GET'])
def home():
    return "✅ Reddit Sentiment API is running! Use POST /predict with JSON {\"text\": \"...\"}"

# 🚀 /predict POST route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        if not data or 'text' not in data:
            return jsonify({'error': 'Missing "text" field'}), 400

        text = data['text']
        if not text.strip():
            return jsonify({'error': 'Text cannot be empty'}), 400

        pred_label, pred_name, pred_probs = predict_sentence(text)

        return jsonify({
            'label': pred_label,
            'sentiment': pred_name,
            'probabilities': pred_probs
        })

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

# 🔁 Start the server
if __name__ == '__main__':
    app.run(debug=True)
