# 🚘 Autonomous Vehicle Safety Analysis  
### Object Detection & Incident Data Analysis

## 📘 Project Overview
This project explores **autonomous vehicle safety** through a two-part analytical approach that combines **computer vision** and **data-driven incident analysis**.

- **Part 1** focuses on visual perception by training a **YOLOv8 object detection model** to identify vehicles and road users in traffic scenes.
- **Part 2** analyzes **reported Tesla-related fatalities** using structured incident data to uncover trends in incident severity and occupant outcomes.

Together, these components provide a holistic view of autonomous vehicle safety, linking **machine learning–based perception systems** with **real-world safety data analysis**.

## 🚀 Running Inference (YOLOv8)

This section demonstrates how to run inference using the trained YOLOv8 model
on sample images provided in the repository.

Trained model weights are not included in this repository.
Users can reproduce results by running the training notebook or supplying their own trained weights.

## Design Decisions
- Chose YOLOv8n to balance inference speed and accuracy
- Used normalized YOLO label format for consistency and scalability
- Accepted lower performance on rare classes due to dataset imbalance
- Prioritized interpretability and evaluation over raw accuracy

## Metrics
Performance varies across classes due to class imbalance in the dataset.
High-frequency classes such as cars and pickup trucks show stronger recall,
while rare classes (e.g., motorcycles) exhibit lower performance.
This reflects real-world dataset constraints rather than model failure.



### Using a Python script
```bash
python src/infer_yolov8.py \
  --weights path/to/best.pt \
  --source samples/images \
  --conf 0.15




