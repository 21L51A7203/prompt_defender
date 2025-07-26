from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def detect_injection(prompt):
    injected_keywords = ["forget", "ignore", "bypass", "jailbreak", "override", "you are not", "act like", "disregard"]
    injected_score = sum(1 for word in injected_keywords if word in prompt.lower())
    clean_score = 1  # constant clean score for comparison

    verdict = "Injected" if injected_score >= clean_score else "Clean"

    return clean_score, injected_score, verdict

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    prompt = request.json.get("prompt", "")
    clean_score, injected_score, verdict = detect_injection(prompt)

    suggestions = []
    if verdict == "Injected":
        suggestions = [
            "🚫 Avoid using phrases like 'Forget you are an assistant'",
            "🧩 Split complex instructions into multiple prompts",
            "🛡️ Do not attempt to bypass AI rules or filters"
        ]
    else:
        suggestions = [
            "✅ Your prompt looks safe!",
            "💡 Use clear and specific instructions for best results"
        ]

    return jsonify({
        "clean_score": clean_score,
        "injected_score": injected_score,
        "verdict": verdict,
        "suggestions": suggestions
    })

if __name__ == "__main__":
    app.run(debug=True)
