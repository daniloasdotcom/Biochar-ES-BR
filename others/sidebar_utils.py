# sidebar_utils.py
import streamlit as st

def configure_sidebar():
    # Adicionar estilo CSS para mudar a cor e sublinhar os links na barra lateral
    st.markdown("""
        <style>
        /* Muda a cor e sublinha os links dentro da barra lateral */
        section[data-testid="stSidebar"] a {
            color: red !important;
        }
        </style>
        """, unsafe_allow_html=True)

    st.sidebar.image("images/projectLogo.png", use_column_width=True)

    st.sidebar.markdown('')
    st.sidebar.markdown('[**Danilo Andrade**](https://daniloas.com/)', unsafe_allow_html=True)
    st.sidebar.write("##")
    st.sidebar.write("##")
