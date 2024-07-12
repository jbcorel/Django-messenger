function openModal(modalId) {
    document.getElementById(modalId).classList.remove('hidden');
}

function closeModal(modalId) {
    document.getElementById(modalId).classList.add('hidden');
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('room-creation-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting the default way

        const formData = new FormData(form);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch(form.action, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Accept': 'application/json'
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // If the form submission was successful, redirect to the success URL
                window.location.href = window.location + data.redirect_url;
            } else {
                // If there are errors, update the form with the errors
                form.innerHTML = data.form_html;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
