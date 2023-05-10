from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return {
        "message": "Automate all the things!",
        "timestamp": int(datetime.now().timestamp()),
    }


@app.route("/version", methods=["GET"])
def version():
    app_version = os.environ.get("APP_VERSION", None)
    return {"version": app_version}


@app.route("/status", methods=["GET"])
def status():
    return {"status": "OK"}


if __name__ == "__main__":
    app_port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=app_port)
