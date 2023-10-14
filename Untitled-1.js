// No momento do login
const usuario = document.getElementById('usuario').value;
const senha = document.getElementById('senha').value;

// Verifica se as informações de login estão corretas
const cadastro = JSON.parse(localStorage.getItem('cadastro'));
if (cadastro && cadastro.usuario === usuario && cadastro.senha === senha) {
    // Redireciona para a tela de boas-vindas
    window.location.href = "boas-vindas.html";
} else {
    document.getElementById('error-message').innerText = "Usuário ou senha incorretos";
}