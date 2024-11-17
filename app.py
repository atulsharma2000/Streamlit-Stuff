import streamlit as st

st.title("Awesome website !")

#  setting up the page
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",  
    # name taken from https://fonts.google.com/icons
    default=True,   # this means , the first page will be this page when we load the website
)

project_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
