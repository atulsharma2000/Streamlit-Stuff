import streamlit as st
from PIL import Image

st.title("My Achievements")

achievements = [
    "./assests/certis/achievements/covidthon.jpg",
    "./assests/certis/VAPT_internshala.png",
    "./assests/certis/Coding_b_recm.png",
    "./assests/certis/iitkgp_CA.png",
]


for achiv_img in achievements:
    if achiv_img:
        IMAGE = Image.open(achiv_img)
        st.image(IMAGE, caption="***************", use_column_width=True)
    else:
        st.warning(f"Image {achiv_img} not found in assets folder.")
