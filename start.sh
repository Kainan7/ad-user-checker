#!/bin/bash

# Caminho base do projeto
APP_DIR="/home/ad-project/ad-user-checker"
BACKEND_DIR="$APP_DIR/backend"
VENV_DIR="$APP_DIR/venv"

echo "🔧 Criando ambiente virtual..."
python3 -m venv "$VENV_DIR"

echo "✅ Ativando ambiente virtual..."
source "$VENV_DIR/bin/activate"

echo "📦 Instalando dependências do requirements.txt..."
pip install --upgrade pip
pip install -r "$APP_DIR/requirements.txt"

echo "🚀 Testando aplicação Flask..."
export FLASK_APP="$BACKEND_DIR/app.py"
cd "$BACKEND_DIR"
flask run --host=0.0.0.0 --port=5000

echo ""
echo "✅ Teste finalizado. Pressione Ctrl+C para parar o servidor."
echo "⚙️ Para rodar em produção, ative o serviço systemd com:"
echo "  sudo systemctl enable ad-user-checker"
echo "  sudo systemctl start ad-user-checker"
