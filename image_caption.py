from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load the processor
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Load the BLIP model
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def generate_caption(image):
    """
    Generates a caption for the given image.

    Args:
        image (PIL.Image): Input image

    Returns:
        str: Generated caption
    """

    # Convert image into tensors
    inputs = processor(images=image, return_tensors="pt")

    # Generate caption
    output = model.generate(**inputs)

    # Convert token IDs into text
    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption