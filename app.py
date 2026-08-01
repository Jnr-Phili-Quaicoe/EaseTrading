import os

from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.get("/")
def home():
    """Render the complete easeTrading learning interface."""
    return render_template("index.html")


@app.get("/health")
def health():
    """Health endpoint used by Render to verify the service."""
    return jsonify(status="healthy", service="easeTrading")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
