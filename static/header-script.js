const logo = document.getElementById('logo');
const login = document.getElementById('login');
const bank = document.getElementById('bank');

logo.addEventListener('click', () => {
    window.location.href = '/';
});

login.addEventListener('click', () => {
    window.location.href = '/login';
});

bank.addEventListener('click', () => {
    window.location.href = '/bank';
});