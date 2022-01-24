import streamlit as st
import pages.projetos.projeto01 as PageProjetos01
import pages.projetos.projeto02 as PageProjetos02
import pages.projetos.papers as papers
import pages.projetos.sprints as sprints


def home():
    text01 = "<h1 style='text-align: center; line-height: 1.15'> Potencial de uso de biocarvões como condicionadores " \
             "de solo e produção de eucalipto</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    text02 = "<h5 style='text-align: center; line-height: 1.15'>Edital Fapes/Cnpq Nº 11/2019 - Programa de " \
             "desenvolvimento Científico e Tecnológico Regional – PDCTR 2019</h5> "

    st.markdown(text02, unsafe_allow_html=True)

    text03 = "<p style='text-align: justify; line-height: 1.15'>Os biocarvões têm chamado a atenção da Ciência do " \
             "Solo para a compreensão dos seus efeitos sobre os atributos químicos, físicos e biologicos dos solos. O " \
             "Estado do Espírito Santo " \
             "possui, dentro das áreas de produção agricola, materiais que são gerados em grande volume e com " \
             "potencial para serem " \
             "utilizados para conversão energética e consequente produção de biocarvões para retornarem ao campo como " \
             "condicionadores de solo. O presente estudo é uma continuação das pesquisas desenvolvidas dentro do " \
             "laboratório de solos do Centro de Ciências Agrarias e Engenharias da Universidade Federal do Espírito " \
             "Santo a fim de alcançar insights para eficácia de uso de resíduos orgânicos e apresentar soluções para o " \
             "uso eficiente de fertilizantes em solos altamente intemperizados.</p> "

    st.markdown(text03, unsafe_allow_html=True)
