import streamlit as st



#  setting up the pages

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


# --------setting the navigation [ without section]
#   pg = st.navigation(pages=[about_page,project_1_page,project_2_page])

#   ------Setting navigation [ with section ]
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page,project_2_page]
    }
)


#----shared on all pages

st.logo("assests/atul_3logo.png",size="large")
st.sidebar.text("Made by 🧑‍💻 Atul 🧑‍💻")

# run the navigation
pg.run()