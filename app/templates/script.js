const bar = document.getElementByid('bar');
const nav = document.getElementByid('navbar');

if (bar) {
    bar.addEventListener('click', () => {
        nav.classList.add('active');
    })
}