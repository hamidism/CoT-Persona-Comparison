from flask import Flask, render_template, request, jsonify
from client import ask

app = Flask(__name__)

# Kuch ready-made reasoning questions to test with
PRESET_QUESTIONS = [
    "A factory has two machines. Machine A can complete one production batch in 8 hours. Machine B is 50% slower than Machine A. If both machines start working together at the same time, how many hours will it take them to complete one batch together?",
    "A software company spent $50,000 developing a new product feature. Market research now shows that if they launch it, it will bring in $30,000 in additional revenue. If they don't launch it, they can instead sell the feature's codebase to another company for $10,000. If they do neither, the codebase becomes worthless. Development is already complete and the $50,000 is already spent either way. What should the company do?",
    "A pen and a notebook together cost $1.10. The notebook costs $1.00 more than the pen. How much does the pen cost?",
    "Ali, Bilal, and Ahmed each play a different sport: cricket, football, or badminton. Bilal does not play football or badminton. Ahmed does not play badminton. Ali does not play cricket. Who plays which sport?",
]


@app.route("/")
def home():
    return render_template("index.html", presets=PRESET_QUESTIONS)


@app.route("/api/compare", methods=["POST"])
def compare():
    data = request.get_json()
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "No question provided"}), 400

    # RUN 1: Plain prompt — no reasoning instruction, no persona
    plain_messages = [
        {"role": "user", "content": question}
    ]
    plain_answer = ask(plain_messages)

    # RUN 2: Chain-of-Thought + Persona
    cot_messages = [
        {"role": "system", "content": "You are a senior analyst who reasons carefully and rigorously before answering."},
        {"role": "user", "content": question + "\n\nThink step-by-step before giving your final answer."},
    ]
    cot_answer = ask(cot_messages)

    return jsonify({"plain": plain_answer, "cot": cot_answer})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
