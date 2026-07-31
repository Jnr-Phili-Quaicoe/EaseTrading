from flask import Flask, render_template, request, jsonify
import hashlib

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/api/check-answer")
def check_answer():
    data = request.get_json(silent=True) or {}
    course = str(data.get("course", "security")).strip().lower()
    answer = str(data.get("answer", "")).strip().lower().replace(" ", "")
    if answer.endswith("()"):
        answer = answer[:-2]

    expected = {
        "security": "hashlib.sha256",
        "python": "def",
        "web": "<nav>",
    }
    correct = answer == expected.get(course, "")
    return jsonify({
        "correct": correct,
        "message": "Excellent! You passed the course." if correct else "Not correct yet. Use the hint and try again."
    })


@app.get("/api/demo-hash")
def demo_hash():
    text = request.args.get("text", "EasyLearning.edu")
    return jsonify({"text": text, "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
