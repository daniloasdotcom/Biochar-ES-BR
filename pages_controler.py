import streamlit as st
import pages.projetos.projeto01 as PageProjetos01
import pages.projetos.projeto02 as PageProjetos02
import pages.projetos.papers as papers
import pages.projetos.sprints as sprints

pj1 = "Experimento 01"
pj2 = "Experimento 02"
pj3 = "Artigos Publicados"
pj4 = "Tarefas da semana"


st.sidebar.title('Menu')
page_projeto = st.sidebar.selectbox('Escolha um página de interesse',
                                    [pj1, pj2, pj3, pj4])

def Choice():
    if page_projeto == pj1:
        PageProjetos01.Projeto01()

    elif page_projeto == pj2:
        PageProjetos02.Projeto02()

    elif page_projeto == pj3:
        papers.papers()

    elif page_projeto == pj4:
        sprints.sprints()

Choice()
