function toggleMenu() {
    const navbar = document.getElementById('navbar');
    navbar.classList.toggle('active');
}

const btntop = document.getElementById("btntop");

window.onscroll = function() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        btntop.style.display = "block"; 
    } else {
        btntop.style.display = "none"; 
}
};

btntop.onclick = function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

const image = document.querySelector('.fotinha3');
const image2 = document.querySelector(".fotinha4");

function aplicarDesfoque() {
    image.style.filter = "blur(5px)";  
    image.style.scale = "1.050"
}

function removerDesfoque() {
    image.style.filter = "none";  
    image.style.scale = "1"
}

function aplicarDesfoque2() {
    image2.style.filter = "blur(5px)";  
    image2.style.scale = "1.050"
    image2.style.transition = "0.5s"
}

function removerDesfoque2() {
    image2.style.filter = "none";  
    image2.style.scale = "1"
    image2.style.transition = "0.5s"
}



