function clearErrorMessages() {
    const errorMessages = document.getElementsByClassName('error-message');
    while (errorMessages[0]) {
        errorMessages[0].parentNode.removeChild(errorMessages[0]);
    }
}

function showErrorMessage(message, fieldId) {
    const field = document.getElementById(fieldId);
    if (!field) {
        console.error(`Campo com id ${fieldId} não encontrado.`);
        return;
    }

    // Remove qualquer mensagem de erro existente
    const existingError = field.parentNode.querySelector('.error-message');
    if (existingError) {
        field.parentNode.removeChild(existingError);
    }

    const errorElement = document.createElement('p');
    errorElement.className = 'error-message';
    errorElement.textContent = message;
    errorElement.style.color = 'red';

    field.parentNode.appendChild(errorElement);
}

async function validateForm() {
    const form = document.getElementById('cadastro-form');
    const formData = new FormData(form);

    // Primeiro, limpe as mensagens de erro existentes
    clearErrorMessages();

    // Aqui, você pode adicionar a lógica para verificar se as senhas correspondem
    // Se não, mostre uma mensagem de erro e retorne
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('password2').value;
    if (password !== confirmPassword) {
        showErrorMessage('As senhas não correspondem.', 'password2');
        return;
    }

    try {
        const response = await fetch('/cadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams(formData)
        });

        if (response.status === 200) {
        
            window.location.href = '/verifique_seu_email';
        
        } else if (response.status === 400 || response.status === 409) {
            
            // Como o tratamento de erro é o mesmo para ambos os status, podemos combiná-los
            const data = await response.json();
            
            if (data.detail) {
                showErrorMessage(data.detail, 'email');
            
            } else if (data.detail2) {
                showErrorMessage(data.detail2, 'makeuser');
            
            } else {
                showErrorMessage("Ocorreu um erro. Tente novamente.", 'username');
            }
       
        } else if (response.status === 422) {
            const data = await response.json();
            // Aqui, você pode percorrer os erros e mostrar uma mensagem para cada um
            for (const error of data.errors) {
                showErrorMessage(error.detail, 'username');
            }
        } else {
            showErrorMessage('Ocorreu um erro. Tente novamente.', 'username');
        }
    } catch (error) {
        console.error(error);
    }
}
