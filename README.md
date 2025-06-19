# ad-user-checker

# 🧠 AD User Checker – Simulador de Active Directory com Flask

Este projeto simula um servidor Active Directory (AD) e fornece uma API web usando Flask, que permite:

- Consultar usuários por login (sAMAccountName)
- Verificar se estão bloqueados ou não
- Exibir e-mail, setor, cargo e empresa

> ⚠️ Este projeto **não se conecta ao AD real** por enquanto – ele usa um ambiente simulado com `ldap3`.

---

## 🚀 Tecnologias utilizadas

- Python 3.11+
- Flask
- ldap3 (modo MOCK_SYNC – simulação local)
- Estrutura em `backend/` com API REST

---

## 🧩 Estrutura

```bash
ad-user-checker/
├── backend/
│   ├── app.py         # Servidor Flask
│   ├── fake_ad.py     # Simulador de AD com usuários de teste
│   ├── ldap_utils.py  # Função que consulta os dados
│   ├── config.py      # (Não usado agora – para AD real depois)
├── requirements.txt   # Dependências
├── README.md          # Este arquivo
├── frontend/          # (ainda em construção)

