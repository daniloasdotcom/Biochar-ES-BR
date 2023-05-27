import streamlit as st
from pages.others.load_css import local_css

st.sidebar.image("images/projectLogo.png", use_column_width=True)

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('**General coordinator**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
st.sidebar.markdown('**Regional Researcher**: [Danilo Andrade](https://daniloas.com/)')

st.sidebar.markdown('**----- Team -----**')

st.sidebar.markdown('**Phd. Researcher**: [Lorena]()')
st.sidebar.markdown('**Master Researcher**: [Camila Barbieiro]()')
st.sidebar.markdown('**Technical support**: [Amanda Gomes](https://www.linkedin.com/in/amanda-g-3449349b/)')
st.sidebar.markdown('**Junior Researcher**: [Mateus Hastenreiter](http://lattes.cnpq.br/4351826031776108)')
st.sidebar.markdown('**Junior Researcher**: [Maria Eduarda](http://lattes.cnpq.br/1801516731947159)')
st.sidebar.markdown('**Junior Researcher**: Ueslei Machado')

st.sidebar.write("##")
st.sidebar.write("##")

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

st.image("images/projectLogo.png", use_column_width=True)