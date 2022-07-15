import streamlit as st
from pages.others.load_css import local_css

# Usando nosso recursos css
local_css("pages/others/style.css")

def Projeto02():
    text01 = "<h1 style='text-align: center; line-height: 1.15'>Disponibilidade de fósforo em agregados de diferentes " \
             "classes de tamanho após incubação com biocarvão</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.write("""
    ###  
    """)

    st.write("""
    ## Resumo
    """)

    text02 = "<p style='text-align: justify;'> Este experimento será estabelecido em laboratório. Biocarvões serão " \
             "acrescido a amostras de solo a fim de promover a formação de agregados e em seguida serão analisados " \
             "quanto ao conteúdo e disponibilidade de P para diferentes classes de agregados formados. Sendo que o P " \
             "extraível com água representa o P facilmente disponível na planta, enquanto o P extraível com NaHCO3 " \
             "também inclui P lábil adsorvido na superfície dos óxidos e hidróxidos de Fe e Al ou carbonato de cálcio " \
             "(CaCO3). Já P extraível via os extratos ácidos (usando HCl e/ou H2SO4) representam o fosfato " \
             "prontamente disponível ligado à Ca, Fe e Al "

    st.markdown(text02, unsafe_allow_html=True)

