import gradio as gr
from PIL import Image
from image_caption import generate_caption


def caption_image(img):
    """
    Receives an image from Gradio,
    converts it to PIL format,
    and returns the generated caption.
    """
    image = Image.fromarray(img)
    caption = generate_caption(image)
    return caption


interface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="numpy", label="Upload an Image"),
    outputs=gr.Textbox(label="Generated Caption"),
    title="🖼️ AI Image Caption Generator",
    description="Upload any image and let the BLIP Transformer model generate an AI caption."
)

interface.launch(server_name="0.0.0.0")