# YOLOv8 Inference API with FastAPI

This project provides an API endpoint for performing inference using a trained YOLOv8 object detection model.


## 🚀 Features
- Accepts image input via HTTP POST (`/predict`)
- Performs object detection on the image using YOLOv8
- Returns detected bounding boxes, confidence scores, and class names
- Health check endpoint (`/ping`)


## 📦 Run the API

```bash
docker build -t fastapi-lr-model .
docker run --env-file .env -p 8080:8080 fastapi-lr-model
```

It will be available at:

```
http://localhost:8080
```

## 📡 API Usage

### Endpoint: `/predict`
**Method:** POST  
**Payload:** Multipart form with a single image file field `file`

Example using `curl`:

```bash
curl -X POST "http://localhost:8080/predict" -F "file=@cat.jpg"
```

### Response JSON Example

```json
{
  "predictions": [
    {
      "bbox": [x1, y1, x2, y2],
      "confidence": 0.91,
      "class_id": 0,
      "class_name": "cat"
    },
    ...
  ]
}
```

## 📝 Notes
- The model should be trained using Ultralytics YOLOv8.
- You can update the `MODEL_PATH` in `main.py` if needed.

## 🧑‍💻 Author
Roman Dovbeta — for educational use at **SET University**.  
You are welcome to fork or contribute!