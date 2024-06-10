document.addEventListener('DOMContentLoaded', () => {
    const listItems = document.querySelectorAll('.list-group-item');
    listItems.forEach(item => {
        item.addEventListener('mouseover', () => {
            item.style.backgroundColor = '#f1f1f1';
        });
        item.addEventListener('mouseout', () => {
            item.style.backgroundColor = 'white';
        });
    });

    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            alert(`You clicked on ${link.textContent}`);
        });
    });
});
