import streamlit as st
import pandas as pd
from send_email import send_email

st.header('Contact Me')
df = pd.read_csv("topics.csv")

with st.container():
    with st.form(key='contact_form'):
        user_email = st.text_input('Enter your email address')
        user_topic = st.selectbox('What topic would you want to discuss?', df["topics"])
        user_message = st.text_area('Enter your message')
        submit_button = st.form_submit_button('Submit')
        st.session_state.update()

        if submit_button:
            send_email(user_email, user_message, user_topic)
            st.info('Email sent!')
