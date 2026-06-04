const API_URL =
"https://multi-agent-research-assistant-4-6buc3idhb.vercel.app";

async function generateReport(){

    const topic =
        document.getElementById("topic").value;

    document.getElementById("loading")
        .innerText = "Generating report...";

    const response =
        await fetch(API_URL,{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                topic:topic
            })
        });

    const data =
        await response.json();

    document.getElementById("loading")
        .innerText = "";

    document.getElementById("output")
        .innerText = data.report;
}