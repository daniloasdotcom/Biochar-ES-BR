import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from pages.others.load_css import local_css

# Usando nosso recursos css
local_css("pages/others/style.css")

st.sidebar.image("images/projectLogo.png", use_column_width=True)

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('**General coordinator**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
st.sidebar.markdown('**Regional Researcher**: [Danilo Andrade](https://daniloas.com/)')

st.sidebar.markdown('**----- Team -----**')

st.sidebar.markdown('**Phd. Researcher**: [Lorena]()')
st.sidebar.markdown('**Master Researcher**: [Camila Barbieiro]()')
st.sidebar.markdown('**Technical support**: [Amanda Gomes](https://www.linkedin.com/in/amanda-g-3449349b/)')
st.sidebar.markdown('**Junior Researcher**: [Mateus Hastenreiter](http://lattes.cnpq.br/4351826031776108)')
st.sidebar.markdown('**Junior Researcher**: [Maria Eduarda](http://lattes.cnpq.br/1801516731947159)')
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

    col1.image(img_biochar01, caption="Application of Biochars in Furrows")
    col1.image(img_biochar05, caption="Eucalyptus Bark Biochars")
    col1.image(img_biochar02, caption="Internal view of the area - 4 years")

    col2.image(img_biochar03, caption="Soil collection - 4 years")
    col2.image(img_biochar04, caption="Study area - 12 months after planting")

Galeria_photos()