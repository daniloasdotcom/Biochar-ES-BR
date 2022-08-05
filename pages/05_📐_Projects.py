import streamlit as st
import pages.projetos.projeto01 as PageProjetos01
import pages.projetos.projeto02 as PageProjetos02
import pages.projetos.projeto03 as PageProjetos03
from pages.others.load_css import local_css


# Usando nosso recursos css
local_css("pages/others/style.css")

pj1 = "Experiment 01"
pj2 = "Experiment 02"
pj3 = "Experiment 03"

st.sidebar.title('Menu De Projetos')
page_projeto = st.sidebar.selectbox('',
                                    [pj1, pj2, pj3])

st.sidebar.image("images/projectLogo.png", use_column_width=True)

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('**Coordinator**: [Danilo Andrade](https://daniloas.com/)')
st.sidebar.markdown('**Supervisor**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')

st.sidebar.markdown('**----- Volunteer team -----**')

st.sidebar.markdown('**Technical support**: [Amanda Gomes](https://www.linkedin.com/in/amanda-g-3449349b/)')
st.sidebar.markdown('**Junior Researcher**: [Mateus Hastenreiter](http://lattes.cnpq.br/4351826031776108)')
st.sidebar.markdown('**Junior Researcher**: [Maria Eduarda](http://lattes.cnpq.br/1801516731947159)')
st.sidebar.markdown('**Junior Researcher**: [Aurélio Martins](http://lattes.cnpq.br/2155060458456586)')
st.sidebar.markdown('**Junior Researcher**: Ueslei Machado')


st.sidebar.write("##")
st.sidebar.write("##")

def Choice():
    if page_projeto == pj1:
        PageProjetos01.Projeto01()

    elif page_projeto == pj2:
        PageProjetos02.Projeto02()

    elif page_projeto == pj3:
        PageProjetos03.Projeto03()

Choice()