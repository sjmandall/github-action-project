from flask import Flask, request, jsonify, send_from_directory
import random

app = Flask(__name__)

emojis = {"r": "🪨", "p": "🗞️", "s": "✂️"}
choices = ["r", "p", "s"]

# 1️⃣ Route to serve index.html
@app.route("/")
def index():
    return send_from_directory('.', 'index.html')  # Serve index.html from current directory

# 2️⃣ Route for game API
@app.route("/play", methods=["GET"])
def play():
    user_input = request.args.get("choice")
    if user_input not in choices:
        return jsonify({"error": "Invalid choice! Use r, p, or s."}), 400

    computer_input = random.choice(choices)

    if user_input == computer_input:
        result = "TIE"
    elif (
        (user_input == "r" and computer_input == "s") or
        (user_input == "s" and computer_input == "p") or
        (user_input == "p" and computer_input == "r")
    ):
        result = "JEET GAYA!! COMPUTER KI MKC"
    else:
        result = "HAR GYA CHUTIYEE"

    return jsonify({
        "you": emojis[user_input],
        "computer": emojis[computer_input],
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

