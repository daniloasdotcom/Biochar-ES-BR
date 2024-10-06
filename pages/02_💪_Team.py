import streamlit as st
from PIL import Image
from pages.others.load_css import local_css

# Usando nosso recursos css
local_css("pages/others/style.css")

def team():
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

    text01 = "<h1 style='text-align: center; line-height: 1.15'>Main Team</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.markdown('')
    st.markdown('')

    col1, col2 = st.columns([1, 1])

    # Primeira linha de imagens
    equipe01 = Image.open("images/danilo.png")
    equipe02 = Image.open("images/renato.png")

    # Inserção das imagens
    col1.image(equipe01, caption="Danilo - Coordinator, PO and Scrum Master")
    col2.image(equipe02, caption="Renato R. Passos -  Supervisor, Stakeholder")

    # Inserção da descrição
    with col1.expander("More about Danilo"):
        st.write("Danilo is an agronomist, passionate about puzzles, enjoys programming, practicing jiu-jitsu, "
                 "reading books, watching movies, and learning new languages. You can find out more about him in this "
                 "[link](https://daniloas.com)")

    with col2.expander("More about Renato"):
        st.write("Você saberá mais sobre ele em breve aqui")


team()