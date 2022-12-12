const signup1 = document.getElementById("nav-sp");
const signin1 = document.getElementById("nav-sn");
const signup2 = document.getElementById("form-sp");
const signin2 = document.getElementById("form-sn");

const signUp = document.getElementById("signup");
const signIn = document.getElementById("signin");

const cancel1 = document.getElementById("spcancel");
const cancel2 = document.getElementById("sncancel");

const signupform = document.querySelector(".signup-cont");
const signinform = document.querySelector(".signin-cont");
const bgnav = document.querySelector(".navbar");
const bgcontent = document.querySelector(".content");
const tname = document.getElementById("title");

signup1.onclick = () => {
    signupform.style.display = 'block';
    tname.innerHTML = "Sign Up | Books";
    bgnav.style.filter = 'blur(3px)';
    bgcontent.style.filter = 'blur(3px)';
};
signup2.onclick = () => {
    signupform.style.display = 'block';
    tname.innerHTML = "Sign Up | Books";
    bgnav.style.filter = 'blur(3px)';
    bgcontent.style.filter = 'blur(3px)';
};

signin1.onclick = () => {
    signinform.style.display = 'block';
    tname.innerHTML = "Sign In | Books";
    bgnav.style.filter = 'blur(3px)';
    bgcontent.style.filter = 'blur(3px)';
};
signin2.onclick = () => {
    signinform.style.display = 'block';
    tname.innerHTML = "Sign In | Books";
    bgnav.style.filter = 'blur(3px)';
    bgcontent.style.filter = 'blur(3px)';
};

cancel1.addEventListener('click', (e) => {
    e.preventDefault()
    signupform.style.display = 'none';
    bgnav.style.filter = 'blur(0)';
    bgcontent.style.filter = 'blur(0)';
    tname.innerHTML = "Welcome | e-Books";
});
cancel2.addEventListener('click', (e) => {
    e.preventDefault()
    signinform.style.display = 'none';
    bgnav.style.filter = 'blur(0)';
    bgcontent.style.filter = 'blur(0)';
    tname.innerHTML = "Welcome | e-Books";
});
/*
signUp.addEventListener('click', () => {
    bgnav.style.filter = 'blur(3px)';
    bgcontent.style.filter = 'blur(3px)';
})*/