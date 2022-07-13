import streamlit as st
from PIL import Image

def team():
    st.sidebar.image("images/projectLogo.png", use_column_width=True)

    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('**Coordinator**: [Danilo Andrade](https://daniloas.com/)')
    st.sidebar.markdown('**Supervisor**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
    st.sidebar.markdown('**Technical support**: [Amanda Gomes](https://www.linkedin.com/in/amanda-g-3449349b/)')
    st.sidebar.markdown('**Junior Researcher**: [Mateus Hastenreiter](http://lattes.cnpq.br/4351826031776108)')
    st.sidebar.markdown('**Junior Researcher**: [Maria Eduarda](http://lattes.cnpq.br/1801516731947159)')
    st.sidebar.markdown('**Junior Researcher**: [Aurélio Martins](http://lattes.cnpq.br/2155060458456586)')
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
    col1.image(equipe01, caption="Danilo - PO and Scrum Master")
    col2.image(equipe02, caption="Renato R. Passos -  Stakeholder")
    col3.image(equipe03, caption="Amanda Gomes -  Development Team")

    # Inserção da descrição
    with col1.expander("More about Danilo"):
        st.write("""
            Danilo é Agrônomo, apaixonado por quebra-cabeças, gosta de programar, 
            treinar jiu-jitsu, ler livros, assistir filmes, e aprender novos idiomas. Você pode conhecer mais sobre 
            ele nesse [link](https://daniloas.com)."
        """)

    with col2.expander("More about Renato"):
        st.write("Você saberá mais sobre ele em breve aqui")

    with col3.expander("More about Amanda"):
        st.write("Você saberá mais sobre ela em breve aqui")

    # Segunda linha de imagens
    equipe04 = Image.open("images/mateus.png")
    equipe05 = Image.open("images/duda.png")
    equipe06 = Image.open("images/aurelio.png")

    # Inserção das imagens
    col1.image(equipe04, caption="Mateus - Development Team")
    col2.image(equipe05, caption="Maria Eduarda - Development Team")
    col3.image(equipe06, caption="Aurélio - Development Team")

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
    col1.image(equipe07, caption="Ueslei - Development Team")

    # Inserção da descrição
    with col1.expander("More about Ueslei"):
        st.write("Você saberá mais sobre ele em breve aqui")

team()