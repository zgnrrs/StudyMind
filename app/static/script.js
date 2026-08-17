let selectedFile = null;

async function uploadPDF() {
    const fileInput = document.getElementById("pdfFile");
    const file = fileInput.files[0];

    if (!file) {
        alert("Lütfen bir PDF seç.");
        return;
    }

    selectedFile = file;

    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("result").classList.add("hidden");

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:8000/upload-pdf", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("PDF yüklenemedi.");
        }

        const data = await response.json();

if (data.error) {
    alert(data.error);
    return;
}

document.getElementById("summary").innerHTML = marked.parse(data.summary);
        document.getElementById("studyMaterial").innerHTML =
    marked.parse(data.study_material);

        document.getElementById("result").classList.remove("hidden");

    } catch (error) {
        alert("Bir hata oluştu: " + error.message);
    }

    document.getElementById("loading").classList.add("hidden");
}


async function generateQuestions() {
    if (!selectedFile) {
        alert("Önce PDF yüklemelisin.");
        return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    const button = document.querySelector(
        '#result button[onclick="generateQuestions()"]'
    );

    const originalText = button.textContent;

    button.disabled = true;
    button.textContent = "⏳ Sorular oluşturuluyor...";

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/generate-questions",
            {
                method: "POST",
                body: formData
            }
        );

        if (!response.ok) {
            throw new Error("Sorular oluşturulamadı.");
        }

        const data = await response.json();

        document.getElementById("questions").innerHTML =
    marked.parse(data.questions);
        document.getElementById("questionsSection").classList.remove("hidden");

    } catch (error) {
        alert("Bir hata oluştu: " + error.message);

    } finally {
        button.disabled = false;
        button.textContent = originalText;
    }
}

document.getElementById("pdfFile").addEventListener("change", function () {
    const file = this.files[0];
    const selectedFile = document.getElementById("selectedFile");

    if (file) {
        selectedFile.textContent = "📄 " + file.name;
        selectedFile.classList.remove("hidden");
    }
});