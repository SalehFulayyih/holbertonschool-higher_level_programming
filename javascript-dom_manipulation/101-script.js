document.addEventListener("DOMContentLoaded", function() {
    const btnTranslate = document.getElementById('btn_translate');
    const languageSelect = document.getElementById('language_code');
    const helloDiv = document.getElementById('hello');

    btnTranslate.addEventListener('click', function() {
        const lang = languageSelect.value;

        if (lang === "") {
            helloDiv.textContent = "Please select a language";
            return;
        }

        fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
            .then(response => response.json())
            .then(data => {
                helloDiv.textContent = data.hello || "Translation not found";
            })
            .catch(error => {
                console.error('Error:', error);
                helloDiv.textContent = "Error fetching translation";
            });
    });
});
