import streamlit as st
from PIL import Image, ImageEnhance
import numpy as np

# Title and Description
st.title("Image Transformation App")
st.write("Upload an image and adjust transformations using the sliders.")

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Brightness Slider
    brightness = st.slider("Adjust Brightness", -100, 100, 0)
    enhancer = ImageEnhance.Brightness(image)
    bright_factor = 1 + (brightness / 100)
    bright_image = enhancer.enhance(bright_factor)
    st.image(bright_image, caption="Brightness Adjusted")

    # Rotation Slider
    angle = st.slider("Rotate Image (Degrees)", -180, 180, 0)
    rotated_image = bright_image.rotate(-angle, expand=True)
    st.image(rotated_image, caption="Rotated Image")

    # Scaling Slider
    scale = st.slider("Scale Image", 0.1, 3.0, 1.0)
    new_width = int(image.width * scale)
    new_height = int(image.height * scale)
    scaled_image = rotated_image.resize((new_width, new_height))
    st.image(scaled_image, caption="Scaled Image")

    # Skewing Example (Using Affine Transform with Numpy)
    skew = st.slider("Skew Factor", -0.5, 0.5, 0.0)
    width, height = scaled_image.size
    skew_matrix = (1, skew, 0, skew, 1, 0)
    skewed_image = scaled_image.transform(
        (width, height), Image.AFFINE, skew_matrix, resample=Image.BICUBIC
    )
    st.image(skewed_image, caption="Skewed Image")
