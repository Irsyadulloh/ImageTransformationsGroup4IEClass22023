import streamlit as st

# Configure the Streamlit app
st.set_page_config(
    page_title="Image Transformation Project",
    page_icon="🖼️",
    layout="wide"
)

st.title("Welcome to the Image Transformation Project")
st.write("Navigate to different pages using the sidebar on the left.")

st.sidebar.success("Select a page above.")
