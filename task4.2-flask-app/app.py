import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return (
        "<h1>Hello from Task 4.2!</h1>"
        f"<p>Served by container: <b>{socket.gethostname()}</b></p>"
        "<p>This is a basic containerized Flask application "
        "(SWE40006 Deployment Task 4.2).</p>"
    )


@app.route("/health")
def health():
    return jsonify(status="ok", hostname=socket.gethostname())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Bind to 0.0.0.0 so the app is reachable from outside the container.
    app.run(host="0.0.0.0", port=port)
