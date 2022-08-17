import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pages.others.load_css import local_css

st.set_page_config(layout="wide")

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

selected = option_menu(menu_title="Chemical attributes of biochars",
                       options=["pH", "Cálcium", "Magnesium", "Phosphorus", "Potassium"],
                       menu_icon="cast",
                       default_index=0,
                       orientation="horizontal")

st.markdown("The graphs below help to visualize the attributes of biochars")

st.markdown("""<hr style="height:1px; border:none; color:#333; background-color:#333;" /> """,
            unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.25, 0.05, 2])

with col1:
    st.markdown('Biocarvões são conhecido por alterarem o pH do solos')


def atributos():
    data = pd.read_csv("files/dados.csv")

    fig02 = plt.figure(figsize=(12, 5))
    ax = plt.axes()
    labels = ['350 ºC', '600 ºC']

    if selected == 'pH':
        plt.barh(data.biocar,
                 data.pH,
                 height=0.7,
                 color=['gray', 'black'])

        plt.yticks(data.biocar,
                   labels,
                   fontsize=14,
                   fontweight='bold')

        plt.xticks(fontsize=14,
                   fontweight='bold')

        plt.xlabel('pH',
                   fontweight='bold',
                   color='black',
                   fontsize=15,
                   horizontalalignment='center',
                   labelpad=15)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_linewidth(3)
        ax.spines['left'].set_linewidth(3)

        plt.show()

    elif selected == 'Cálcium':
        plt.barh(data.biocar,
                 data.Ca,
                 height=0.5,
                 color=['gray', 'black'])

        plt.yticks(data.biocar,
                   labels,
                   fontsize=14,
                   fontweight='bold')

        plt.xticks(fontsize=14,
                   fontweight='bold')

        plt.xlabel('Calcium (dag/kg)',
                   fontweight='bold',
                   color='black',
                   fontsize=15,
                   horizontalalignment='center',
                   labelpad=15)

        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)

        ax.spines['bottom'].set_linewidth(3)
        ax.spines['left'].set_linewidth(3)

        plt.show()

    elif selected == 'Magnesium':
        plt.barh(data.biocar,
                 data.Mg,
                 height=0.5,
                 color=['gray', 'black'])

        plt.yticks(data.biocar,
                   labels,
                   fontsize=14,
                   fontweight='bold')

        plt.xticks(fontsize=14,
                   fontweight='bold')

        plt.xlabel('Magnesium (dag/kg)',
                   fontweight='bold',
                   color='black',
                   fontsize=15,
                   horizontalalignment='center',
                   labelpad=15)

        sns.despine()

        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)

        ax.spines['bottom'].set_linewidth(3)
        ax.spines['left'].set_linewidth(3)

        plt.show()

    elif selected == 'Phosphorus':
        plt.barh(data.biocar,
                 data.P,
                 height=0.5,
                 color=['gray', 'black'])

        plt.yticks(data.biocar,
                   labels,
                   fontsize=14,
                   fontweight='bold')

        plt.xticks(fontsize=14,
                   fontweight='bold')

        plt.xlabel('Phosphorus (dag/kg)',
                   fontweight='bold',
                   color='black',
                   fontsize=15,
                   horizontalalignment='center',
                   labelpad=15)

        sns.despine()

        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)

        ax.spines['bottom'].set_linewidth(3)
        ax.spines['left'].set_linewidth(3)

        plt.show()

    elif selected == 'Potassium':
        plt.barh(data.biocar,
                 data.K,
                 height=0.5,
                 color=['gray', 'black'])

        plt.yticks(data.biocar,
                   labels,
                   fontsize=14,
                   fontweight='bold')

        plt.xticks(fontsize=14,
                   fontweight='bold')

        plt.xlabel('Potassium (dag/kg)',
                   fontweight='bold',
                   color='black',
                   fontsize=15,
                   horizontalalignment='center',
                   labelpad=15)

        sns.despine()

        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)

        ax.spines['bottom'].set_linewidth(3)
        ax.spines['left'].set_linewidth(3)

        plt.show()

    st.pyplot(fig02)


with col3:
    atributos()