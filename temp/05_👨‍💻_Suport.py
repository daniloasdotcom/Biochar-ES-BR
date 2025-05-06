import streamlit as st
from others.sidebar_utils import configure_sidebar

def pagina_apoio():
    configure_sidebar()  # Chama a função para configurar a barra lateral

    # Título da página
    st.title("Apoio e Manutenção")

    # Organizando em duas colunas para alinhamento horizontal
    col1, col2 = st.columns([1, 2])

    with col1:
        # Inserir logo da Código Agro e Dados Agro com largura padronizada
        st.image("images/codigo_agro.png", width=150)
        st.image("images/dados_agro.png", width=200)

    with col2:
        # Information about the supporters
        st.write(
            "[**Código Agro**](https://codigoagro.com/) provides support in maintaining this website through the Dados Agro Project, \
            offering the necessary resources and support to keep the page active and running."
        )
        st.write(
            "The [**Dados Agro**](https://dadosagro.com/) Project is an initiative by Código Agro that supports the production of graphs \
            and data management presented on this site, as well as the development of experiments."
        )

pagina_apoio()
