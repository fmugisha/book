const logout = document.querySelector(".logout");
const login = document.querySelector(".login");
const msg = document.querySelector(".lg-msg");
const saveBtn = document.getElementById("save");
const roleValue = document.getElementById("role")

logout.addEventListener('click', (e) => {
    e.preventDefault();
    login.style.display = 'block';
    msg.style.display = 'block';
})

if ((roleValue.isChecked == True && roleValue.checked == False)||(roleValue.isChecked == False && roleValue.checked == True)) {
    saveBtn.style.display = 'block'
} else {
    saveBtn.style.display = 'none'
}