# YOLOv8 Object Detection for Autonomous Vehicle Scenarios

## 📌 Overview
This project implements a **YOLOv8-based object detection model** designed to identify vehicles and road users commonly encountered in autonomous driving environments. The model focuses on real-time detection performance while maintaining reasonable accuracy across multiple object classes.

The project demonstrates an end-to-end object detection workflow, including dataset preparation, model training, evaluation, and inference.

---

## 🎯 Objective
To train and evaluate a **YOLOv8 object detection model** capable of identifying multiple vehicle and road user classes from traffic imagery.

---

## 🧠 Model Architecture
- **Model:** YOLOv8n (Nano)
- **Layers:** 73 (fused)
- **Parameters:** ~3.0 million
- **Compute Cost:** ~8.1 GFLOPs
- **Framework:** Ultralytics YOLOv8

YOLOv8n was selected for its lightweight design, making it suitable for **real-time or resource-constrained environments**.

---

## 📊 Dataset Summary
- **Validation Images:** 1,125
- **Total Instances:** 3,551
- **Number of Classes:** 11

**Detected Classes**
- articulated_truck  
- bicycle  
- bus  
- car  
- motorcycle  
- motorized_vehicle  
- non-motorized_vehicle  
- pedestrian  
- pickup_truck  
- single_unit_truck  
- work_van  

---

## 📈 Model Performance

### Overall Metrics
| Metric | Value |
|------|------|
| Precision | 0.48 |
| Recall | 0.46 |
| mAP@0.50 | 0.374 |
| mAP@0.50–0.95 | 0.27 |

### Observations
- Strong performance on common vehicle classes such as **cars, pickup trucks, and articulated trucks**
- Reduced accuracy on rare classes due to **class imbalance**
- Performance drop at higher IoU thresholds is expected for a lightweight model

---

## 🚀 Inference Example
```python
from ultralytics import YOLO

model = YOLO("runs/train/results_1/weights/best.pt")
model.predict("samples/", conf=0.15, save=True)
