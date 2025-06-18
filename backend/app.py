from flask import Flask, request, jsonify
from ldap_utils import get_user_info
import fake_ad  # garante que o servidor simulado seja carregado

app = Flask(__name__)

@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    info = get_user_info(username)
    if info:
        return jsonify(info)
    return jsonify({"error": "Usuário não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
