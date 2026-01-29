from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"translation": ""})

        translated = GoogleTranslator(
            source="en",
            target="kn"
        ).translate(text)

        return jsonify({"translation": translated})

    except Exception as e:
        print("TRANSLATION ERROR:", e)
        return jsonify({"error": "Translation service not available"}), 500


# ❌ DO NOT use app.run() on Render
# Gunicorn will start the app
