import streamlit as st
from PIL import Image

def team():
    text01 = "<h1 style='text-align: center; line-height: 1.15'> Roles of our Scrum Team</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.markdown('')
    st.markdown('')

    col1, col2, col3 = st.columns([1, 1, 1])

    # Primeira linha de imagens
    equipe01 = Image.open("images/danilo.png")
    equipe02 = Image.open("images/renato.png")
    equipe03 = Image.open("images/amanda.png")

    # Inserção das imagens
    col1.image(equipe01, caption="Danilo - PO and Scrum Master")
    col2.image(equipe02, caption="Renato R. Passos -  Stakeholder")
    col3.image(equipe03, caption="Amanda Gomes -  Development Team")

    # Inserção da descrição
    with col1.expander("More about Danilo"):
        st.write("""
            Danilo é Agrônomo, apaixonado por quebra-cabeças, nos tempos livres gosta de programar, 
            treinar jiu-jitsu, ler livros, assistir filmes, e dormir. Você pode conhecer mais sobre 
            ele nesse [link](https://daniloas.com)."
        """)

    with col2.expander("More about Renato"):
        st.write("Você saberá mais sobre ele em breve aqui")

    with col3.expander("More about Amanda"):
        st.write("Você saberá mais sobre ela em breve aqui")

    # Segunda linha de imagens

    # Primeira linha de imagens
    equipe04 = Image.open("images/mateus.png")
    equipe05 = Image.open("images/duda.png")
    equipe06 = Image.open("images/aurelio.png")

    # Inserção das imagens
    col1.image(equipe04, caption="Mateus - Development Team")
    col2.image(equipe05, caption="Maria Eduarda - Development Team")
    col3.image(equipe06, caption="Aurélio - Development Team")

    # Inserção da descrição
    with col1.expander("More about Mateus"):
        st.write("Você saberá mais sobre ele em breve aqui")

    with col2.expander("More about Maria Eduarda"):
        st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi"
                 "/streamlit_app.py) e continua aqui")

    with col3.expander("More about Aurélio"):
        st.write("Você saberá mais sobre ele em breve aqui")

