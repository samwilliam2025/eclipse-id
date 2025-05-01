from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    # Aqui você pode adicionar a lógica para processar a imagem, como comparar com um banco de dados ou fazer verificação.
    # Por enquanto, vamos simular um resultado de imagem encontrada com uma URL fictícia.

    result = {
        "status": "encontrada",
        "message": "Imagem encontrada!",
        "image_url": "https://example.com/imagem-falsa.jpg"  # Exemplo de URL de imagem
    }

    return JSONResponse(content=result)
