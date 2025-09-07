# 📸 SelfieOnSmile – OpenCV Project

This project detects a smile in real-time using **OpenCV** and automatically captures a selfie when you smile.
I built this by following a YouTube tutorial and, along the way, learned about **OpenCV basics, face detection, and smile detection** using Haarcascade classifiers.

---

## 🚀 Features

* Real-time **face detection** using Haarcascade
* **Smile detection** with Haarcascade
* Automatically captures and saves a **selfie when a smile is detected**
* Works with **webcam feed**
* Press **`q`** anytime to quit the program

---

## 🛠️ Tech Stack

* **Python 3**
* **OpenCV (cv2)**
* **Haarcascade Classifiers**

---

## ⚙️ Steps Involved

1. **Import OpenCV** (`cv2`)
2. **Start webcam** using `cv2.VideoCapture()`
3. **Load Haarcascade XML files** for face and smile detection
4. **Continuous frame capture** (video = series of images) using `while True`
5. **Convert frames to grayscale** (`cv2.cvtColor`) for better feature detection
6. **Detect faces** using `detectMultiScale()`

   * **ScaleFactor**: Adjusts zoom level (recommended `1.1`)
   * **minNeighbors**: Number of neighbors to retain detection
7. **Draw rectangle** around detected faces (`cv2.rectangle`)
8. If a **smile is detected inside the face**, capture and **save the image** using `cv2.imwrite()`
9. **Press `q`** to exit the program
10. **Release resources** and close all windows

---

## 📂 Project Structure

```
SelfieOnSmile-OpenCV-project/
│── haarcascade_frontalface_default.xml
│── haarcascade_smile.xml
│── selfie_on_smile.py
│── README.md
│── /saved_images
```

---

## ▶️ How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/0504ankitsharma/SelfieOnSmile-OpenCV-project.git
   cd SelfieOnSmile-OpenCV-project
   ```

2. Install dependencies:

   ```bash
   pip install opencv-python
   ```

3. Run the script:

   ```bash
   python selfie_on_smile.py
   ```

4. Smile 😄 → Your picture will be saved in `/saved_images/`

---

## 📚 Learning Outcomes

Through this project, I learned:

* How to use **OpenCV** for real-time video processing
* **Face and smile detection** with Haarcascades
* How to capture and save frames using OpenCV

---

## 🙌 Acknowledgements

* OpenCV official documentation
* YouTube tutorial 

---
