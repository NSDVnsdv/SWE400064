import os
import socket
from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

APP_TITLE = os.environ.get("APP_TITLE", "Swinburne Task Tracker")

# In-memory task store (resets when the container restarts).
tasks = [
    {"id": 1, "text": "Containerize the Flask app", "done": True},
    {"id": 2, "text": "Write an optimized Dockerfile", "done": True},
    {"id": 3, "text": "Deploy publicly over HTTP", "done": False},
]
next_id = 4


@app.route("/")
def index():
    return render_template(
        "index.html",
        title=APP_TITLE,
        tasks=tasks,
        hostname=socket.gethostname(),
        now=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
    )


@app.route("/add", methods=["POST"])
def add_task():
    global next_id
    text = request.form.get("text", "").strip()
    if text:
        tasks.append({"id": next_id, "text": text, "done": False})
        next_id += 1
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "ok", "hostname": socket.gethostname()}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
