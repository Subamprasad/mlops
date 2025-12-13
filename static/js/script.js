document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const btn = document.querySelector('.btn-primary');
    
    if(form) {
        form.addEventListener('submit', function() {
            // Change button text and disable it
            btn.value = 'Predicting...';
            btn.disabled = true;
            btn.style.opacity = '0.7';
            btn.style.cursor = 'wait';
        });
    }
    
    // Smooth scroll to result if it exists
    const resultBox = document.querySelector('.result-box');
    if(resultBox) {
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
});
