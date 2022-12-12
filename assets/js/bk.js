const logout = document.querySelector(".logout");
const login = document.querySelector(".login");
const msg = document.querySelector(".lg-msg");

const add = document.querySelector(".add");
const edit = document.querySelector(".row-id");
const cancelbtn = document.getElementById("bk-id");
const form = document.querySelector(".bk-form-cont");

logout.addEventListener('click', (e) => {
    e.preventDefault();
    login.style.display = 'block';
    msg.style.display = 'block';
});

add.addEventListener('click', (e) => {
    e.preventDefault();
    form.style.display = 'block';
});

edit.addEventListener('click', (e) => {
    e.preventDefault();
    form.style.display = 'block';
});

cancelbtn.addEventListener('click', (e) => {
    e.preventDefault();
    form.style.display = 'none';
});