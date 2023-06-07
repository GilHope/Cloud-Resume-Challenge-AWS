// GH-CLOUD-RESUME VISITOR COUNTER


// Import API URL from config.js file.
import apiUrl from '../config.js';

// Add a 'load' event listener to the window that will run the async function once the page is fully loaded.
// Use the Fetch API to get a response from the API URL.
// Parse the JSON from the response.
window.addEventListener('load', async (event) => {
    const response = await fetch(apiUrl);
    let data = await response.json();

    // Log the parsed JSON data to the console.
    console.log('API response data:', data); // log full response

    // Extract 'view_count' from the parsed JSON and prepend it with 'Total Visitors: '
    // Find the element with class 'counter-number'
    let visitorCount = "Total Visitors: " + data.view_count; // extract view_count directly from data
    let counterElement = document.querySelector('.counter-number');

    // If the element was found...
    // ...update its text content with the 'visitorCount' string.
    if (counterElement) {
        counterElement.textContent = visitorCount;
    }
});

// Relevant Docs:
// https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
// https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener
// https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector



  



