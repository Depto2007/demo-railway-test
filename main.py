from flask import Flask, jsonify
import random

app = Flask(__name__)

texts = ["hello", "depto", "lorem", "ipsum", "world", "chatgpt", "railway"]

@app.route("/random-text", methods=["GET"])
def random_text():
    text = random.choice(texts)
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
