let topicoAtual = null;
let slideAtual = 0;
let totalSlides = 0;

function abrirTopico(topico) {
    // Esconde o menu
    document.getElementById('menu-principal').style.display = 'none';

    // Esconde todos os tópicos
    const todosTopicos = document.querySelectorAll('.slides-container');
    todosTopicos.forEach(t => t.style.display = 'none');

    // Mostra o tópico selecionado
    topicoAtual = topico;
    document.getElementById(topico).style.display = 'block';

    // Reset para o primeiro slide
    slideAtual = 0;
    mostrarSlide(slideAtual);

    // Rola para o topo
    window.scrollTo(0, 0);
}

function voltarMenu() {
    // Esconde todos os tópicos
    const todosTopicos = document.querySelectorAll('.slides-container');
    todosTopicos.forEach(t => t.style.display = 'none');

    // Mostra o menu
    document.getElementById('menu-principal').style.display = 'block';

    // Rola para o topo
    window.scrollTo(0, 0);
}

function mostrarSlide(n) {
    const slides = document.querySelectorAll(`#${topicoAtual} .slide`);
    totalSlides = slides.length;

    // Garante que n está dentro dos limites
    if (n >= totalSlides) slideAtual = totalSlides - 1;
    if (n < 0) slideAtual = 0;

    // Esconde todos os slides
    slides.forEach(slide => slide.classList.remove('active'));

    // Mostra o slide atual
    slides[slideAtual].classList.add('active');

    // Atualiza contador
    const contadorId = topicoAtual.replace('topico', 'contador');
    document.getElementById(contadorId).textContent = `${slideAtual + 1} / ${totalSlides}`;

    // Rola para o topo
    window.scrollTo(0, 0);
}

function proximoSlide() {
    slideAtual++;
    if (slideAtual >= totalSlides) slideAtual = totalSlides - 1;
    mostrarSlide(slideAtual);
}

function slideAnterior() {
    slideAtual--;
    if (slideAtual < 0) slideAtual = 0;
    mostrarSlide(slideAtual);
}

// Atalhos de teclado
document.addEventListener('keydown', (e) => {
    if (topicoAtual) {
        if (e.key === 'ArrowRight' || e.key === ' ') {
            e.preventDefault();
            proximoSlide();
        } else if (e.key === 'ArrowLeft') {
            e.preventDefault();
            slideAnterior();
        } else if (e.key === 'Escape') {
            voltarMenu();
        }
    }
});
