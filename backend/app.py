from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ldap_utils import get_user_info
#import fake_ad
import json
import os

# Caminho absoluto para o diretório base
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

app = Flask(__name__, static_folder=FRONTEND_DIR)
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

MODIFIED_FILE = os.path.join(os.path.dirname(__file__), "usuarios_modificados.json")


def save_modification(username, updates):
    data = {}
    if os.path.exists(MODIFIED_FILE):
        with open(MODIFIED_FILE, "r") as f:
            try:
                data = json.load(f)
            except:
                data = {}

    if username not in data:
        data[username] = {}

    data[username].update(updates)

    with open(MODIFIED_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.route("/api/user/<username>", methods=["GET"])
def get_user(username):
    info = get_user_info(username)
    if not info:
        return jsonify({"error": "Usuário não encontrado"}), 404

    if os.path.exists(MODIFIED_FILE):
        with open(MODIFIED_FILE, "r") as f:
            try:
                data = json.load(f)
                if username in data:
                    info.update(data[username])
            except:
                pass

    return jsonify(info)

@app.route("/api/user/update", methods=["POST"])
def update_user():
    content = request.json
    username = content.get("username")
    updates = {
        "name": content.get("name"),
        "email": content.get("email"),
        "company": content.get("company"),
        "department": content.get("department"),
        "title": content.get("title")
    }
    save_modification(username, updates)
    return jsonify({"message": "Usuário atualizado com sucesso (simulado)"}), 200

@app.route("/api/user/password", methods=["POST"])
def update_password():
    content = request.json
    username = content.get("username")
    new_password = content.get("new_password")
    save_modification(username, {"senha": new_password})
    return jsonify({"message": "Senha atualizada com sucesso (simulado)"}), 200

@app.route("/api/user/unlock", methods=["POST"])
def unlock_user():
    content = request.json
    username = content.get("username")
    action = content.get("action")  # "unlock" ou "lock"
    save_modification(username, {"locked": False if action == "unlock" else True})
    return jsonify({"message": f"Usuário {'desbloqueado' if action == 'unlock' else 'bloqueado'} com sucesso (simulado)"}), 200

if __name__ == "__main__":
    print("✅ Servidor AD simulado carregado com sucesso.")
    app.run(debug=True, host='0.0.0.0', port=5000)
