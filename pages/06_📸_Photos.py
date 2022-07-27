import streamlit as st
from PIL import Image
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

def Galeria_photos():
    col1, col2 = st.columns([1, 1])

    img_biochar01 = Image.open("images/sulcoBiochar.png")
    img_biochar02 = Image.open("images/plantioEucalipto.png")

    img_biochar03 = Image.open("images/biocharBandeja.jpg")
    img_biochar04 = Image.open("images/campo04anos.jpg").rotate(270)
    img_biochar05 = Image.open("images/areaEucalipto.jpg").rotate(270)

    col1.image(img_biochar01, caption="Aplicação de Biocarvões em Sulco")
    col1.image(img_biochar05, caption="Visão interna da área - 4 anos")
    col1.image(img_biochar02, caption="Área de estudo - 12 meses após plantio")

    col2.image(img_biochar03, caption="Biocarvões de Casca de Eucalipto")
    col2.image(img_biochar04, caption="Coleta de solo - 4 anos")

Galeria_photos()
