from fastapi import FastAPI, HTTPException, File, UploadFile
import numpy as np
import tensorflow as tf
import io
import librosa

# Initialize FastAPI app
app = FastAPI(
    title="Keras Music Classifier API",
    version="1.2.0",
    description="An API for serving predictions from a .keras music classification model. Accepts audio file uploads."
)

# Load the Keras model at startup
MODEL_PATH = "Trained_model.keras"
try:
    model = tf.keras.models.load_model(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model from {MODEL_PATH}: {e}")

# Audio processing parameters
SAMPLE_RATE = 22050         # Hz
DURATION = 30               # seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION
N_MELS = 128                # mel bands

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Upload an audio file (e.g., WAV, MP3) to get music genre predictions.
    The audio is loaded, trimmed/padded to {DURATION}s, converted to a Mel-spectrogram,
    then fed to the model.
    """
    try:
        # Read audio bytes
        contents = await file.read()
        data, sr = librosa.load(io.BytesIO(contents), sr=SAMPLE_RATE, mono=True)

        # Trim or pad to fixed length
        if len(data) > SAMPLES_PER_TRACK:
            data = data[:SAMPLES_PER_TRACK]
        else:
            padding = SAMPLES_PER_TRACK - len(data)
            data = np.pad(data, (0, padding), mode='constant')

        # Compute Mel-spectrogram
        mel_spec = librosa.feature.melspectrogram(y=data, sr=sr, n_mels=N_MELS)
        mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

        # Normalize to [0, 1]
        norm_mel = (mel_spec_db - mel_spec_db.min()) / (mel_spec_db.max() - mel_spec_db.min())

        # Model expects shape: (batch, height, width, channels)
        input_array = np.expand_dims(norm_mel, axis=(0, -1)).astype(np.float32)

        # Predict
        preds = model.predict(input_array)

        return {"filename": file.filename, "predictions": preds.tolist()}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Dependencies:
# pip install fastapi uvicorn tensorflow librosa numpy soundfile
#
# Example Usage:
# curl -X POST "http://localhost:8000/predict" \
#      -F "file=@path/to/song.mp3"
