// GH-CLOUD-RESUME VISITOR COUNTER

// const counter = document.querySelector(".counter-number");
// async function updateCounter()  {
//     // let response = await fetch("https://d5uvb4hkmt25ddtlw5o4zccrk40opdiw.lambda-url.us-east-1.on.aws/");
//     // let response = await fetch("https://25h2mgx3kj.execute-api.us-east-1.amazonaws.com/VisitorCount");
//     let response = await fetch("https://25h2mgx3kj.execute-api.us-east-1.amazonaws.com/Prod/VisitorCount");
//     let data = await response.json();
//     // console.log(data);  // log the response data
//     console.log('Total visitors:', data.body);
//     counter.innerHTML = ` Total Visitors: ${data.body}`;
// }

// updateCounter(); 

// window.addEventListener('load', async (event) => {
//     const response = await fetch('https://25h2mgx3kj.execute-api.us-east-1.amazonaws.com/Prod/VisitorCount');
//     let data = await response.json();

//     console.log('API response data:', data); // log full response

//     let visitorCount = "Total Visitors: " + data; // use data directly as it's a number
//     let counterElement = document.querySelector('.counter-number');

//     if (counterElement) {
//         counterElement.textContent = visitorCount;
//     }
// });

window.addEventListener('load', async (event) => {
    const response = await fetch('https://25h2mgx3kj.execute-api.us-east-1.amazonaws.com/Prod/VisitorCount');
    let data = await response.json();

    console.log('API response data:', data); // log full response

    let visitorCount = "Total Visitors: " + data.body.view_count; // extract view_count from body
    let counterElement = document.querySelector('.counter-number');

    if (counterElement) {
        counterElement.textContent = visitorCount;
    }
});




