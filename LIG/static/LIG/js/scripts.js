document.addEventListener('DOMContentLoaded', () => {
    // Verificar se está na página principal
    const isHomePage = window.location.pathname === '/';



    // Smooth Scroll for Links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            document.querySelector(link.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Hover Effect for Discipline List Items
    const disciplineItems = document.querySelectorAll('.disciplines-list li');
    disciplineItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            item.style.backgroundColor = '#c8e6c9';
        });
        item.addEventListener('mouseleave', () => {
            item.style.backgroundColor = '#e0f7fa';
        });
    });
});
