import streamlit as st
from PIL import Image

st.title("My Certifications")

certificates = [
    "./assests/certis/MTA_python.png",
    "./assests/certis/python_certi.PNG",
    "./assests/certis/mlops.png",
    "./assests/certis/docker_.png",
    "./assests/certis/sql_certi.PNG",
    "./assests/certis/iitkgp_CA.png",
    "./assests/certis/nptel_design_and_eng.png",
    "./assests/certis/swayam_CN.png",
    "./assests/certis/VAPT_internshala.png",
    "./assests/certis/Coding_b_recm.png",
]


for cert_img in certificates:
    if cert_img:
        IMAGE = Image.open(cert_img)
        st.image(IMAGE, caption="***************", use_column_width=True)
    else:
        st.warning(f"Image {cert_img} not found in assets folder.")
