# GTZAN Music Genre Classifier

Welcome to our project, a deep learning–powered music genre classification system trained on the GTZAN dataset. This repository contains all code, configurations, and documentation needed to reproduce our results and deploy the model in a Flutter/Dart Android application.

---

## 🚀 Project Overview

Our model is a hybrid **CNN–LSTM** model that processes audio as mel-spectrogram slices and captures both local timbral textures and temporal dynamics for high-accuracy genre recognition. By combining convolutional layers with a recurrent layer, our system achieves **94.51 %** overall accuracy on the GTZAN benchmark. In addition to research-grade performance, we’ve packaged the trained model as a **TensorFlow Lite** module ready for real-time, on-device inference in a Flutter mobile app.

---

## ✨ Key Features

- **State-of-the-Art Accuracy**  
  Achieves 94.51 % test accuracy, with macro-averaged precision, recall, and F1-score around 94 %.

- **Hybrid Architecture**  
  - Three Conv2D layers (32 → 64 → 128 filters; 3×3 kernels; ReLU activations; max-pooling; dropout)  
  - LSTM layer with 64 units for temporal modeling  
  - Dense + softmax output layer for 10 genre classes

- **Robust Preprocessing**  
  - Splits each 30 s track into 4 s chunks with 2 s overlap  
  - Computes 128-band log-mel spectrograms  
  - Optional data augmentation: time-stretching, pitch-shifting

- **End-to-End Pipeline**  
  Includes data loading, preprocessing, feature extraction, model training, evaluation, and mobile deployment.

- **Mobile Deployment**  
  - Conversion to TFLite for lightweight on-device inference  
  - Flutter/Dart integration example for Android

---

## 📦 Repository Structure

```

MLProjectCode/src/         
├── download.py                  # Download GTZAN dataset
├── preprocess.py                # Audio preprocessing and feature extraction
├── augmentations.py             # Data augmentation scripts
├── train.py                     # Model training script
├── evaluate.py                  # Model evaluation script
├── test.py                      # Optional testing utilities
├── requirements.txt             # Python dependencies

android/                        
├── AndroidManifest.xml          # Android config (part of Flutter app)
├── build.gradle                 # Android build file
└── ...                          # Other native Android project files

assets/                         
├── gtzan/                       # Raw GTZAN dataset
├── processed/                   # Preprocessed spectrogram data
├── model.tflite                 # Converted TFLite model for mobile
├── weights.h5                   # Trained Keras model weights
├── metrics.csv                  # Evaluation metrics
├── confusion_matrix.png         # Confusion matrix plot
└── spectrogram_sample.png       # Example mel-spectrogram image

build/                          
└── ...                          # Auto-generated build artifacts

hugging/                        
└── config.json                  # Config for Hugging Face (optional)

ios/                            
└── Runner.xcodeproj             # iOS Flutter project config

lib/                            
├── main.dart                    # Entry point for Flutter app
└── ...                          # Dart files (UI, controllers, services)

linux/                          
└── deploy.sh                    # Linux deployment script

macos/                          
└── deploy.sh                    # macOS deployment script

test/                           
├── test_main.dart               # Flutter unit tests
└── test_model.py                # Python model testing script

web/                            
└── index.html                   # Flutter web build entry point

windows/                        
└── deploy.bat                   # Windows deployment script

"Apk file Video"/               
└── demo.mp4                     # Screen recording or demo video of APK in action

LICENSE                          # Project license (Apache 2.0)

MusicClassifier.apk              # Pre-built Android APK for quick testing

README.md                        # Project overview and instructions (you are here)

documentation/                  
├── report.pdf                   # Final report / paper
└── architecture_diagram.png     # System architecture diagram

pubspec.yaml                     # Flutter project configuration

pubspec.lock                     # Locked Dart package version


````

---

## 🔧 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/gtzan-music-classifier.git
   cd gtzan-music-classifier

2. **Set up a Python environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt

4. **Download GTZAN dataset**

   ```bash
   python data/download.py --output_dir ./data/gtzan
   ```

---

## 🎬 Usage

### Preprocess & Augment Data

```bash
python data/preprocess.py --input_dir ./data/gtzan --output_dir ./data/processed
```

### Train the Model

```bash
python models/train.py \
  --data_dir ./data/processed \
  --epochs 100 \
  --batch_size 32 \
  --learning_rate 0.001 \
  --output_model ./results/weights.h5
```

### Evaluate Performance

```bash
python models/evaluate.py \
  --model_path ./results/weights.h5 \
  --data_dir ./data/processed \
  --metrics_output ./results/metrics.csv
```

---

## 📈 Results

* **Accuracy:** 94.51 %
* **Precision:** 0.945
* **Recall:** 0.942
* **F1-score:** 0.943

A full per-genre breakdown and confusion matrix are available in `results/metrics.csv` and `results/confusion_matrix.png`.

---

## 📱 Mobile App Integration

To try real-time on-device inference:

1. **Open the Flutter project**

   ```bash
   cd app
   flutter pub get
   ```

2. **Place the TFLite model**
   Copy `results/model.tflite` into `app/assets/`.

3. **Run on Android**

   ```bash
   flutter run
   ```

The app records a short audio clip and displays the predicted genre along with a confidence score. See `app/screenshots/` for example outputs.

---

## 🤝 Contributing

We welcome contributions! Please fork the repo, create a feature branch, and submit a pull request. Whether it’s improving model accuracy, adding new augmentation techniques, or refining the mobile UI, your expertise and ideas are invaluable.

## Drive Video Link
https://drive.google.com/file/d/1EuMoPz9W_E0SdqWrYXwbcJtRLfDmfPde/view?usp=drive_link
