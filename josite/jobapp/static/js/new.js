// page contains the javascript frontend validations
var fullnameInput = document.getElementById("id_fullname");
var fullnameError = document.getElementById("fullname-error");
    
fullnameInput.addEventListener('blur', function(event) {
    var fullname = fullnameInput.value.trim();
    
    if (fullname === "") {
        fullnameError.innerHTML = "Name field cannot be empty";
        window.scrollTo(0, 0);
    } else if (fullname.length < 4 || fullname.length > 100) {
        fullnameError.innerHTML = "Number of letters must be between 4 and 100";
        window.scrollTo(0, 0);
    } else {
        fullnameError.innerHTML = "";  // Clear error message
    }
    });
    
 // Email validation
var emailInput = document.getElementById("id_email");
var emailError = document.getElementById("email-error");

emailInput.addEventListener('blur', function(event) {
    var email = emailInput.value.trim();
    var emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (email === "") {
        emailError.innerHTML = "Email address cannot be empty";
        window.scrollTo(0, 0);
    } else if (!email.match(emailRegex)) {
        emailError.innerHTML = "Invalid email address";
        window.scrollTo(0, 0);
    } else {
        emailError.innerHTML = "";  // Clear error message
    }
});

// Phone number validation
var phoneInput = document.getElementById("id_phonenumber");
var phoneError = document.getElementById("phone-error");
var phoneRegex = /^\d{10}$/;

phoneInput.addEventListener('blur', function(event) {
    var phone = phoneInput.value.trim();

    if (phone === "") {
        phoneError.innerHTML = "Phone number cannot be empty";
        window.scrollTo(0, 0);
    } else if (!phone.match(phoneRegex)) {
        phoneError.innerHTML = "Invalid phone number";
        window.scrollTo(0, 0);
    } else {
        phoneError.innerHTML = "";  // Clear error message
    }
});

// Date of Birth validation
var dobInput = document.getElementById("id_dob");
var dobError = document.getElementById("dob-error");

dobInput.addEventListener('blur', function(event) {
    var dob = dobInput.value.trim();
    // Function to calculate age based on the given date of birth
    function calculateAge(birthDate) {
        var today = new Date();
        var birthDate = new Date(birthDate);
        var age = today.getFullYear() - birthDate.getFullYear();
        var month = today.getMonth() - birthDate.getMonth();
        if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        return age;
    }

    if (dob === "") {
        dobError.innerHTML = "Date of Birth cannot be empty";
        window.scrollTo(0, 0);
    } else {
        var age = calculateAge(dob);
        if (age < 18) {
            dobError.innerHTML = "You must be at least 18 years old to apply";
            window.scrollTo(0, 0);
        } else {
            dobError.innerHTML = "";  // Clear error message
        }
    }
});

// Experience type validation
var experienceInput = document.getElementById("id_experience_type");
var experienceError = document.getElementById("experience-error");

experienceInput.addEventListener('blur', function(event) {
    var experience = experienceInput.value.trim();

    if (experience === "") {
        experienceError.innerHTML = "Please select an option";
       
    } else {
        experienceError.innerHTML = "";  // Clear error message
    }
});

// Job type validation
var jobTypeInput = document.getElementById("id_job_type");
var jobTypeError = document.getElementById("job-type-error");

jobTypeInput.addEventListener('blur', function(event) {
    var jobType = jobTypeInput.value.trim();

    if (jobType === "") {
        jobTypeError.innerHTML = "Please select an option";
        
    } else {
        jobTypeError.innerHTML = "";  // Clear error message
    }
});
