const logo = document.getElementById('logo');
const bank = document.getElementById('bank');

logo.addEventListener('click', () => {
    window.location.href = '/';
});

bank.addEventListener('click', () => {
    window.location.href = '/bank';
});