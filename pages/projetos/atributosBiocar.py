import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def atributos():
    st.title("Caracterização dos biocarvões")
    st.markdown("Os gráficos abaixo ajudam a visualizar as atributos dos biocarvões")

    selected_status = st.selectbox('Select o atributo desejado',
                                           options=['pH',
                                                    'Cálcio',
                                                    'Magnésio',
                                                    'Fósforo'])

    data = pd.read_csv("dados.csv")

    fig02 = plt.figure(figsize=(10, 5))

    if selected_status == 'pH':
        plt.bar(data.biocar, data.pH)
        plt.xlabel('Biocarvão', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('pH', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.show()

    elif selected_status == 'Cálcio':
        plt.bar(data.biocar, data.Ca)
        plt.xlabel('Biocarvão', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('Cálcio (dag/kg)', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.show()

    elif selected_status == 'Magnésio':
        plt.bar(data.biocar, data.Mg)
        plt.xlabel('Biocarvão', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('Magnésio (dag/kg)', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.show()

    elif selected_status == 'Fósforo':
        plt.bar(data.biocar, data.P)
        plt.xlabel('Biocarvão', fontweight='bold', color = 'black', fontsize='14', horizontalalignment='center')
        plt.ylabel('Fósforo (dag/kg)', fontweight='bold', color = 'black', fontsize='14', horizontalalignment='center')

        plt.show()

    st.pyplot(fig02)