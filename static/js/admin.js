document.addEventListener('DOMContentLoaded', function () {
    console.log('Admin dashboard loaded 🧁');

    // Example feature: Filter rows (placeholder for future logic)
    const searchInput = document.getElementById('search-messages');
    if (searchInput) {
        searchInput.addEventListener('keyup', function (e) {
            const term = e.target.value.toLowerCase();
            const rows = document.querySelectorAll('.data-table tbody tr');

            rows.forEach(row => {
                const text = row.innerText.toLowerCase();
                row.style.display = text.includes(term) ? '' : 'none';
            });
        });
    }
});
