
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Flask Backend is Running Successfully!",
        "status": "success",
        "service": "Flask API"
    })

@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Hello from AWS Deployed Flask Backend!",
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
