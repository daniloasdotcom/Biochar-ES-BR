import streamlit as st

def publica():
    text01 = "<h1 style='text-align: center; line-height: 1.15'>Publicações em produção</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.write("""
    ## Capítulos de livros
    """)

    text02 = "<p style='text-align: justify;'> Efeitos dos biocarvões sobre a agregação dos solos</p> "

    st.markdown(text02, unsafe_allow_html=True)

    text03 = "<p style='text-align: justify;'> Funcionalização de biocarvões </p> "

    st.markdown(text03, unsafe_allow_html=True)

    text04 = "<p style='text-align: justify;'>A relação entre microrganismo e fósforo do solo</p> "

    st.markdown(text04, unsafe_allow_html=True)

    text05 = "<p style='text-align: justify;'>Métodos de caracatização química de biocarvões</p> "

    st.markdown(text05, unsafe_allow_html=True)

    st.write("""
        ## Artigos
        """)

    text06 = "<p style='text-align: justify;'> Biochar: Soil Aggregation from Degraded Pastures </p> "

    st.markdown(text06, unsafe_allow_html=True)