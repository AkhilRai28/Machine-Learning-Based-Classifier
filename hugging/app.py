import gradio as gr
import tensorflow as tf
import librosa
import numpy as np
from skimage.transform import resize

model = tf.keras.models.load_model("training_model.h5")
labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

def preprocess_and_predict(audio):
    if audio is None:
        return "No audio provided."

    filepath = audio  # gradio provides a temporary filepath
    y, sr = librosa.load(filepath, sr=None)

    chunk_duration = 4
    overlap_duration = 2
    chunk_samples = chunk_duration * sr
    overlap_samples = overlap_duration * sr
    step = chunk_samples - overlap_samples
    num_chunks = int(np.ceil((len(y) - chunk_samples) / step)) + 1

    data = []
    for i in range(num_chunks):
        start = i * step
        chunk = y[start : start + chunk_samples]
        if len(chunk) < chunk_samples:
            chunk = np.pad(chunk, (0, chunk_samples - len(chunk)))

        mel_spec = librosa.feature.melspectrogram(y=chunk, sr=sr, n_mels=150)
        mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
        mel_resized = resize(mel_spec_db[..., np.newaxis], (150, 150, 1), preserve_range=True).astype(np.float32)
        data.append(mel_resized)

    X = np.array(data)
    preds = model.predict(X)
    pred_indices = np.argmax(preds, axis=1)
    final = np.bincount(pred_indices).argmax()

    return f"Predicted Genre: {labels[final]}"

# Create Gradio interface
interface = gr.Interface(
    fn=preprocess_and_predict,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="🎵 GTZAN Music Genre Classifier",
    description="Upload an audio clip (MP3/WAV). The model splits it into overlapping chunks, predicts each, and returns the most frequent genre."
)

if __name__ == "__main__":
    interface.launch()
