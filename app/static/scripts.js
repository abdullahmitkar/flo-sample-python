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
