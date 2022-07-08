import streamlit as st
from PIL import Image

def home():
    # criando 3 colunas
    col1, col2, col3 = st.columns([1, 6, 1])

    img_biochar01 = Image.open("images/biochar.png")

    col2.image(img_biochar01, width=1920, use_column_width=True)

    text01 = "<h1 style='text-align: center; line-height: 1.15'> Potential for the use of biochars as soil " \
             "conditioners and eucalyptus production</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    text02 = "<h5 style='text-align: center; line-height: 1.15'>FAPES/CNPq Nº 11/2019 - Regional Scientific and " \
             "Technological Development Program  – PDCTR 2019</h5> "

    st.markdown(text02, unsafe_allow_html=True)

    st.write("""
        ###  
        """)

    text03 = "<p style='text-align: justify; line-height: 2'>Biochars have drawn the attention of Soil Science to the " \
             "understanding of their effects on the chemical, physical and biological attributes of soils. In this " \
             "context, the State of Espírito Santo has, within the areas of agricultural production, materials that " \
             "are generated in large volume and with the potential to be used for energy conversion and consequent " \
             "production and reuse of biochars to return to the field as soil conditioners.</p> "

    st.markdown(text03, unsafe_allow_html=True)

    text04 = "<p style='text-align: justify; line-height: 2'>My name is <a href='https://daniloas.com'>Danilo</a>, " \
             "Regional Scholarship Researcher and " \
             "coordinator of the present set of studies on biochars as soil conditioners under the supervision of " \
             "Professor <a href='http://lattes.cnpq.br/3882320619443256'>Renato Ribeiro Passos</a> and funding from " \
             "the Fundação de " \
             "Amparo à Pesquisa e Inovação do " \
             "Espírito Santo and the National Council for Scientific and Technological Development.</p> "

    st.markdown(text04, unsafe_allow_html=True)

    text05 = "<p style='text-align: justify; line-height: 2'>And this is the website created to publicize the " \
             "progress of research approved and developed from the FAPES/CNPq No. of Espírito Santo with the " \
             "objective of obtaining insights into the effectiveness of the use of carbonized organic waste and " \
             "presenting solutions for its use as soil conditioners.</p> "

    st.markdown(text05, unsafe_allow_html=True)
