import os
import threading
import subprocess
from flask import Flask

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 8080))


@app.route("/")
def home():
    return "Extractor Pro X is running!"


def run_flask():
    app.run(host="0.0.0.0", port=PORT, use_reloader=False)


if __name__ == "__main__":
    # Start the HTTP server required by Render Web Service.
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Start the Telegram bot.
    # Keeping this as a subprocess preserves the repository's existing
    # "python -m Extractor" startup behavior.
    process = subprocess.run(["python", "-m", "Extractor"])
    raise SystemExit(process.returncode)
