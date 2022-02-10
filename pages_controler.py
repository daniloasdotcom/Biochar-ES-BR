import streamlit as st
import pages.projetos.home as home
import pages.projetos.projeto01 as PageProjetos01
import pages.projetos.projeto02 as PageProjetos02
import pages.projetos.papers as papers
import pages.projetos.sprints as sprints
import pages.projetos.publica as publica

pj0 = "Inicio"
pj1 = "Experimento 01"
pj2 = "Experimento 02"
pj3 = "Artigos Publicados"
pj4 = "Tarefas da semana"
pj5 = "Publicação em produção"


st.sidebar.title('Menu')
page_projeto = st.sidebar.selectbox('Escolha um página de interesse',
                                    [pj0, pj1, pj2, pj3, pj4, pj5])

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('**Coordenação**: [Danilo Andrade](https://daniloas.com/)')
st.sidebar.markdown('**Supervisão**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
st.sidebar.markdown('**Iniciação científica**: [Amanda Gomes](https://www.linkedin.com/in/amanda-g-3449349b/)')
st.sidebar.markdown('**Iniciação científica**: Mateus Hastenreiter')
st.sidebar.markdown('**Iniciação científica**: Maria Eduarda')
st.sidebar.markdown('**Iniciação científica**: Aurélio Martins')


def Choice():
    if page_projeto == pj0:
        home.home()

    elif page_projeto == pj1:
        PageProjetos01.Projeto01()

    elif page_projeto == pj2:
        PageProjetos02.Projeto02()

    elif page_projeto == pj3:
        papers.papers()

    elif page_projeto == pj4:
        sprints.sprints()

    elif page_projeto == pj5:
        publica.publica()

Choice()
