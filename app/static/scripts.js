const scrollContainer = document.getElementById('scroll-container');
let currentPage = 1;

// Function to append content to the scroll container
function appendContent(content) {
    const item = document.createElement('div');
    item.classList.add('item');
    item.innerHTML = content;
    scrollContainer.appendChild(item);
}

// Function to load the next card
function loadNextCard() {
    appendContent(`
        <h2>Page ${currentPage + 1}</h2>
        <!-- Content for Page ${currentPage + 1} -->
    `);
    currentPage++;
}

// Initial content
loadNextCard();

// Event listener for loading next card on scroll
scrollContainer.addEventListener('scroll', () => {
    if (scrollContainer.scrollHeight - scrollContainer.scrollTop === scrollContainer.clientHeight) {
        // Load the next card when scrolled to the bottom
        loadNextCard();
    }
});


// static/scripts.js

const scrollContainer = document.getElementById('scroll-container');
const sectionContent = document.getElementById('section-content');

let currentPage = 1;

function appendContent(content) {
    const item = document.createElement('div');
    item.classList.add('item');
    item.innerHTML = content;
    scrollContainer.appendChild(item);
}

function loadNextCard() {
    appendContent(`
        <h2>Page ${currentPage + 1}</h2>
        <!-- Content for Page ${currentPage + 1} -->
    `);
    currentPage++;
}

loadNextCard();

scrollContainer.addEventListener('scroll', () => {
    if (scrollContainer.scrollHeight - scrollContainer.scrollTop === scrollContainer.clientHeight) {
        loadNextCard();
    }
});

// Swipe navigation for section content
let touchStartX = 0;
let touchEndX = 0;

sectionContent.addEventListener('touchstart', (event) => {
    touchStartX = event.touches[0].clientX;
});

sectionContent.addEventListener('touchend', (event) => {
    touchEndX = event.changedTouches[0].clientX;

    if (touchEndX < touchStartX) {
        // Swipe left
        window.history.back();
    }
});

