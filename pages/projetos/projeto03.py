import streamlit as st
import matplotlib.pyplot as plt


def Projeto03():
    text01 = "<h1 style='text-align: center; line-height: 1.15'>Fontes de Alcalinidade em Biocarvões </h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.write("""
    ###  
    """)

    st.write("""
    ## Resumo
    """)

    text02 = "<p style='text-align: justify;'> Biocarvões, em sua maior parte, apresentam propriedades alcalinas e " \
             "possuem a capacidade de elevar o pH de solos ácidos com consequentes efeitos sobre a disponibilidade de " \
             "nutrientes às plantas (JEFFERY et al., 2017). A literatura relata pelo menos quatro fontes de " \
             "alcalinidade nos biocarvões. São elas: (i) grupos funcionais orgânicos de superfície de pKa elevado (" \
             "grupos funcionais diretamente ligados à matriz aromática condensada dos biochar, tais como –COO- e –O- " \
             "capazes de aceitar prótons), (ii) compostos orgânicos solúveis (compostos orgânicos que apresentam " \
             "grupos funcionais capazes de aceitar prótons), (iii) carbonatos e (iv) outros compostos inorgânicos (" \
             "definidos como compostos inorgânicos solúveis em ácido presentes nos biocarvões, tais como fosfatos, " \
             "sulfatos, silicatos, hidróxidos de ferro e hidróxidos de alumínio, capazes de aceitar prótons em suas " \
             "ligações) (FIDEL et al., 2017)</p> "

    st.markdown(text02, unsafe_allow_html=True)

    text03 = "<p style='text-align: justify;'> A figura a seguir é um exemplo de como o pH dos biocarvões pode ser"\
             "influenciado pela temperatura de produção dos biocarvões</p> "

    st.markdown(text03, unsafe_allow_html=True)


    # Gráfico de pH de biocarvões
    data = {'CE 350ºC': 5.5, 'CE 600ºC': 6.5, 'PC 350ºC': 6.3, 'PC 600ºC': 7.0}

    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(courses, values)
    plt.xlabel("Biocarvões")
    plt.ylabel("pH dos biocarvões")
    plt.title("pH dos biocarvões em diferentes temperaturas")
    st.pyplot(fig)