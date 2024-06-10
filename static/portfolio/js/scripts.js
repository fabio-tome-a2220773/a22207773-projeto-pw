

document.addEventListener("DOMContentLoaded", () => {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const body = document.body;
    const isDarkMode = localStorage.getItem('dark-mode') === 'true';

    if (isDarkMode) {
        body.classList.add('dark-mode');
    }

    darkModeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        localStorage.setItem('dark-mode', body.classList.contains('dark-mode'));
    });

    function updateDateTime() {
        const dateTimeElement = document.getElementById('date-time');
        const now = new Date();
        const formattedDateTime = now.toLocaleString('pt-PT', {
            dateStyle: 'full',
            timeStyle: 'long'
        });
        dateTimeElement.textContent = formattedDateTime;
    }

    updateDateTime();
    setInterval(updateDateTime, 1000);
});
