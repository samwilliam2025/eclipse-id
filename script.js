const form = document.getElementById("upload-form");
const resultMessage = document.getElementById("result-message");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const fileInput = document.getElementById("image-upload");
  const file = fileInput.files[0];

  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("https://seuprojeto.lovable.app/upload-image", {
    method: "POST",
    body: formData,
  });

  const result = await response.json();

  if (result.status === "encontrada") {
    resultMessage.textContent = `Imagem encontrada: ${result.image_url}`;
  } else {
    resultMessage.textContent = "Imagem não encontrada. Tente novamente.";
  }
});
