import streamlit as st
from PIL import Image
from pages.others.load_css import local_css
from pages.others.sidebar_utils import configure_sidebar

st.set_page_config(
    page_title="Biochar Website",
    page_icon="🌱",
    layout="wide"
)

def home():
    configure_sidebar()  # Chama a função para configurar a barra lateral

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

    text03 = "<p style='text-align: justify; line-height: 2'>Biochars have generated great interest in the scientific " \
             "community specialized in soil science due to their positive effects on the chemical, physical, and biological " \
             "attributes of soils. In this context, the state of Espírito Santo, Brazil, stands out as a region with vast " \
             "potential for the production of materials that can be converted into biochar, used as soil conditioners.</p>"

    st.markdown(text03, unsafe_allow_html=True)

    text04 = "<p style='text-align: justify; line-height: 2'>In 2012, I, <a href='https://daniloas.com/' target='_blank'>" \
             "<span class='highlight blue'>Danilo Andrade Santos</span></a>, accompanied Professor <a href='https://lattes.cnpq.br/3882320619443256'>" \
             "<span class='highlight blue'>Renato Ribeiro Passos</span></a> during his postdoctoral research at the Federal " \
             "University of Viçosa (UFV), where we initiated studies on biochars. These research activities were later continued " \
             "at the Federal University of Espírito Santo (UFES). Through this website, you can follow my research activities " \
             "with biochars developed at UFES in collaboration with Professor Renato Ribeiro Passos.</p>"

    st.markdown(text04, unsafe_allow_html=True)

    text05 = "<p style='text-align: justify; line-height: 2'>To learn more about me and my other areas of expertise, " \
             "you can visit my personal website at <a href='https://daniloas.com/' target='_blank'>" \
             "<span class='highlight blue'>daniloas.com</span></a>. There, you will find my homepage, " \
             "where you can also explore my portfolio page, which presents my main projects, " \
             "skills, and academic and professional trajectory.</p>"

    st.markdown(text05, unsafe_allow_html=True)

# Tornar esta página a primeira a ser exibida no Streamlit
if __name__ == "__main__":
    home()
