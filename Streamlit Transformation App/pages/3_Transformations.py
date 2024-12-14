import streamlit as st
import cv2
from PIL import Image
import numpy as np

# Title and Description
st.title("Image Transformation App")
st.write("Upload an image and adjust transformations using the sliders.")

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.image(img_array, caption="Original Image", use_column_width=True)

    # Brightness Slider
    brightness = st.slider("Adjust Brightness", -100, 100, 0)
    adjusted = cv2.convertScaleAbs(img_array, alpha=1, beta=brightness)
    st.image(adjusted, caption="Brightness Adjusted")

    # Rotation Slider
    angle = st.slider("Rotate Image (Degrees)", -180, 180, 0)
    rows, cols = img_array.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated = cv2.warpAffine(adjusted, M, (cols, rows))
    st.image(rotated, caption="Rotated Image")

    # Scaling Slider
    scale = st.slider("Scale Image", 0.1, 3.0, 1.0)
    scaled = cv2.resize(rotated, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    st.image(scaled, caption="Scaled Image")

    # Skewing Example
    skew = st.slider("Skew Factor", -0.5, 0.5, 0.0)
    M = np.float32([[1, skew, 0], [skew, 1, 0]])
    skewed = cv2.warpAffine(scaled, M, (cols, rows))
    st.image(skewed, caption="Skewed Image")
