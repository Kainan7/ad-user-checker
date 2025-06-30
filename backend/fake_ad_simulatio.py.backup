from ldap3 import Server, Connection, MOCK_SYNC, OFFLINE_AD_2012_R2

#define um servidor fake com estrutura AD
server = Server("fake_ad_server" , get_info=OFFLINE_AD_2012_R2)

#conexão em modo simulado
conn = Connection(server, user="cn= admin,dc=grupofan,dc=local", password="123", client_strategy=MOCK_SYNC)
conn.bind()

#adiciona uma base DN fictícia
conn.strategy.add_entry('dc=grupofan,dc=local', {
	'objectClass': ['domain'],
	'dc': 'grupofan'
})

# Adiciona usuários fictícios
usuarios = [
    {
        'cn': 'joao.silva',
        'displayName': 'João Silva',
        'sAMAccountName': 'joao.silva',
        'mail': 'joao.silva@grupofan.com.br',
        'company': 'Fanlog',
        'department': 'TI',
        'title': 'Analista de Suporte',
        'userAccountControl': '512'  # habilitado
    },
    {
        'cn': 'maria.souza',
        'displayName': 'Maria Souza',
        'sAMAccountName': 'maria.souza',
        'mail': 'maria.souza@grupofan.com.br',
        'company': 'Fancred',
        'department': 'Financeiro',
        'title': 'Coordenadora Financeira',
        'userAccountControl': '514'  # desabilitado/bloqueado
    }
]

for user in usuarios:
    dn = f"cn={user['cn']},dc=grupofan,dc=local"
    conn.strategy.add_entry(dn, {
        'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
        **user
    })

print("✅ Servidor AD simulado carregado com sucesso.")
