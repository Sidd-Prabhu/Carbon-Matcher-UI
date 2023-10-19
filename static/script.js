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


//document.getElementById('contact-form').addEventListener('submit', function (e) {
//    e.preventDefault();
//    const name = document.getElementById('name').value;
//    const email = document.getElementById('email').value;
//    const message = document.getElementById('message').value;
//    // You can add code here to handle form submission, e.g., send data to the server
//    //alert(`Form submitted:\nName: ${name}\nEmail: ${email}\nMessage: ${message}`);
//});