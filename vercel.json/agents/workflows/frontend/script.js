async function research() {

    const topic =
        document.getElementById("topic").value;

    const response =
        await fetch("/api/index", {
            method: "POST",
            headers: {
                "Content-Type":
                "application/json"
            },
            body: JSON.stringify({
                topic
            })
        });

    const data =
        await response.json();

    document.getElementById(
        "output"
    ).innerText = data.report;
}