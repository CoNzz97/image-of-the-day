import streamlit as st
from backend import image_title, image_of_the_day, image_explanation

st.set_page_config(layout="wide", page_title="Image of the day.")
empty_col1, col1, empty_col2 = st.columns(3)

with col1:
    st.title(image_title)
    st.image(image_of_the_day)
    st.write(image_explanation)


