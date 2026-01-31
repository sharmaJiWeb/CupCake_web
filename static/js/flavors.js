document.addEventListener('DOMContentLoaded', () => {

    // --- Entrance Animation ---
    const cards = document.querySelectorAll('.flavor-card');

    // Staggered animation on load
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('visible');
        }, index * 100); // 100ms delay between each card
    });

    // --- Filtering Logic ---
    const filterBtns = document.querySelectorAll('.filter-btn');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            cards.forEach(card => {
                // Reset visibility for animation re-trigger (optional, but nice)
                card.classList.remove('visible');
                card.style.display = 'none'; // Hide layout space

                const cardCategory = card.getAttribute('data-category');

                if (filterValue === 'all' || cardCategory === filterValue) {
                    card.style.display = 'flex'; // Show layout space
                    // Small timeout to allow display:flex to apply before adding visible class for transition
                    setTimeout(() => {
                        card.classList.add('visible');
                    }, 50);
                }
            });
        });
    });

    // --- Add to Cart Interaction ---
    const addToCartBtns = document.querySelectorAll('.add-to-cart-btn');

    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const card = e.target.closest('.flavor-card');

            // Extract Data
            const title = card.querySelector('.flavor-title').textContent.trim();
            const priceText = card.querySelector('.flavor-price').textContent.replace('$', '').trim();
            const price = parseFloat(priceText);
            const image = card.querySelector('.flavor-image img').src;
            const id = title.toLowerCase().replace(/['\s]+/g, '-'); // Simple slug generation

            // Call Global Cart Function
            if (window.addToCart) {
                window.addToCart(id, title, price, image);

                // Visual Feedback
                const originalText = btn.textContent;
                btn.textContent = "Added! ✓";
                btn.style.backgroundColor = "var(--accent-dark-pink)";
                btn.style.color = "white";

                setTimeout(() => {
                    btn.textContent = originalText;
                    btn.style.backgroundColor = "";
                    btn.style.color = "";
                }, 2000);
            } else {
                console.error("Cart system not loaded!");
            }
        });
    });
});
