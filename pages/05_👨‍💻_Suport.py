import streamlit as st
from pages.others.sidebar_utils import configure_sidebar

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
        # Informações sobre os apoiadores
        st.write(
            "A [**Código Agro**](https://codigoagro.com/) dá suporte na manutenção deste site através do Projeto Dados Agro, \
            fornecendo recursos e suporte necessários para manter a página ativa e em funcionamento."
        )
        st.write(
            "O Projeto [**Dados Agro**](https://dadosagro.com/) é um projeto da Código Agro que dá suporte na produção de gráficos \
            e gestão de dados apresentados neste site e no desenvolvimento dos experimentos."
        )

pagina_apoio()
