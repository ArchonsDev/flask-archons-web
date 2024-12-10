const navToggle = document.getElementById('navToggle');
navToggle.addEventListener('click', (e) => {
    const flyout = document.getElementById('navFlyout');
    
    if (flyout.classList.contains('hidden')) {
        navToggle.src = './static/images/close.svg';
    } else {
        navToggle.src = './static/images/hamburger.svg';
    }

    flyout.classList.toggle('hidden');
});