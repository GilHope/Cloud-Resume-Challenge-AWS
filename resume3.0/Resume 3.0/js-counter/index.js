// GH-CLOUD-RESUME VISITOR COUNTER

const counter = document.querySelector(".counter-number");
async function updateCounter()  {
    let response = await fetch("https://d5uvb4hkmt25ddtlw5o4zccrk40opdiw.lambda-url.us-east-1.on.aws/");
    let data = await response.json();
    counter.innerHTML = ` Total Visitors: ${data}`;
}

updateCounter();