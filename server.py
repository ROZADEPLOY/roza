import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://roza-webapp.onrender.com")

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/api/check_user", methods=["POST"])
def check_user():
    data = request.json
    user_id = int(data.get("user_id", 0))
    return jsonify({
        "success": True,
        "is_admin": user_id in ADMIN_IDS
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
