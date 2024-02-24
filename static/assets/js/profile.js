let edit1 = document.getElementById("phone");
let icon1 = document.querySelector(".toggle1");

let edit2 = document.getElementById("email");
let icon2 = document.querySelector(".toggle2");

let edit3 = document.getElementById("old-pass");
let icon3 = document.querySelector(".toggle3");

let edit4 = document.getElementById("new-pass");
let icon4 = document.querySelector(".toggle4");

icon1.onclick = function () {
  edit1.removeAttribute("disabled");
};

icon2.onclick = function () {
  edit2.removeAttribute("disabled");
};

icon3.onclick = function () {
  edit3.removeAttribute("disabled");
};

icon4.onclick = function () {
  edit4.removeAttribute("disabled");
};

let saveEdits = document.querySelector(".save-btn");

saveEdits.onclick = function () {
  edit1.setAttribute("disabled", "");
  edit2.setAttribute("disabled", "");
  edit3.setAttribute("disabled", "");
  edit4.setAttribute("disabled", "");
};
