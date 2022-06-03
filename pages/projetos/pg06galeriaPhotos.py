import streamlit as st
from PIL import Image

def Galeria_photos():
    col1, col2 = st.columns([1, 1])

    img_biochar01 = Image.open("images/sulcoBiochar.png")
    img_biochar02 = Image.open("images/plantioEucalipto.png")

    img_biochar03 = Image.open("images/biocharBandeja.jpg")
    img_biochar04 = Image.open("images/campo04anos.jpg").rotate(270)
    img_biochar05 = Image.open("images/areaEucalipto.jpg").rotate(270)

    col1.image(img_biochar01, caption="Aplicação de Biocarvões em Sulco")
    col1.image(img_biochar02, caption="Área de estudo - 12 meses após plantio")

    col2.image(img_biochar03, caption="Biocarvões de Casca de Eucalipto")
    col2.image(img_biochar04, caption="Coleta de solo - 4 anos")
    col2.image(img_biochar05, caption="Visão interna da área - 4 anos")
