import streamlit as st
import re
import requests     # for webhook
# Lets setup no-code  tool  to process the form message , by this we can setup whole automation flow like forwarding the message to email account or saving it to a database
# - So to trigger the automation flow , we can use webhooks 
# - Webhooks are just informing no code tools every time there is new submission


WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZjMDYzMTA0M2M1MjZmNTUzMDUxMzAi_pc"

def is_valid_email(email):
    # basic regex for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None



# making it a function so that we can import it  in our about_me page
def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")
        
        
        if submit_button: # for now static , so just show message
            if not WEBHOOK_URL:
                st.error(
                    "Email service is not set up. Please try again later.", icon="📧"
                )
                st.stop()
            
            if not name:
                st.error("Please provide you name.",icon="👦")
                st.stop()
                
            if not email:
                st.error("Please provide your email address.",icon="📧")
                st.stop()
                
            if not is_valid_email(email):
                st.error("Please provide a valid email address.",icon="📧")
                st.stop()
            
            if not message:
                st.error("Please provide your message.",icon="📝")
                st.stop()
            
            # st.success("Thank you for your message! I will get back to you soon.")
            
            # prepare the data payload and send it to the specified webhook url
            data = {"email": email,"name":name,"message":message}
            response = requests.post(WEBHOOK_URL,json=data)
            
            if response.status_code == 200:
                st.success("Your message has been sent successfully!🎉 I will get back to you soon. 🤝")
            else:
                st.error("There was an error sending your message." , icon= "🥲")
            