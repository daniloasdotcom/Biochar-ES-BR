import streamlit as st
from PIL import Image
from pages.others.load_css import local_css
from pages.others.sidebar_utils import configure_sidebar

# Usando nosso recursos css
local_css("pages/others/style.css")

configure_sidebar()  # Chama a função para configurar a barra lateral

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