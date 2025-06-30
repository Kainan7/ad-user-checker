from ldap3 import Server, Connection, MOCK_SYNC
from fake_ad import server, conn  # importa o servidor simulado

def get_user_info(username):
    search_filter = f"(sAMAccountName={username})"
    conn.search('dc=grupofan,dc=local', search_filter, attributes=[
        'displayName', 'mail', 'company', 'department', 'title', 'userAccountControl'
    ])

    if not conn.entries:
        return None

    entry = conn.entries[0]
    user_control = int(entry.userAccountControl.value)

    is_locked = user_control & 2 or user_control & 16  # flags: 2 = desabilitado, 16 = bloqueado

    return {
        "username": username,
        "name": entry.displayName.value,
        "email": entry.mail.value,
        "company": entry.company.value,
        "department": entry.department.value,
        "title": entry.title.value,
        "locked": bool(is_locked)
    }
