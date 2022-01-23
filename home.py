import streamlit as st
import pages.projetos.projeto01 as PageProjetos01
import pages.projetos.projeto02 as PageProjetos02
import pages.projetos.papers as papers

pj1 = "Experimento 01"
pj2 = "Experimento 02"
pj3 = "Artigos Publicados"


st.sidebar.title('Menu')
page_projeto = st.sidebar.selectbox('Escolha o Projeto de Pesquisa',
                                    [pj1, pj2, pj3])


def Choice():
    if page_projeto == pj1:
        PageProjetos01.Projeto01()

    elif page_projeto == pj2:
        PageProjetos02.Projeto02()

    elif page_projeto == pj3:
        papers.papers()


Choice()
