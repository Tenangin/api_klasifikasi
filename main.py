import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
import joblib

app = FastAPI()

# Cek dan load model
if not os.path.exists("best_model_tf.h5") or not os.path.exists("scaler.save"):
    raise RuntimeError("Model atau scaler tidak ditemukan!")

model = tf.keras.models.load_model("best_model_tf.h5")
scaler = joblib.load("scaler.save")

labels = ["Normal", "Depression", "Bipolar Type-1", "Bipolar Type-2"]

class InputData(BaseModel):
    features: list[float]

@app.post("/predict")
async def predict(data: InputData):
    if len(data.features) != 17:
        raise HTTPException(status_code=400, detail="Harus 17 angka.")

    x = np.array([data.features], dtype=np.float32)
    x_scaled = scaler.transform(x)
    preds = model.predict(x_scaled)
    confidence = float(np.max(preds))
    label_idx = int(np.argmax(preds))
    result_label = labels[label_idx]

    return {
        "kondisi": result_label,
        "confidence": round(confidence, 4)
    }
