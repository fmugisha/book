const logout = document.querySelector(".logout");
const login = document.querySelector(".login");
const msg = document.querySelector(".lg-msg");

logout.addEventListener('click', (e) => {
    e.preventDefault();
    login.style.display = 'block';
    msg.style.display = 'block';
});