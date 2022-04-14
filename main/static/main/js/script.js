

const hamburger = document.getElementById('hamburger');
const navUL = document.getElementById('nav-ul');

hamburger.addEventListener('click', () => {
    navUL.classList.toggle('show');
});
var slideIndex = 1;
showSlides(slideIndex);
