document.addEventListener("DOMContentLoaded", function () {
// Get references to the elements
    var dynamicContent = document.getElementById("start");
    var signIn = document.getElementById("signIn");
    var register = document.getElementById("register");
    var form = document.getElementById("signInSheet");
    var registerSheet = document.getElementById("registerSheet");
    var submitDataButton = document.getElementById("submitData")

    submitDataButton.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Collect form data
        const formData = new FormData(form);
        // Send a POST request to the Flask backend
        fetch('/signIn.html', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the backend (if needed)
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});