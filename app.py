import os
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load your pre-trained Linear SVC or Logistic Regression model
# We load it at the start so it stays in memory
model, tfidf = pickle.load(open("model.pkl", "rb"))


@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    ticket_text = data.get("text", "")

    # Transform the text and predict
    vector = tfidf.transform([ticket_text])
    prediction = model.predict(vector)[0]

    return jsonify({"category": prediction})


if __name__ == "__main__":
    # Use environment variable for Port (required by App Platform)
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
