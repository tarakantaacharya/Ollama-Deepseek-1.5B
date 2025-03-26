from flask import Flask, render_template, request, Response
import requests
import json

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

def stream_response(question):
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": question,
        "stream": True
    }

    response = requests.post(OLLAMA_URL, headers={"Content-Type": "application/json"}, data=json.dumps(payload), stream=True)

    for line in response.iter_lines():
        if line:
            json_data = json.loads(line.decode("utf-8"))
            yield json_data.get("response", "") + " "

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    question = request.json["question"]
    return Response(stream_response(question), content_type="text/plain")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
