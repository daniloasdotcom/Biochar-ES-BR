import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pages.others.load_css import local_css

# Usando nosso recursos css
local_css("pages/others/style.css")


st.sidebar.image("images/projectLogo.png", use_column_width=True)

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('**Coordinator**: [Danilo Andrade](https://daniloas.com/)')
st.sidebar.markdown('**Supervisor**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')

st.sidebar.markdown('**----- Volunteer team -----**')

st.sidebar.markdown('**Technical support**: [Amanda Gomes](https://www.linkedin.com/in/amanda-g-3449349b/)')
st.sidebar.markdown('**Junior Researcher**: [Mateus Hastenreiter](http://lattes.cnpq.br/4351826031776108)')
st.sidebar.markdown('**Junior Researcher**: [Maria Eduarda](http://lattes.cnpq.br/1801516731947159)')
st.sidebar.markdown('**Junior Researcher**: [Aurélio Martins](http://lattes.cnpq.br/2155060458456586)')
st.sidebar.markdown('**Junior Researcher**: Ueslei Machado')

st.sidebar.write("##")
st.sidebar.write("##")


st.title("Atributos químicos dos biocarvões")
st.markdown("Os gráficos abaixo ajudam a visualizar as atributos dos biocarvões")

st.markdown("""<hr style="height:1px; border:none; color:#333; background-color:#333;" /> """,
                unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.25, 0.05, 2])

with col1:
    st.markdown('Biocarvões são conhecido por alterarem o pH do solos')

def atributos():

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
        plt.ylabel('Biochar total calcium (dag/kg)', fontweight='bold', color='black', fontsize='14',
                   horizontalalignment='center')
        plt.show()

    elif selected_status == 'Magnésio':
        plt.bar(data.biocar, data.Mg, color=("#3b3b3b", "#000000"), width=0.5)
        plt.xlabel('Biochar', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('Biochar total magnesium (dag/kg)', fontweight='bold', color='black', fontsize='14',
                   horizontalalignment='center')
        plt.show()

    elif selected_status == 'Fósforo':
        plt.bar(data.biocar, data.P, color=("#3b3b3b", "#000000"), width=0.5)
        plt.xlabel('Biochar', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('Biochar total phosphorus (dag/kg)', fontweight='bold', color='black', fontsize='14',
                   horizontalalignment='center')
        plt.show()

    elif selected_status == 'Potássio':
        plt.bar(data.biocar, data.K, color=("#3b3b3b", "#000000"), width=0.5)
        plt.xlabel('Biochar', fontweight='bold', color='black', fontsize='14', horizontalalignment='center')
        plt.ylabel('Biochar total potassium (dag/kg)', fontweight='bold', color='black', fontsize='14',
                   horizontalalignment='center')
        plt.show()

    st.pyplot(fig02)

with col3:
    atributos()

