let topicoAtual = null;
let slideAtual = 0;
let totalSlides = 0;
let isExercicio = false;
let isQuiz = false;

function abrirTopico(topico) {
    // Esconde o menu
    const menuPrincipal = document.getElementById('menu-principal');
    if (menuPrincipal) {
        menuPrincipal.style.display = 'none';
    }

    // Esconde todos os tópicos
    const todosTopicos = document.querySelectorAll('.slides-container');
    todosTopicos.forEach(t => t.style.display = 'none');

    // Mostra o tópico selecionado
    topicoAtual = topico;
    const elementoTopico = document.getElementById(topico);
    if (elementoTopico) {
        elementoTopico.style.display = 'block';
    }

    // Reset para o primeiro slide
    slideAtual = 0;
    mostrarSlide(slideAtual);

    // Rola para o topo
    window.scrollTo(0, 0);
}

function voltarMenu() {
    // Se estiver em uma página de exercício ou quiz, redireciona
    if (isExercicio || isQuiz) {
        window.location.href = '../../index.html';
        return;
    }

    // Esconde todos os tópicos
    const todosTopicos = document.querySelectorAll('.slides-container');
    todosTopicos.forEach(t => t.style.display = 'none');

    // Mostra o menu
    const menuPrincipal = document.getElementById('menu-principal');
    if (menuPrincipal) {
        menuPrincipal.style.display = 'block';
    }

    // Rola para o topo
    window.scrollTo(0, 0);
}

function mostrarSlide(n) {
    if (!topicoAtual) return;
    
    const slides = document.querySelectorAll(`#${topicoAtual} .slide`);
    totalSlides = slides.length;

    if (totalSlides === 0) return;

    // Garante que n está dentro dos limites
    if (n >= totalSlides) slideAtual = totalSlides - 1;
    if (n < 0) slideAtual = 0;

    // Esconde todos os slides
    slides.forEach(slide => slide.classList.remove('active'));

    // Mostra o slide atual
    if (slides[slideAtual]) {
        slides[slideAtual].classList.add('active');
    }

    // Atualiza contador se existir
    const contadorId = topicoAtual.replace('topico', 'contador').replace('exercicios-', 'contador');
    const contador = document.getElementById(contadorId);
    if (contador) {
        contador.textContent = `${slideAtual + 1} / ${totalSlides}`;
    }

    // Rola para o topo
    window.scrollTo(0, 0);
}

function proximoSlide() {
    if (totalSlides > 0) {
        slideAtual++;
        if (slideAtual >= totalSlides) slideAtual = totalSlides - 1;
        mostrarSlide(slideAtual);
    }
}

function slideAnterior() {
    if (totalSlides > 0) {
        slideAtual--;
        if (slideAtual < 0) slideAtual = 0;
        mostrarSlide(slideAtual);
    }
}

// Inicialização para exercícios e quizzes
document.addEventListener('DOMContentLoaded', () => {
    // Verifica se é uma página de exercício
    const exercicioContainer = document.querySelector('[id^="exercicios-topico"]');
    if (exercicioContainer) {
        isExercicio = true;
        topicoAtual = exercicioContainer.id;
        // Mostra o container de slides
        exercicioContainer.style.display = 'block';
        const slides = document.querySelectorAll(`#${topicoAtual} .slide`);
        totalSlides = slides.length;
        if (totalSlides > 0) {
            slideAtual = 0;
            mostrarSlide(0);
        }
    }

    // Verifica se é uma página de quiz
    const quizContainer = document.querySelector('.quiz-container');
    if (quizContainer) {
        isQuiz = true;
    }
});

// Atalhos de teclado
document.addEventListener('keydown', (e) => {
    // ESC sempre volta ao menu
    if (e.key === 'Escape') {
        e.preventDefault();
        voltarMenu();
        return;
    }

    // Para tópicos e exercícios (não quizzes)
    if (topicoAtual && !isQuiz) {
        if (e.key === 'ArrowRight' || e.key === ' ') {
            e.preventDefault();
            proximoSlide();
        } else if (e.key === 'ArrowLeft') {
            e.preventDefault();
            slideAnterior();
        }
    }
});
