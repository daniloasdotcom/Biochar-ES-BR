# sidebar_utils.py
import streamlit as st

def configure_sidebar():
    st.sidebar.image("images/projectLogo.png", use_column_width=True)

    st.sidebar.markdown('')
    st.sidebar.markdown('Chief Researchers')
    st.sidebar.markdown('[Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
    st.sidebar.markdown('[Danilo Andrade](https://daniloas.com/)')
    st.sidebar.write("##")
    st.sidebar.write("##")
