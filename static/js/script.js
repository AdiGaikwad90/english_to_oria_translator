document.getElementById("translation-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var formData = new FormData(this);

    fetch("/translate", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("translated-text").innerText = decodeURIComponent(JSON.parse('"' + data.translated_text + '"'));
    })
    .catch(error => console.error("Error:", error));
});
