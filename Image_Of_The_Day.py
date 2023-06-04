import streamlit as st
from backend import image_title, image_of_the_day, image_explanation

st.set_page_config("wide")
st.title(image_title)
st.image(image_of_the_day)
st.write(image_explanation)


