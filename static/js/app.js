const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu')
menu.addEventListener('click', function() {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
})

document.getElementById('togglePassword').addEventListener('click', function() {
  var passwordInput = document.getElementById('password');
  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    this.classList.remove('fa-eye');
    this.classList.add('fa-eye-slash');
  } else {
    passwordInput.type = 'password';
    this.classList.remove('fa-eye-slash');
    this.classList.add('fa-eye');
  }
});
