import streamlit as st
from PIL import Image

def home():
    # criando 3 colunas
    col1, col2, col3 = st.columns([1, 6, 1])

    img_biochar01 = Image.open("images/sulcoBiochar.png")

    col2.image(img_biochar01, width=1920, use_column_width=True)

    text01 = "<h1 style='text-align: center; line-height: 1.15'> Potential for the use of biochars as soil " \
             "conditioners and eucalyptus production</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    text02 = "<h5 style='text-align: center; line-height: 1.15'>Fapes/Cnpq Nº 11/2019 - Regional Scientific and " \
             "Technological Development Program  – PDCTR 2019</h5> "

    st.markdown(text02, unsafe_allow_html=True)

    st.write("""
        ###  
        """)

    text03 = "<p style='text-align: justify; line-height: 2'>Biochars have drawn the attention of Soil Science to the " \
             "understanding of their effects on the chemical, physical and biological attributes of soils. The State " \
             "of Espírito Santo has, within the areas of agricultural production, materials that are generated in " \
             "large volume and with the potential to be used for energy conversion and consequent production of " \
             "biochars to return to the field as soil conditioners. The present study is a continuation of the " \
             "research developed within the soil laboratory of the Centro de Ciências Agrarias e Engenharias of the " \
             "Federal University of Espírito Santo in order to obtain insights into the effectiveness of the use of " \
             "organic residues and to present solutions for the efficient use of fertilizers in soils. highly " \
             "weathered.</p> "

    st.markdown(text03, unsafe_allow_html=True)



