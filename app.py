from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate_text():
    try:
        data = request.json
        english_text = data.get("text", "").strip()
        
        if not english_text:
            return jsonify({"error": "No text provided"}), 400
        
        # Translate English to Kannada
        translator = GoogleTranslator(source='en', target='kn')
        kannada_text = translator.translate(english_text)
        
        return jsonify({"kannada_text": kannada_text})
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({"error": f"Translation error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
