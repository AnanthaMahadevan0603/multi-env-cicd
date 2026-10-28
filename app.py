import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    env = os.environ.get("APP_ENV", "unknown")
    return f"Hello from the {env.upper()} environment - version 1"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
