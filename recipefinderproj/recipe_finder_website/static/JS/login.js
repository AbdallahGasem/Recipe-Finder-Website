let field1 = document.getElementById('field1');
let field2 = document.getElementById('field2');

// Load values from localStorage if available (used for demonstration purposes)
if (localStorage.length > 0) {
    field1.value = localStorage.getItem('field1');
    field2.value = localStorage.getItem('field2');
}

field1.onkeyup = function() {
    localStorage.setItem('field1', field1.value);
    localStorage.setItem('field2', field2.value);
}

document.getElementById("submitButton").addEventListener("click", function(event) {
    if (field1.checkValidity() && field2.checkValidity()) {
        // Retrieve email, password, and option arrays from localStorage
        let emailArray = JSON.parse(localStorage.getItem('emailArray')) || [];
        let passArray = JSON.parse(localStorage.getItem('passArray')) || [];
        let checkArray = JSON.parse(localStorage.getItem('checkArray')) || [];
        let credentialsValid = "not registered";
        
        for (let i = 0; i < emailArray.length; i++) {
            if (field1.value === emailArray[i] && field2.value === passArray[i]) {
                if (checkArray[i] === "user") {
                    credentialsValid = "user";
                } else if (checkArray[i] === "admin") {
                    credentialsValid = "admin";
                }
                break;
            }
        }
        
        if (credentialsValid === "user") {
            event.preventDefault(); // Prevent default form submission
            window.location.href = "recipesuser.html";
            return false;
        } else if (credentialsValid === "admin") {
            event.preventDefault();
            window.location.href = 'recipesadminfokak.html';
            return false;
        } else {
            event.preventDefault();
            alert("Incorrect credentials");
            return false;
        }
    }
});
