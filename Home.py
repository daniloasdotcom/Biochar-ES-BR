import streamlit as st
from PIL import Image
from pages.others.load_css import local_css

st.set_page_config(layout="wide")


def home():
    st.sidebar.image("images/projectLogo.png", use_column_width=True)

    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('**General Coordinator**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
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

    col2.image(img_biochar01, width=1080, use_column_width=True)

    text01 = "<h1 style='text-align: center; line-height: 1.15'> Potential for the use of biochars as soil " \
             "conditioners</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.markdown("""<hr style="height:1px; border:none; color:#333; background-color:#333;" /> """,
                unsafe_allow_html=True)

    st.write("""
        ###  
        """)

    text03 = "<p style='text-align: justify; line-height: 2'>Biochars have aroused great interest in the scientific " \
             "community specialized in soil science due to their effects on the chemical, physical and biological " \
             "attributes of soils. Within this context, the State of Espírito Santo-Brazil stands out as a region with vast " \
             "potential for the production of materials that can be converted into biochar used as a soil " \
             "conditioner.</p> "

    st.markdown(text03, unsafe_allow_html=True)

    text04 = "<p style='text-align: justify; line-height: 2'>In order to disseminate the results and progress of " \
             "research conducted by the soil group of the Federal University of Espírito Santo-Brazil, under the " \
             "guidance of " \
             "Professor <a " \
             "href='https://lattes.cnpq.br/3882320619443256'><span class='highlight blue'>Renato Ribeiro " \
             "Passos</span></a> and supervision of Researcher <a " \
             "href='https://lattes.cnpq.br/7543705744207270'><span class='highlight blue'>Danilo Andrade Santos" \
             "</span></a> , this website was created. Here you will find information about the progress of our research group's activities.</p> "

    st.markdown(text04, unsafe_allow_html=True)


home()
