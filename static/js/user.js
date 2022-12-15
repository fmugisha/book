window.addEventListener('load', (event) => {
    event.preventDefault()

    const logout = document.querySelector(".logout");
    const login = document.querySelector(".login");
    const msg = document.querySelector(".lg-msg");
    const saveBtn = document.getElementById("save");
    const roleValue = document.querySelectorAll(".role")
    const form = document.getElementById("change")

    logout.addEventListener('click', (e) => {
        e.preventDefault();
        login.style.display = 'block';
        msg.style.display = 'block';
    })
})