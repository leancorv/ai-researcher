import os
from flask import Flask
from src import agent
from src.output import save_result

app = Flask(__name__)

@app.route("/run", methods=["POST", "GET"])
def run_agent():
    topics = [
        "Coderhouse expansión latinoamérica 2025",
        "tendencias inteligencia artificial empresas 2025",
    ]
    for topic in topics:
        result = agent.run(topic)
        if result["status"] != "discarded":
            save_result(result)
    return "Agent ran successfully", 200

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)