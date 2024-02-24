
// start password registration
let password = document.getElementById("password");
let passwordValue = document.getElementById("password").value;
let confirmPassword = document.getElementById("Confirm-password");
let confirmPasswordValue = document.getElementById("Confirm-password").value;
let passwordInnerText = password.value;
let confirmPasswordInnerText = confirmPassword.value;

let passMessege = document.getElementById("pass-messege");
let confPassMessege = document.getElementById("conf-pass-messege");

password.onkeyup = function () {
  if (passwordValue < 7) {
    passwordValue = document.getElementById("password").value.length;
    password.style.borderColor = "red";
    passMessege.style.display = "block";
    // console.log(password.value);
  } else {
    passwordValue = document.getElementById("password").value.length;
    password.style.borderColor = "#00ca99";
    passMessege.style.display = "none";
  }
};

confirmPassword.onkeyup = function () {
  if (confirmPassword.value != password.value) {
    confirmPasswordValue =
      document.getElementById("Confirm-password").value.length;
    confirmPassword.style.borderColor = "red";
    confPassMessege.style.display = "block";
    // console.log(confirmPassword.value);
  } else {
    confirmPassword.style.borderColor = "#00ca99";
    confPassMessege.style.display = "none";
  }
};
// end password registration
