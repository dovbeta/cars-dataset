from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import torch
from PIL import Image
import io

app = FastAPI()

MODEL_PATH = "model/best.pt"
model = YOLO(MODEL_PATH)
model.fuse()

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data)).convert("RGB")

        results = model(image)[0]

        predictions = []
        for box in results.boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = box
            predictions.append({
                "bbox": [x1, y1, x2, y2],
                "confidence": round(conf, 3),
                "class_id": int(cls),
                "class_name": model.names[int(cls)]
            })

        return JSONResponse(content={"predictions": predictions})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
