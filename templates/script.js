const dateInput = document.getElementById("date");
const suggestionsBox = document.querySelector(".suggestions");
const suggestionsList = document.getElementById("date-suggestions");

const availableDates = [
    "2024-12-25", "2024-12-31", "2024-12-15", 
    "2025-01-01", "2025-02-14", "2025-03-17"
];

// Function to format the date to YYYY-MM-DD
function formatDate(date) {
    const dateObj = new Date(date);
    const year = dateObj.getFullYear();
    const month = String(dateObj.getMonth() + 1).padStart(2, '0'); // Month is 0-indexed
    const day = String(dateObj.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// Function to show suggestions based on user input
function showSuggestions(input) {
    // Clear previous suggestions
    suggestionsList.innerHTML = "";
    
    // Filter available dates based on the input
    const filteredDates = availableDates.filter(date => date.includes(input));

    // If there are any matches, show the suggestions
    if (filteredDates.length > 0) {
        suggestionsBox.style.display = "block";
        filteredDates.forEach(date => {
            const listItem = document.createElement("li");
            listItem.textContent = date;
            listItem.addEventListener("click", () => {
                dateInput.value = formatDate(date); // Format and set the selected date
                suggestionsBox.style.display = "none"; // Hide the suggestions
            });
            suggestionsList.appendChild(listItem);
        });
    } else {
        suggestionsBox.style.display = "none"; // Hide if no matches
    }
}

// Event listener to show suggestions as user types
dateInput.addEventListener("input", (event) => {
    const input = event.target.value;
    showSuggestions(input);
});

// Hide suggestions if the user clicks outside
document.addEventListener("click", (event) => {
    if (!event.target.closest(".container")) {
        suggestionsBox.style.display = "none";
    }
});
