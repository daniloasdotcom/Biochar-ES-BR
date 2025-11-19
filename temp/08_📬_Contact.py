import streamlit as st
from others.load_css import local_css
from others.sidebar_utils import configure_sidebar

configure_sidebar()  # Chama a função para configurar a barra lateral

# Usando nosso recursos css
local_css("pages/others/style.css")

st.header("Get In Touch With Us")

contact_form = """
<form action="https://formsubmit.co/danilo_as@live.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

st.image("images/projectLogo.png", use_container_width=True)