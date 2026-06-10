from flask import Flask, jsonify
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Real-Time PostgreSQL SCADA Dashboard</h1>
    <p>Application is running.</p>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok"})
