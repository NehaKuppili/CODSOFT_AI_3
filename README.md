# 🖼️ AI Image Caption Generator

An AI-powered web application that automatically generates descriptive captions for uploaded images using the **BLIP (Bootstrapping Language-Image Pre-training)** model from Hugging Face.

This project was developed as part of the **CodSoft Artificial Intelligence Internship – Task 3**.

---

## 🚀 Features

- Upload any image
- Automatically generates accurate image captions
- Powered by the BLIP Transformer model
- Simple and interactive Gradio interface
- Fast and easy to use

---

## 🛠️ Technologies Used

- Python
- Gradio
- Hugging Face Transformers
- PyTorch
- Pillow

---

## 📂 Project Structure

```
TASK3_AI_IMAGECAPTIONING/
│── app.py
│── image_caption.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/TASK3_AI_IMAGECAPTIONING.git
cd TASK3_AI_IMAGECAPTIONING
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:7860
```

---

## 🧠 Model Used

**Salesforce BLIP Image Captioning Base**

The model combines computer vision and natural language processing to understand image content and generate meaningful captions.

---

## 📸 How It Works

1. Upload an image.
2. The BLIP processor converts the image into tensors.
3. The BLIP model analyzes the image.
4. The model generates a descriptive caption.
5. The caption is displayed in the Gradio interface.

---

## 🎯 Future Improvements

- Generate multiple caption suggestions
- Support batch image captioning
- Add caption download functionality
- Improve UI with custom themes

---

## 👩‍💻 Author

**Neha Kuppili**

Developed for the **CodSoft Artificial Intelligence Internship**.