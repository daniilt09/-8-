document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search');
    const cards = document.querySelectorAll('.wcard');
    searchInput.addEventListener('input', () => {
        const filter = search.value.toLowerCase();
        cards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            if (title.includes(filter)) {
                card.style.display = 'flex'; 
            } else {
                card.style.display = 'none';
            }
        });
    });
});