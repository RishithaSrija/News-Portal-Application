import streamlit as st
import smtplib
from email.mime.text import MIMEText
import random
import string

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def send_code_email(recipient_email, code):
    subject = "Your Password Reset Code"
    body = f"Hello,\n\nYour password reset code is: {code}\n\nUse this code to reset your password."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('your_email@gmail.com', 'your_app_password')  # Use App Password
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

def forgot_password_page():
    st.markdown("<h1 style='text-align:center; color:#e62c2c;'>❓ Forgot Password</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ccc;'>Enter your email to receive a reset code</p>", unsafe_allow_html=True)

    email = st.text_input("Email")

    if st.button("Send Code"):
        if email:
            code = generate_code()
            # You can store this code in session or database for later verification
            st.session_state.reset_code = code
            if send_code_email(email, code):
                st.success(f"A reset code has been sent to {email}")
        else:
            st.warning("Please enter a valid email address.")

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.stop()
