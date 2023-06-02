// GH-CLOUD-RESUME VISITOR COUNTER

const counter = document.querySelector(".counter-number");
async function updateCounter()  {
    // let response = await fetch("https://d5uvb4hkmt25ddtlw5o4zccrk40opdiw.lambda-url.us-east-1.on.aws/");
    // let response = await fetch("https://25h2mgx3kj.execute-api.us-east-1.amazonaws.com/VisitorCount");
    let response = await fetch("https://25h2mgx3kj.execute-api.us-east-1.amazonaws.com/Prod/VisitorCount");
    let data = await response.json();
    console.log(data);  // log the response data
    console.log('Total visitors:', data.body);
    counter.innerHTML = ` Total Visitors: ${data.body}`;
}

updateCounter();