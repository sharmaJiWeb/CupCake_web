document.addEventListener('DOMContentLoaded', () => {
    console.log('Sweet Cupcake Theme Loaded');

    // Simple Intersection Observer for scroll animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    animatedElements.forEach(el => observer.observe(el));

    // Mobile Menu Toggle - Moved to base.js

    // Parallax Effect for Blobs
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        // Parallax for highlight background blobs
        document.querySelectorAll('.blob-bg').forEach((blob, index) => {
            const speed = (index + 1) * 0.05; // Gentle speed variation
            // Use translation but be careful not to override existing transforms if any
            // Blobs in css are just positioned, so translate is safe
            blob.style.transform = `translateY(${scrolled * speed}px)`;
            // Note: If blob-bg had other transforms, we'd need to combine them. 
            // Currently they only have border-radius and size.
        });
    });

    // Loader Logic
    window.addEventListener('load', () => {
        const loader = document.getElementById('loader-wrapper');
        if (loader) {
            // Min time to show cute animation or just hide
            setTimeout(() => {
                loader.classList.add('hidden');
            }, 800); // 800ms delay to enjoy the animation
        }
    });
});
