import streamlit as st

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email Address")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        st.success("Thank you for your message! I will get back to you soon.")