document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.form-with-validation');

    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            // Reset previous error states
            resetErrors(form);

            // Validate based on form type
            if (form.action.includes('login')) {
                if (!validateLoginForm(form)) {
                    event.preventDefault();
                }
            } else if (form.action.includes('register')) {
                if (!validateRegisterForm(form)) {
                    event.preventDefault();
                }і
            }
        });
    });

    function validateLoginForm(form) {
        const username = form.querySelector('#id_username');
        const password = form.querySelector('#id_password');
        let isValid = true;

        // Username validation
        if (!username.value.trim()) {
            showError(username, 'Username is required');
            isValid = false;
        }

        // Password validation
        if (!password.value.trim()) {
            showError(password, 'Password is required');
            isValid = false;
        }

        return isValid;
    }

    function validateRegisterForm(form) {
        const username = form.querySelector('#id_username');
        const password1 = form.querySelector('#id_password1');
        const password2 = form.querySelector('#id_password2');
        let isValid = true;

        // Username validation
        if (!username.value.trim()) {
            showError(username, 'Username is required');
            isValid = false;
        } else if (username.value.trim().length < 3) {
            showError(username, 'Username must be at least 3 characters long');
            isValid = false;
        }

        // Password validation
        if (!password1.value.trim()) {
            showError(password1, 'Password is required');
            isValid = false;
        } else if (password1.value.trim().length < 8) {
            showError(password1, 'Password must be at least 8 characters long');
            isValid = false;
        }

        // Password confirmation
        if (!password2.value.trim()) {
            showError(password2, 'Please confirm your password');
            isValid = false;
        } else if (password1.value !== password2.value) {
            showError(password2, 'Passwords do not match');
            isValid = false;
        }

        return isValid;
    }

    function showError(input, message) {
        // Find the input group div
        const inputGroup = input.closest('.input-group');
        
        // Create error message element
        const errorElement = document.createElement('div');
        errorElement.className = 'validation-error text-danger small mt-1 w-100';
        errorElement.textContent = message;
        
        // Insert error message after the input group
        inputGroup.after(errorElement);
        
        // Add error styling to input
        input.classList.add('is-invalid');
    }

    function resetErrors(form) {
        // Remove all error messages
        form.querySelectorAll('.validation-error').forEach(el => el.remove());
        
        // Remove error styling from inputs
        form.querySelectorAll('input').forEach(input => {
            input.classList.remove('is-invalid');
        });
    }
});


const buyButtons = document.querySelectorAll('.buy-button');

buyButtons.forEach(button => {
    button.addEventListener('mouseover', () => {
        button.style.backgroundColor = '#0069d9';
    });

    button.addEventListener('mouseout', () => {
        button.style.backgroundColor = '#007bff';
    });
});
document.querySelectorAll('input[type="file"]').forEach(input => {
    const fileNameSpan = input.nextElementSibling;
    const button = input.previousElementSibling;

    button.addEventListener('click', () => input.click());

    input.addEventListener('change', () => {
        fileNameSpan.textContent = input.files.length > 0 ? input.files[0].name : 'Файл не вибрано';
    });
});