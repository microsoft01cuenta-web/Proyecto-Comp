// JavaScript functionality for the web dashboard

// Function to get current date and time in UTC
function getCurrentDateTime() {
    const now = new Date();
    return now.toISOString().replace('T', ' ').substring(0, 19);
}

// Function to display date and time
function displayDateTime() {
    const dateTimeElement = document.getElementById('date-time-display');
    dateTimeElement.textContent = getCurrentDateTime();
}

// Call the function to display date and time on page load
window.onload = displayDateTime;