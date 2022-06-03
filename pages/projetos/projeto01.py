import streamlit as st
from PIL import Image

def Projeto01():
    col1, col2, col3 = st.columns([1, 6, 1])

    img_biochar02 = Image.open("images/plantioEucalipto.png")

    col2.image(img_biochar02, width=1920, use_column_width=True)

    text01 = "<h1 style='text-align: center; line-height: 1.15'> Monitoring of soil attributes, development and " \
             "nutritional status of eucalyptus plants in the field, under application of biochars</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.write("""
    ###  
    """)

    st.write("""
    ## Resumo
    """)

    text02 = "<p style='text-align: justify;'> In March 2018, a field trial was started using resources from EDITAL " \
             "FAPES/SEAG Nº 06/2015, in the experimental area of IFES - Campus de Alegre - Brazil. In this assay, " \
             "eucalyptus bark biochars are tested in treatments distributed in a randomized block design in a 5 x 2 " \
             "factorial scheme, with five doses of biochars (0; 0.25%; 0.5%; 1.0% and 2 % by volume of biochars by " \
             "volume of furrow) produced under two temperatures (350 ºc and 600 ºc). The trial is now maintained with " \
             "resources from Fapes/Cnpq Nº 11/2019 - Regional technological and scientific development program - " \
             "PDCTR 2019.</p> "

    st.markdown(text02, unsafe_allow_html=True)

