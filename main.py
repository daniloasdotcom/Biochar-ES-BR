import streamlit as st
import pages.projetos.home as home
import pages.projetos.projeto01 as PageProjetos01
import pages.projetos.projeto02 as PageProjetos02
import pages.projetos.projeto03 as PageProjetos03
import pages.projetos.papers as papers
import pages.projetos.sprints as sprints
import pages.projetos.equipe as equipe
import pages.projetos.atributosBiocar as atributos
import pages.projetos.publica as publica
import pages.projetos.pg06galeriaPhotos as GaleriaPhotos

st.set_page_config(page_title='Biochar Project')

pj0 = "Home"
pj1 = "Experiment 01"
pj2 = "Experiment 02"
pj3 = "Experiment 03"
pj4 = "Publications"
pj5 = "Publication in production"
pj6 = "Photo gallery"
pj7 = "Progress"
pj8 = "Biochar's atributes"
pj9 = "Team"

st.sidebar.image("images/projectLogo.png", use_column_width=True)

st.sidebar.title('Menu')
page_projeto = st.sidebar.selectbox('Choose a page of interest',
                                    [pj0, pj1, pj2, pj3, pj4, pj5, pj6, pj7, pj8, pj9])

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

def Choice():
    if page_projeto == pj0:
        home.home()

    elif page_projeto == pj1:
        PageProjetos01.Projeto01()

    elif page_projeto == pj2:
        PageProjetos02.Projeto02()

    elif page_projeto == pj3:
        PageProjetos03.Projeto03()

    elif page_projeto == pj4:
        papers.papers()

    elif page_projeto == pj5:
        publica.publica()

    elif page_projeto == pj6:
        GaleriaPhotos.Galeria_photos()

    elif page_projeto == pj7:
        sprints.sprints()

    elif page_projeto == pj8:
         atributos.atributos()

    elif page_projeto == pj9:
         equipe.team()

Choice()
