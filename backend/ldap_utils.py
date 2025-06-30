from ldap3 import Server, Connection, ALL, NTLM, SUBTREE, SIMPLE

# ⚠️ Recomendado mover essas configs para variáveis de ambiente ou arquivo .env
LDAP_SERVER = '192.168.2.86'  # ou o IP do AD
LDAP_PORT = 389                # ou 636 se for LDAPS
LDAP_USER = 'fanad@fan2.com'  # usuário de consulta com permissões mínimas
LDAP_PASSWORD = 'Kp1234567@'
LDAP_SEARCH_BASE = 'DC=fan2,DC=com'

def get_user_info(username):
    try:
        server = Server(LDAP_SERVER, port=LDAP_PORT, get_info=ALL)
        conn = Connection(
            server,
            user=LDAP_USER,
            password=LDAP_PASSWORD,
            authentication=SIMPLE,
            auto_bind=True
        )

        search_filter = f"(sAMAccountName={username})"
        conn.search(
            search_base=LDAP_SEARCH_BASE,
            search_filter=search_filter,
            search_scope=SUBTREE,
            attributes=[
                'displayName', 'mail', 'company', 'department',
                'title', 'userAccountControl'
            ]
        )

        if not conn.entries:
            return None

        entry = conn.entries[0]
        user_control = int(entry.userAccountControl.value)

        is_locked = user_control & 2 or user_control & 16  # 2 = desabilitado, 16 = bloqueado

        return {
            "username": username,
            "name": entry.displayName.value if entry.displayName else '',
            "email": entry.mail.value if entry.mail else '',
            "company": entry.company.value if entry.company else '',
            "department": entry.department.value if entry.department else '',
            "title": entry.title.value if entry.title else '',
            "locked": bool(is_locked)
        }

    except Exception as e:
        print(f"Erro ao conectar no AD: {e}")
        return None
