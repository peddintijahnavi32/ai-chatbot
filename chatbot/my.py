from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

client = genai.Client(api_key="AIzaSyAWE1rNrKuPAVauKSdIk3MERe9shTE1eDE")  # ⚠️ keep private

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['query']

    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=user_input
    )

    return render_template(
        "index.html",
        user=user_input,
        result=response.text
    )

if __name__ == "__main__":
    app.run(debug=True)