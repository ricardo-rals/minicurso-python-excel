// Carrega o conteúdo de um tópico dinamicamente
async function carregarTopico(topico) {
    const container = document.getElementById('conteudo-topico');

    try {
        const response = await fetch(`topicos/${topico}.html`);

        if (!response.ok) {
            throw new Error(`Erro ao carregar ${topico}: ${response.status}`);
        }

        const html = await response.text();
        container.innerHTML = html;

        // Abre o tópico após carregar
        abrirTopico(topico);

    } catch (error) {
        console.error('Erro ao carregar tópico:', error);
        container.innerHTML = `
            <div class="slide active" style="display: block;">
                <h2>Erro ao Carregar Tópico</h2>
                <p style="color: red;">Não foi possível carregar o conteúdo do tópico.</p>
                <p>Erro: ${error.message}</p>
                <button class="btn" onclick="voltarMenu()">Voltar ao Menu</button>
            </div>
        `;
    }
}

// Adiciona eventos aos cards de tópicos
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.topico-card');

    cards.forEach(card => {
        card.addEventListener('click', () => {
            const topico = card.getAttribute('data-topico');
            carregarTopico(topico);
        });
    });
});
