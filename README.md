# AD User Checker

Sistema web para consulta e gerenciamento de usuários do Active Directory (AD) utilizando Python, Flask e LDAP3.

---

## 🧩 Funcionalidades

- Consulta de usuários do AD por nome
- Visualização de:
  - Nome
  - E-mail
  - Empresa
  - Setor
  - Cargo
  - Status (Ativo/Bloqueado)
- Edição de informações do usuário
- Alteração de senha
- Bloqueio e desbloqueio de contas
- Interface 100% integrada com backend via API REST
- Simulação local com `ldap3` (modo de teste)

---

## 🚀 Tecnologias utilizadas

- Python 3.11+
- Flask
- Flask-CORS
- LDAP3
- HTML + CSS + JavaScript

---

## 🛠️ Instalação e execução

1. Clone o repositório:

```bash
git clone https://github.com/Kainan7/ad-user-checker.git
cd ad-user-checker
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o backend simulado:

```bash
cd backend
python app.py
```

5. Abra o frontend:

```bash
cd ../frontend
Abra o arquivo index.html no navegador
```

---

## 🧪 Modo de Teste

O servidor AD simulado é carregado com dois usuários:

- `joao.silva`
- `maria.souza`

Eles podem ser alterados via interface ou diretamente no `usuarios_modificados.json`.

---

## 🔐 Observações

- Este projeto é uma simulação. Para uso com AD real, configure `config.py` com os dados do domínio da empresa.
- Para integração com Active Directory real, será necessário um usuário com permissões administrativas e uma rede com acesso ao servidor LDAP da empresa.

---

## 📁 Estrutura do Projeto

```
ad-user-checker/
├── backend/
│   ├── app.py
│   ├── fake_ad.py
│   ├── ldap_utils.py
│   └── usuarios_modificados.json
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── requirements.txt
└── README.md
```

---

## 📄 Licença

Projeto desenvolvido para fins acadêmicos e profissionais de infraestrutura/suporte interno. Uso livre com créditos.
