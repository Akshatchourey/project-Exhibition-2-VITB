pizza = document.querySelector('.pizza')
navbar = document.querySelector('.nav-bar')
navlinks = document.querySelector('.nav-links')

pizza.addEventListener('click',()=>{
    navbar.classList.toggle('h-nav-resp')
    navlinks.classList.toggle('nav-links-res')
    pizza.classList.toggle('pizza')
})
