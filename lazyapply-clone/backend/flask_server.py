from flask import Flask, request
from autoapply import auto_apply

app = Flask(__name__)

@app.route("/start", methods=["POST"])
def trigger_apply():
    auto_apply()
    return {"status": "started"}

if __name__ == "__main__":
    app.run(port=5000)