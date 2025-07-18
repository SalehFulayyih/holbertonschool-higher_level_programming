document.addEventListener("DOMContentLoaded", function() {
    const header = document.querySelector('header');
    const toggle = document.getElementById('toggle_header');

    toggle.addEventListener('click', function() {
        if (header.classList.contains('red')) {
            header.classList.replace('red', 'green');
        } else if (header.classList.contains('green')) {
            header.classList.replace('green', 'red');
        }
    });
});
