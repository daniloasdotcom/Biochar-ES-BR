import streamlit as st
from PIL import Image
from pages.others.load_css import local_css

st.set_page_config(layout="wide")

def home():
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

    # Usando nosso recursos css
    local_css("pages/others/style.css")

    # criando 3 colunas
    col1, col2, col3 = st.columns([1, 6, 1])

    img_biochar01 = Image.open("images/biochar.png")

    st.markdown("""<hr style="height:1px; border:none; color:#333; background-color:#333;" /> """,
                unsafe_allow_html=True)

    col2.image(img_biochar01, width=1920, use_column_width=True)

    text04 = "<h1 style='text-align: center; line-height: 1.15'>Fontes de Financiamento</h1> "

    st.markdown(text04, unsafe_allow_html=True)

    st.markdown("""<hr style="height:1px; border:none; color:#333; background-color:#333;" /> """,
                unsafe_allow_html=True)

    text01 = "<h5 style='text-align: center; line-height: 1.15'>EDITAL FAPES Nº 019/2022 CHAMADA DE APOIO A NÚCLEOS " \
             "CAPIXABAS DE EXCELÊNCIA EM PESQUISA</h5> "

    st.markdown(text01, unsafe_allow_html=True)

    text02 = "<p style='text-align: justify; line-height: 2'>Descreva aqui os objetivos do financiamento</p>" \
             "<p style='text-align: justify; line-height: 2'><b>Coordenador: </b></p>"

    st.markdown(text02, unsafe_allow_html=True)

    st.write("""
            ###
            """)

    text03 = "<h5 style='text-align: justify; line-height: 1.15'>FAPES/CNPq Nº 11/2019 - Regional Scientific and " \
             "Technological Development Program  – PDCTR 2019</h5> "

    st.markdown(text03, unsafe_allow_html=True)

    text04 = "<p style='text-align: justify; line-height: 2'>Descreva aqui os objetivos do financiamento</p> "

    st.markdown(text04, unsafe_allow_html=True)

    st.write("""
            ###
            """)

    text05 = "<h5 style='text-align: justify; line-height: 1.15'>EDITAL CNPq/FAPES Nº 23/2018 - PROGRAMA DE APOIO A " \
             "NÚCLEOS EMERGENTES - PRONEM</h5> "

    st.markdown(text05, unsafe_allow_html=True)

    text06 = "<p style='text-align: justify; line-height: 2'>Descreva aqui os objetivos do financiamento</p> "

    st.markdown(text06, unsafe_allow_html=True)

    st.write("""
            ###
            """)

    text07 = "<h5 style='text-align: justify; line-height: 1.15'>FAPES - EDITAL FAPES/SEAG Nº 06/2015 - PPE AGROPECUÁRIA</h5> "

    st.markdown(text07, unsafe_allow_html=True)

    text08 = "<p style='text-align: justify; line-height: 2'>Descreva aqui os objetivos do financiamento</p> "

    st.markdown(text08, unsafe_allow_html=True)


home()