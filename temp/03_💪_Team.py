import streamlit as st
from PIL import Image
from others.load_css import local_css
from others.sidebar_utils import configure_sidebar

# Usando nosso recursos css
local_css("pages/others/style.css")

def team():
    configure_sidebar()  # Chama a função para configurar a barra lateral

    text01 = "<h1 style='text-align: center; line-height: 1.15'>Main Team</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.markdown('')
    st.markdown('')

    col1, col2, col3 = st.columns([1, 2, 1])

    # Primeira linha de imagens
    equipe01 = Image.open("images/danilo.png")
    equipe02 = Image.open("images/renato.png")

    # Inserção das imagen
    col2.image(equipe02, caption="Renato R. Passos")
    with col2.expander("More about Renato"):
        st.write("[Renato Passos](https://lattes.cnpq.br/3882320619443256)")

    # Inserção da descrição
    col2.image(equipe01, caption="Danilo Andrade")
    with col2.expander("More about Danilo"):
        st.write("[Danilo Andrade](https://daniloas.com)")
team()