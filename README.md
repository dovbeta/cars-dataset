# Car Detection Dataset Preparation

This repository contains the dataset preparation pipeline for training a Computer Vision model to detect cars in images. The dataset includes images of vehicles annotated with bounding boxes in **YOLO format**, and the dataset is version-controlled using **DVC (Data Version Control)**.

## 🔍 Project Overview

The goal of this project is to:

- Collect and label car images.
- Annotate vehicles using bounding boxes.
- Export annotations in **YOLO format**.
- Use **Label Studio** for manual annotation.
- Use **DVC** for dataset versioning and reproducibility.

---

## 📁 Dataset Structure (YOLO Format)

After annotation export and formatting, the dataset is structured as follows:

```
dataset/
├── images/
│   ├── 1.png
│   └── ...
├── labels/
│   ├── image_001.txt
│   └── ...
├── classes.txt
└── notes.json
```

Each `.txt` file inside the `labels/` folders contains YOLO-formatted bounding box annotations:
```
<class_id> <x_center> <y_center> <width> <height>
```
All coordinates are normalized (values between 0 and 1).

---

## 🛠 Tools Used

- **Label Studio** – for annotating images with bounding boxes.
- **DVC** – for dataset versioning and reproducibility.
- **Git** – for version control of code and metadata.

---

## 🧾 Annotation Workflow

1. Upload images to **Label Studio**.
2. Annotate each car with a bounding box.
3. Export annotations as YOLO-format text files.
4. Track the dataset using DVC.

---

## 📦 DVC Setup & Usage

### Initialize DVC

```bash
dvc init
```

### Track Dataset

```bash
dvc add dataset
```

### Commit to Git

```bash
git add dataset.dvc
git commit -m "Add YOLO-formatted dataset with DVC tracking"
```

### (Optional) Configure Remote and Push

```bash
dvc remote add -d myremote <remote_url>
dvc push
```

---

## 📚 Usage

This dataset is ready for training with YOLOv5/YOLOv8 or other object detection models that support YOLO format. Ensure that:
- Classes are defined in a `classes.txt` file.


---

## 📌 Versioning

Use DVC to track any dataset changes (new annotations, new splits, etc.).

To revert or reproduce a previous version:

```bash
git checkout <commit_hash>
dvc checkout
```

To push updates:

```bash
git commit -am "Updated annotations"
dvc push
```

---

## 🧑‍💻 Author

Roman Dovbeta — for educational use at **SET University**.  
You are welcome to fork or contribute!