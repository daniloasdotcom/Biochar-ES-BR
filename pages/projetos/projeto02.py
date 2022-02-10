import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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

    data = {'CE 350ºC': 5.5, 'CE 600ºC': 6.5, 'PC 350ºC': 6.3, 'PC 600ºC': 7.0}
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(courses, values)
    plt.xlabel("Biocarvões")
    plt.ylabel("pH dos biocarvões")
    plt.title("pH dos biocarvões em diferentes temperaturas")
    st.pyplot(fig)