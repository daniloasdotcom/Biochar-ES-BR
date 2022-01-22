import streamlit as st

def Projeto01():
    text01 = "<h1 style='text-align: center; line-height: 1.15'> Monitoramento de atributos do solo, " \
             "desenvolvimento e estado " \
             "nutricional de plantas de eucalipto em campo, sob aplicação de biocarvões</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.write("""
    ###  
    """)

    st.write("""
    ## Resumo
    """)

    text02 = "<p style='text-align: justify;'> Este experimento de campo é também uma continuação de um ensaio " \
             "estabelecido, em março de 2018 com recursos do EDITAL FAPES/SEAG Nº 06/2015, na área experimental do " \
             "IFES - Campus de Alegre. Neste ensaio os biocarvões de casca de eucalipto são testados em tratamentos " \
             "distribuídos num delineamento em blocos casualizados em um esquema fatorial 5 x 2, sendo cinco doses de " \
             "biocarvões (0; 0,25%; 0,5%; 1,0% e 2% em volume de biocarvões por volume de sulco) produzidos sob duas " \
             "temperaturas (350 ºc e 600 ºc).</p> "

    st.markdown(text02, unsafe_allow_html=True)

    st.latex('y = ax + b')

