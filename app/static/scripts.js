const scrollContainer = document.getElementById('scroll-container');

// Simulated data for each section
const teacherContent = "Your teacher information goes here.";
const entertainerContent = "Your entertainer information goes here.";
const tutorContent = "Your tutor information goes here.";
const moneyGuyContent = "Your money guy information goes here.";

// Function to check if the user has scrolled to the bottom
function isScrolledToBottom() {
    return scrollContainer.scrollHeight - scrollContainer.scrollTop === scrollContainer.clientHeight;
}

// Function to append content to the scroll container
function appendContent(content) {
    const item = document.createElement('div');
    item.classList.add('item');
    item.innerHTML = content;
    scrollContainer.appendChild(item);
}

// Initial content
appendContent(teacherContent);
appendContent(entertainerContent);
appendContent(tutorContent);
appendContent(moneyGuyContent);

// Event listener for infinite scrolling
scrollContainer.addEventListener('scroll', () => {
    if (isScrolledToBottom()) {
        // Append more content when scrolled to the bottom
        appendContent('More content goes here.');
    }
});
