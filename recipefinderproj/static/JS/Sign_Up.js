// let fname = document.getElementById('uname');
// let mail = document.getElementById('mail');
// let pass = document.getElementById('pass');
// let confpass = document.getElementById('confpass');

// function saveToLocalStorage(selectedOption) {
//     localStorage.setItem('uname', fname.value);
//     localStorage.setItem('mail', mail.value);
//     localStorage.setItem('pass', pass.value);
//     localStorage.setItem('option', selectedOption);

//     // Save email and password arrays to localStorage
//     let emailArray = JSON.parse(localStorage.getItem('emailArray')) || [];
//     let passArray = JSON.parse(localStorage.getItem('passArray')) || [];
//     let checkArray = JSON.parse(localStorage.getItem('checkArray')) || [];
//     emailArray.push(mail.value);
//     passArray.push(pass.value);
//     checkArray.push(selectedOption);
//     localStorage.setItem('emailArray', JSON.stringify(emailArray));
//     localStorage.setItem('passArray', JSON.stringify(passArray));
//     localStorage.setItem('checkArray', JSON.stringify(checkArray));
// }

// function validateForm() {
//     if (pass.value !== confpass.value) {
//         alert("Passwords do not match!");
//         return false; 
//     }
//     return true; 
// }

// function emailExists(email) {
//     let emailArray = JSON.parse(localStorage.getItem('emailArray')) || [];
//     return emailArray.includes(email);
// }

// document.getElementById("submitButton").addEventListener("click", function(event) {
//     const selectedOption = document.querySelector('input[name="option"]:checked').value;
//     console.log(selectedOption);
//     if (fname.checkValidity() && lname.checkValidity() && mail.checkValidity() && pass.checkValidity() && confpass.checkValidity()) {
//         if (validateForm() && !emailExists(mail.value)) {
//             saveToLocalStorage(selectedOption); 
//             if (selectedOption === 'user') {
//                 event.preventDefault(); 
//                 window.location.href = 'recipesuser.html';
//                 return false;
//             } else if (selectedOption === 'admin') {
//                 event.preventDefault(); 
//                 window.location.href = 'recipesadminfokak.html';
//                 return false;
//             }
//         } else if (emailExists(mail.value)) {
//             event.preventDefault(); 
//             alert("Email already exists");
//             return false;
//         }
//     } else {
//         return false;    
//     }
// });


// let fname = document.getElementById('uname');
// let mail = document.getElementById('mail');
// let pass = document.getElementById('pass');
// let confpass = document.getElementById('confpass');

// function validateForm() {
//     if (pass.value !== confpass.value) {
//         alert("Passwords do not match!");
//         return false; 
//     }
//     return true; 
// }

// document.getElementById("submitButton").addEventListener("click", function(event) {
//     event.preventDefault(); // Prevent the default form submission
//     const selectedOption = document.querySelector('input[name="option"]:checked').value;

//     if (validateForm()) {
//         // Prepare the data to be sent
//         const formData = new FormData();
//         formData.append('uname', fname.value);
//         formData.append('password', pass.value);
//         formData.append('mail', mail.value);
//         formData.append('option', selectedOption);

//         // Send the data using fetch API
//         fetch('addrecord/', { // The URL to your Django addrecord view
//             method: 'POST',
//             body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 // Redirect based on user type
//                 window.location.href = selectedOption === 'user' ? 'recipesuser.html' : 'recipesadminfokak.html';
//             } else {
//                 // Handle errors, such as email already exists or passwords do not match
//                 alert(data.error);
//             }
//         })
//         .catch(error => console.error('Error:', error));
//     }
// });


// Function to get the CSRF token from a cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Get the CSRF token
const csrftoken = getCookie('csrftoken');

let fname = document.getElementById('uname');
let mail = document.getElementById('mail');
let pass = document.getElementById('pass');
let confpass = document.getElementById('confpass');

function validateForm() {
    if (pass.value !== confpass.value) {
        alert("Passwords do not match!");
        return false; 
    }
    return true; 
}




document.getElementById("submitButton").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the form element
    var form = document.querySelector('form');

    // Check if the form is valid
    if (!form.checkValidity()) {
        // If the form is not valid, trigger the browser's default validation UI
        form.reportValidity();
        return false;
    }

    const selectedOption = document.querySelector('input[name="option"]:checked').value;

    if (validateForm()) {
        // Prepare the data to be sent
        const formData = new FormData(form); // Use the form element to initialize FormData

        // Send the data using fetch API with the CSRF token included in the headers
        fetch('addrecord/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrftoken
            },
            credentials: 'same-origin' // Required for cookies to be sent with the request
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Redirect based on user type
                // window.location.href = selectedOption === 'user' ? 'recipesuser.html' : 'recipesadminfokak.html';
                if (selectedOption == 'user') {
                    event.preventDefault(); 
                    window.location.href = 'recipesuser.html';
                    return false;
                } else if (selectedOption == 'admin') {
                    event.preventDefault(); 
                    window.location.href = 'recipesadminfokak.html';
                    return false;
                }


            } else {
                // Handle errors, such as email already exists or passwords do not match
                alert(data.error);
            }
        })
        .catch(error => console.error('Error:', error));
    }
});
