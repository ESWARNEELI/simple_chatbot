from flask import Flask, request, jsonify, render_template
from google import genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


client = genai.Client(api_key="REMOVED A")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("prompt")

    stream = client.models.generate_content_stream(
        model="models/gemini-flash-latest",
        contents=user_input
    )

    response_text = ""
    for chunk in stream:
        if chunk.text:
            response_text += chunk.text

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)

