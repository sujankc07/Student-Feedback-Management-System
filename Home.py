
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


st.set_page_config(
    page_title="Feedback Management",
)

st.markdown("<h1 style='text-align: center; color: white;'>Student Feedback App</h1>", unsafe_allow_html=True)
img=Image.open('image.png')
st.image(img)
