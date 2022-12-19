const logout = document.querySelector(".logout");
const login = document.querySelector(".login");
const msg = document.querySelector(".lg-msg");

const add = document.querySelector(".add");
const edit = document.querySelector(".row-id");
//const cancelbtn = document.getElementById("bk-id");
const form = document.querySelector(".bk-form-cont");
const formEdit = document.querySelector(".bk-form-cont-edit");

logout.addEventListener('click', (e) => {
    e.preventDefault();
    login.style.display = 'block';
    msg.style.display = 'block';
});

add.addEventListener('click', (e) => {
    e.preventDefault();
    form.style.display = 'block';
});

edit.addEventListener('click', (event) => {
    event.preventDefault();
    formEdit.style.display = 'block';
});