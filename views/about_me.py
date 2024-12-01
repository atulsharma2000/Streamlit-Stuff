import streamlit as st
from PIL import Image


from forms.contact import contact_form


@st.dialog("Contact Me")  # this is to show form in the pop up window
def show_contact_form():
    contact_form()


# ----hero section-------
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    # st.image("./", width=230)  # Directly referencing the image
    # Opening the image

    IMAGE_PATH = "./assests/my_2photo.png"
    IMAGE = Image.open(IMAGE_PATH)
    st.image(IMAGE, width=230)


with col2:
    st.title("Atul Sharma", anchor=False)
    # st.markdown("### Hi, I'm **Atul Sharma**")
    # st.markdown("### I'm a **Data Scientist**")
    # st.markdown(
    #     "### I'm passionate about **Machine Learning**, **Data Analysis**, and **Data Visualization**"
    # )
    # st.markdown("### I'm currently working on **Python**, **SQL**, and **Tableau**")
    st.write(
        "Data Science Enthusiast. I'm passionate about *Machine Learning*, *Data Analysis*, and *Data Visualization*"
    )
    if st.button("📧 Contact Me"):
        show_contact_form()  # when button is clicked go to this funciton  (pop up window having contact form)


# ---- Experience and qualifications
st.write("\n")
st.subheader("Qualifications & Experience", anchor=False)
# By setting anchor=False, you are essentially disabling the creation of an anchor ID for the header or subheader. This can be useful in situations where you don’t need or want to create a linkable anchor point.
st.write(
    """
    - I hold a Bachelor's degree in Computer Science from Poornima University, Jaipur.
    - Currently, I am enrolled in a Post Graduate Diploma in Big Data Analytics (PG-DBDA) at the Centre for Development of Advanced Computing (CDAC) in Pune.
    - I am an excellent team player, consistently collaborating with peers to achieve common goals.
    - I possess strong leadership skills, having led various group tasks during my academic career.
    - I have a passion for problem-solving and enjoy tackling complex challenges with innovative solutions.
    - My technical skills include proficiency in programming languages such as Python, Java, and SQL.
    - I am committed to continuous learning and staying updated with the latest trends in technology and data analytics.
    """
)

# --- skills---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: python (sckitlearn, pandas , steamlit , flask), sql , java, C/C++
    - Modeling : Logistic regression, linear regressionm decision trees
    - Databases: MySQL, PostgreSQL, MongoDB, Cassandra
    - Operating Systems: Windows, Linux
    - Data Science Tools: Tableau, Power BI, Excel, pandas, NumPy, Matplotlib
    """
)


# Define social media links
social_links = {
    "GitHub": {
        "url": "https://github.com/yourusername",
        "logo": "./views/img_dogu.jpg",
    },
    "LinkedIn": {
        "url": "https://www.linkedin.com/in/yourusername/",
        "logo": "./views/img_dogu.jpg",
    },
    "Twitter": {
        "url": "https://twitter.com/yourusername",
        "logo": "./views/img_dogu.jpg",
    },
}

# Display social media links in sidebar
st.header("Connect with Me!")

# Create a horizontal layout for social media links
cols = st.columns(len(social_links))
for col, (platform, info) in zip(cols, social_links.items()):
    logo = Image.open(info["logo"])
    col.image(logo, width=30)  # Adjust size as needed
    col.markdown(f"[{platform}]({info['url']})", unsafe_allow_html=True)
