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

    text01 = "<h1 style='text-align: center; line-height: 1.15'> Roles of our Scrum Team</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.markdown('')
    st.markdown('')

    col1, col2, col3 = st.columns([1, 1, 1])

    # Primeira linha de imagens
    equipe01 = Image.open("images/danilo.png")
    equipe02 = Image.open("images/renato.png")
    equipe03 = Image.open("images/amanda.png")

    # Inserção das imagens
    col1.image(equipe01, caption="Danilo - Coordinator, PO and Scrum Master")
    col2.image(equipe02, caption="Renato R. Passos -  Supervisor, Stakeholder")
    col3.image(equipe03, caption="Amanda Gomes -  Volunteer Technical Support and Development Team")

    # Inserção da descrição
    with col1.expander("More about Danilo"):
        st.write("Danilo is an agronomist, passionate about puzzles, enjoys programming, practicing jiu-jitsu, "
                 "reading books, watching movies, and learning new languages. You can find out more about him in this "
                 "[link](https://daniloas.com)")

    with col2.expander("More about Renato"):
        st.write("Você saberá mais sobre ele em breve aqui")

    with col3.expander("More about Amanda"):
        st.write("Você saberá mais sobre ela em breve aqui")

    # Segunda linha de imagens
    equipe04 = Image.open("images/mateus.png")
    equipe05 = Image.open("images/duda.png")
    equipe06 = Image.open("images/aurelio.png")

    # Inserção das imagens
    col1.image(equipe04, caption="Mateus - Junior Researcher ans Development Team")
    col2.image(equipe05, caption="Maria Eduarda - Junior Researcher and Development Team")
    col3.image(equipe06, caption="Aurélio - Junior Researcher and Development Team")

    # Inserção da descrição
    with col1.expander("More about Mateus"):
        st.write("Você saberá mais sobre ele em breve aqui")

    with col2.expander("More about Maria Eduarda"):
        st.write("Você saberá mais sobre ela em breve aqui")

    with col3.expander("More about Aurélio"):
        st.write("Você saberá mais sobre ele em breve aqui")

    # Terceira linha de imagens
    equipe07 = Image.open("images/ueslei.png")

    # Inserção das imagens
    col1.image(equipe07, caption="Ueslei - Junior Researcher and Development Team")

    # Inserção da descrição
    with col1.expander("More about Ueslei"):
        st.write("Você saberá mais sobre ele em breve aqui")

team()