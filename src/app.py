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


if __name__ == "__main__":
    app_port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=app_port)
