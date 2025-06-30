
let dadosUsuario = null;
let dadosOriginais = null;

async function consultarUsuario() {
    const username = document.getElementById("usuario").value;
    const resultado = document.getElementById("resultado");
    const infoCampos = document.getElementById("infoCampos");

    resultado.style.display = "none";
    infoCampos.innerHTML = "";
    document.getElementById("acoes").style.display = "none";
    document.getElementById("editarBox").style.display = "none";
    document.getElementById("senhaBox").style.display = "none";

    if (!username) {
        alert("Digite o nome de usuário!");
        return;
    }

    try {
        const res = await fetch(`http://192.168.2.120:5000/api/user/${username}`);
        const data = await res.json();

        if (res.ok) {
            dadosUsuario = { ...data };
            dadosOriginais = { ...data };

            infoCampos.innerHTML = `
                <p><strong>Nome:</strong> ${data.name}</p>
                <p><strong>Email:</strong> ${data.email}</p>
                <p><strong>Empresa:</strong> ${data.company}</p>
                <p><strong>Setor:</strong> ${data.department}</p>
                <p><strong>Cargo:</strong> ${data.title}</p>
                <p><strong>Status:</strong> 
                    <span class="${data.locked ? 'tag-bloqueado' : 'tag-ativo'}">
                        ${data.locked ? 'Bloqueado' : 'Ativo'}
                    </span>
                    <span class="link-acao ${data.locked ? 'link-desbloquear' : 'link-bloquear'}"
                          onclick="alternarBloqueio()">
                        ${data.locked ? 'desbloquear usuário' : 'bloquear usuário'}
                    </span>
                </p>
            `;

            document.getElementById("acoes").style.display = "block";
            infoCampos.style.display = "block";
            resultado.style.display = "block";
        } else {
            infoCampos.innerHTML = `<p style="color:red;"><strong>Erro:</strong> ${data.error}</p>`;
            resultado.style.display = "block";
        }
    } catch (err) {
        infoCampos.innerHTML = `<p style="color:red;">Erro na consulta.</p>`;
        resultado.style.display = "block";
    }
}

function editarCampos() {
    document.getElementById("infoCampos").style.display = "none";
    document.getElementById("senhaBox").style.display = "none";

    document.getElementById("acoes").style.display = "none";

    const box = document.getElementById("editarBox");
    box.innerHTML = `
        <p><strong>Nome:</strong></p>
    <input type="text" id="editNome" value="${dadosUsuario.name}" />

    <p><strong>Email:</strong></p>
    <input type="text" id="editEmail" value="${dadosUsuario.email}" />

    <p><strong>Empresa:</strong></p>
    <input type="text" id="editEmpresa" value="${dadosUsuario.company}" />

    <p><strong>Setor:</strong></p>
    <input type="text" id="editSetor" value="${dadosUsuario.department}" />

    <p><strong>Cargo:</strong></p>
    <input type="text" id="editCargo" value="${dadosUsuario.title}" />

    <button class="btn-verde" onclick="confirmarEdicao()">Confirmar Alterações</button>
    <button class="btn-vermelho" onclick="cancelarEdicao()">Cancelar</button>
    `;
    box.style.display = "block";
}

function confirmarEdicao() {
    dadosUsuario.name = document.getElementById("editNome").value;
    dadosUsuario.email = document.getElementById("editEmail").value;
    dadosUsuario.company = document.getElementById("editEmpresa").value;
    dadosUsuario.department = document.getElementById("editSetor").value;
    dadosUsuario.title = document.getElementById("editCargo").value;

    fetch("http://192.168.2.120:5000/api/user/update", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: document.getElementById("usuario").value, ...dadosUsuario })
    });

    alert("Alterações salvas.");
    document.getElementById("editarBox").style.display = "none";
    consultarUsuario();
    document.getElementById("acoes").style.display = "block";

}

function cancelarEdicao() {
    document.getElementById("editarBox").style.display = "none";
    document.getElementById("infoCampos").style.display = "block";
    document.getElementById("acoes").style.display = "block";

}

function exibirCampoSenha() {
    document.getElementById("infoCampos").style.display = "none";
    document.getElementById("editarBox").style.display = "none";

    document.getElementById("acoes").style.display = "none";


    document.getElementById("senhaBox").innerHTML = `
        <input type="password" id="novaSenha" placeholder="Nova senha"/>
        <button class="btn-verde" onclick="confirmarSenha()">Confirmar Senha</button>
        <button class="btn-vermelho" onclick="cancelarSenha()">Cancelar</button>
    `;
    document.getElementById("senhaBox").style.display = "block";
}

function confirmarSenha() {
    const senha = document.getElementById("novaSenha").value;

    fetch("http://192.168.2.120:5000/api/user/password", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: document.getElementById("usuario").value, new_password: senha })
    });

    alert("Senha alterada.");
    document.getElementById("senhaBox").style.display = "none";
    consultarUsuario();
    document.getElementById("acoes").style.display = "block";

}

function cancelarSenha() {
    document.getElementById("senhaBox").style.display = "none";
    document.getElementById("infoCampos").style.display = "block";
    document.getElementById("acoes").style.display = "block";

}

function alternarBloqueio() {
    const locked = dadosUsuario.locked;
    const action = locked ? "unlock" : "lock";

    fetch("http://192.168.2.120:5000/api/user/unlock", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: document.getElementById("usuario").value, action })
    });

    alert(locked ? "Usuário desbloqueado." : "Usuário bloqueado.");
    consultarUsuario();
}
