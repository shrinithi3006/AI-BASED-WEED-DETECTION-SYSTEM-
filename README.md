# 🌱 AI-Based Weed Detection System for Smart Agriculture

> An AI-powered weed detection system that uses **YOLO (You Only Look Once)** and **ESP32-CAM** to identify weeds in agricultural fields, helping farmers improve crop management through precision agriculture.

---

## 📖 Overview

Weed infestation significantly reduces crop yield and increases farming costs. Traditional weed removal methods require extensive manual labor and are time-consuming.

This project proposes an **AI-based weed detection system** capable of identifying weeds in real time using a trained YOLO model integrated with an ESP32-CAM. The system can be further extended to perform automatic weed removal or targeted herbicide spraying.

---

## 🎯 Objectives

- Detect weeds accurately using Artificial Intelligence.
- Distinguish weeds from crops using computer vision.
- Capture real-time images through ESP32-CAM.
- Reduce manual weed identification.
- Improve precision farming techniques.

---

## ✨ Features

- 🌿 Real-time weed detection
- 🤖 YOLO-based object detection
- 📷 ESP32-CAM image acquisition
- 🧠 AI-powered image classification
- ⚡ Fast inference
- 📊 Detection result visualization
- 🌾 Precision agriculture support

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Model Development |
| YOLO | Object Detection |
| OpenCV | Image Processing |
| ESP32-CAM | Image Capture |
| Arduino IDE | ESP32 Programming |
| Google Colab | Model Training |
| Roboflow / LabelImg | Dataset Annotation |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```
AI-Based-Weed-Detection-System
│
├── Dataset/
│
├── Training/
│   ├── train.py
│   ├── detect.py
│   └── data.yaml
│
├── Trained_Model/
│
├── ESP32_CAM/
│
├── Arduino_Code/
│
├── Images/
│
├── Results/
│
├── docs/
│   ├── Project_Report.pdf
│   └── Presentation.pptx
│
└── README.md
```

---

## 📊 Dataset

The dataset consists of annotated images containing:

- Crop Images
- Weed Images
- Mixed Crop & Weed Images

The dataset was labeled using annotation tools and trained using the YOLO framework.

---

## 🧠 Model Training

The YOLO model was trained using:

- Custom annotated dataset
- Image augmentation
- Multiple training epochs
- Validation dataset
- Performance evaluation metrics

--
## 📈 Results

The trained model is capable of detecting weeds from agricultural images with good accuracy.

Example outputs include:

- Weed Detection
- Bounding Box Prediction
- Confidence Score
- Crop Identification


## 🙏 Acknowledgements

This project was developed as part of the Bachelor's Degree Final Year Project in Electronics and Instrumentation Engineering.

Special thanks to our project guide, faculty members, and department for their continuous support.

---

⭐ If you found this project useful, consider giving it a star!
