import streamlit as st
import streamlit.components.v1 as components

def pagina_apoio():
    # Título da página
    st.title("Apoio e Manutenção")

    # Organizando em duas colunas para alinhamento horizontal
    col1, col2 = st.columns(2)

    with col1:
        # Inserir logo da Código Agro e Dados Agro
        st.image("images/codigo_agro.png", use_column_width=True)
        st.image("images/dados_agro.png", use_column_width=True)

    with col2:
        # Informações sobre os apoiadores
        st.write(
            "A [**Código Agro**](https://codigoagro.com/) dá suporte na manutenção deste site através do Projeto Dados Agro, \
            fornecendo recursos e suporte necessários para manter a página ativa e em funcionamento."
        )
        st.write(
            "O Projeto [**Dados Agro**](https://dadosagro.com/) é um projeto da Código Agro que dá suporte na produção de gráficos \
            e gestão de dados apresentados neste site e no desenvolvimento do experimentos."
        )

pagina_apoio()