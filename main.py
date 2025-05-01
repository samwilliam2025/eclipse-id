from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Form, File, UploadFile

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API está funcionando!"}

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    return JSONResponse(content={"filename": file.filename})
