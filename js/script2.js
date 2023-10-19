document.getElementById('data-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('data-form').reset();
        document.getElementById('message').style.display = 'block';
        document.getElementById('message').textContent = data.message;
        setTimeout(() => {
            document.getElementById('message').style.display = 'none';
        }, 5000);
    });
});
