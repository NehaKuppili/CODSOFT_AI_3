# 🖼️ AI Image Caption Generator

An AI-powered web application that automatically generates meaningful captions for uploaded images using the **BLIP (Bootstrapping Language-Image Pre-training)** transformer model from Hugging Face.

This project was developed as part of the **CodSoft Artificial Intelligence Internship – Task 3**.

---

## 🚀 Live Demo

🌐 **Try the application here:**

https://nehakuppili-task3-ai-image-captioning.hf.space

> If you're using the Hugging Face Space page instead, replace the link above with:
> https://huggingface.co/spaces/nehakuppili/task3_ai_image_captioning

---

## 📸 Features

- Upload any image
- AI-generated descriptive captions
- Powered by the BLIP Transformer model
- Simple and interactive Gradio interface
- Fast and user-friendly

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
git clone https://github.com/YOUR_GITHUB_USERNAME/TASK3_AI_IMAGECAPTIONING.git
cd TASK3_AI_IMAGECAPTIONING
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```
http://127.0.0.1:7860
```

---

## 🧠 Model Used

**Salesforce BLIP Image Captioning Base**

The BLIP model combines computer vision and natural language processing to analyze images and generate human-readable captions.

---

## 📖 How It Works

1. Upload an image.
2. The BLIP processor converts the image into tensors.
3. The BLIP model analyzes the image.
4. The model generates a descriptive caption.
5. The generated caption is displayed in the Gradio interface.

---

## 🎯 Future Enhancements

- Multiple caption suggestions
- Caption download option
- Batch image captioning
- Enhanced user interface

---

## 👩‍💻 Author

**Neha Kuppili**

Developed for the **CodSoft Artificial Intelligence Internship**.
