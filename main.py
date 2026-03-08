from flask import Flask, request, jsonify
from fitness_generator import generate_plan

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    goal = data.get("goal")

    plan = generate_plan(goal)

    return jsonify({"plan": plan})

if __name__ == "__main__":
    app.run(debug=True)
