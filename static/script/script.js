function showErrorMessage(message) {
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
}

async function validateForm() {
    const form = document.getElementById('cadastro-form');
    const formData = new FormData(form);

    try {
        const response = await fetch('/cadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams(formData)
        });
        if (response.status === 200) {
            // Email cadastrado com sucesso, redireciona para a página de confirmação
            window.location.href = '/verifique_seu_email';
          
        } else if (response.status === 400) {
            // O email já está cadastrado, exibe a mensagem de erro
            const data = await response.json();
            const errorMessage = data.detail || "Email já cadastrado no sistema.";
            showErrorMessage(errorMessage);
        
        }else if (response.status === 409) {
            const data2 = await response.json();
            const errorMessage2 = data2.detail2 || "O usuário já existe no sistema.";
            showErrorMessage(errorMessage2);
        
        }else {
            // Outros erros
            const errorMessage = "Ocorreu um erro. Tente novamente.";
            showErrorMessage(errorMessage);
        }
    } catch (error) {
        console.error(error);
    }
}
