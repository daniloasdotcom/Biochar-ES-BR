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
                                            'Fósforo',
                                            'Potássio'])

    data = pd.read_csv("files/dados.csv")

    fig02 = plt.figure(figsize=(10, 5))

    if selected_status == 'pH':
        plt.bar(data.biocar, data.pH, color=("#3b3b3b", "#000000"), width=0.5)
        plt.title("pH of Biochars")
        plt.xlabel('Biochar', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('pH', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.show()

    elif selected_status == 'Cálcio':
        plt.bar(data.biocar, data.Ca, color=("#3b3b3b", "#000000"), width=0.5)
        plt.xlabel('Biochar', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('Biochar total calcium (dag/kg)', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.show()

    elif selected_status == 'Magnésio':
        plt.bar(data.biocar, data.Mg, color=("#3b3b3b", "#000000"), width=0.5)
        plt.xlabel('Biochar', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('Biochar total magnesium (dag/kg)', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.show()

    elif selected_status == 'Fósforo':
        plt.bar(data.biocar, data.P, color=("#3b3b3b", "#000000"), width=0.5)
        plt.xlabel('Biochar', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('Biochar total phosphorus (dag/kg)', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.show()

    elif selected_status == 'Potássio':
        plt.bar(data.biocar, data.K, color=("#3b3b3b", "#000000"), width=0.5)
        plt.xlabel('Biochar', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('Biochar total potassium (dag/kg)', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.show()

    st.pyplot(fig02)
