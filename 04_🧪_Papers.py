import base64
import streamlit as st
from pages.others.load_css import local_css

# Usando nosso recursos css
local_css("pages/others/style.css")

st.sidebar.image("images/projectLogo.png", use_column_width=True)

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('**General coordinator**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
st.sidebar.markdown('**Regional Researcher**: [Danilo Andrade](https://daniloas.com/)')

st.sidebar.write("##")
st.sidebar.write("##")

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="600" height="600" ' \
                  f'type="application/pdf" ></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def papers():
    text01 = "<h1 style='text-align: center; line-height: 1.15'>Publications produced during the duration of the " \
             "project</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.write("""# Books Chapters""")

    # primeiro paper
    with st.container():
        text02 = "<p style='text-align: justify;'> SILVA, C. C.; SANTOS, D. A.; SILVA, A. G.; PASSOS, R. R.; RANGEL, " \
                 "O. J. P.; SILVA, M. E. P. B.; PROFETI, D.; PROFETI, L. P. R. Biocarvões e disponibilidade de " \
                 "fósforo para a produção vegetal. In: COSTA, A. V.; PARREIRA, L. A.;  PROFETI, L. P. R.; Campos, O. S." \
                 " (Org.). <strong>Tópicos Especiais em Agroquímica I</strong>. 1 ed. Vitória: UFES, 2021, v. I, " \
                 "p. 51-68. </p> "

        st.markdown(text02, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Read PDF', key='1'):
            show_pdf('files/Silva_et_al_2021.pdf')
    with col2:
        st.button('Close PDF', key='2')
    with col3:
        with open("files/Silva_et_al_2021.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF", key='3',
                           data=PDFbyte,
                           file_name="Silva_et_al_2021.pdf",
                           mime='application/octet-stream')

    # Segundo paper
    with st.container():
        text03 = "<p style='text-align: justify;'> PASSOS, R.R.; SANTOS, D. A.; SARTORI, A. F.; ZACARIAS, A. J.; SILVA, " \
                 "C. C.; RANGEL, O. J. P.; MOSA, L. L.; PROFETI, D.; PROFETI, L. P. R.; SILVA, R. W. Biocarvão de " \
                 "casca de eucalipto efeito sobre atributos químicos de um latossolo vermelho-amarelo cultivado com " \
                 "<i>Eucaliptus urograndis</i>. In: Fabricio Gomes Gonçalves; Marcos Vinicius Winckler Caldeira; Gilson " \
                 "Fernandes da Silva; Gustavo Soares de Souza. (Org.). <strong>Sistemas Integrados de Produção pesquisa " \
                 "e " \
                 "desenvolvimento de tecnologias</strong>. 1ed.Guarujá - SP: Editora Científica Digital, 2021, v. I, " \
                 "p. 87-105. " \
                 "https://doi.org/10.37885/210605169 </p> "

        st.markdown(text03, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Read PDF', key='4'):
            show_pdf('files/Passos_et_al_2021b.pdf')
    with col2:
        st.button('Close PDF', key='5')
    with col3:
        with open("files/Passos_et_al_2021b.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF", key='6',
                           data=PDFbyte,
                           file_name="Passos_et_al_2021b.pdf",
                           mime='application/octet-stream')

    # Terceiro paper
    with st.container():
        text03 = "PASSOS, R. R. ; SANTOS, D. A. ; SARTORI, A. F. ; ZACARIAS, A. J. ; MENDONCA, I. W. ; RANGEL, " \
                 "O. J. P. ; MOSA, L. L. ; PROFETI, D. ; PROFETI, L. P. R. ; SILVA, R. W. . Carbono orgânico e " \
                 "atributos físicos de um latossolo vermelho-amarelo sob aplicação de biocarvão cultivado com " \
                 "Eucalyptus Urograndis. In: Fabricio Gomes Gonçalves; Marcos Vinicius Winckler Caldeira; Gilson " \
                 "Fernandes da Silva; Gustavo Soares de Souza. (Org.). Sistemas Integrados de Produção pesquisa e " \
                 "desenvolvimento de tecnologias. 1ed.Guarujá - SP: Editora Científica Digital, 2021, v. I, " \
                 "p. 106-127. </p> "

        st.markdown(text03, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Read PDF', key='7'):
            show_pdf('files/Passos_et_al_2021a.pdf')
    with col2:
        st.button('Close PDF', key='8')
    with col3:
        with open("files/Passos_et_al_2021a.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF", key='9',
                           data=PDFbyte,
                           file_name="Passos_et_al_2021a.pdf",
                           mime='application/octet-stream')

    # Quarto paper
    with st.container():
        text05 = "<p style='text-align: justify;'> SANTOS, D. A.; SILVA, A. G. ; PASSOS, R. R. ; RANGEL, O. J. P. . " \
                 "Agregados do solo e dinâmica do P: uma relação ainda pouco compreendida. In: Rangel, O. J. P.; Berilli, " \
                 "A. P. C. G.; Oliveira, A. de F. M. de; Alves, D. I.; Alves, J. de A.; Ferrari, J. L.;  Novaes, " \
                 "M. S.; Moulin, M. M.; Mendonça, P. P. (Org.). <strong>Tópicos em Agroecologia - Volume III.</strong> 1 ed. Vitória: " \
                 "Edifes, 2022, v. III, p. 336-349. </p> "

        st.markdown(text05, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Read PDF', key='10'):
            show_pdf('files/Santos_et_al_2022.pdf')
    with col2:
        st.button('Close PDF', key='11')
    with col3:
        with open("files/Santos_et_al_2022.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF", key='12',
                           data=PDFbyte,
                           file_name="Santos_et_al_2022.pdf",
                           mime='application/octet-stream')

    st.write("""# Papers""")
    # Quarto paper
    with st.container():
        text06 = "<p style='text-align: justify;'> FONSECA, A. A.; SANTOS, D. A.; MOURA JUNIOR, C.D.; PASSOS, " \
                 "R. R.; RANGEL, O.J.P. Phosphorus and potassium in aggregates of degraded soils: changes caused by " \
                 "biochar application. <strong>CLEAN</strong> (WEINHEIM. INTERNET), p. 2000366, 2021. </p> "

        st.markdown(text06, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Read PDF', key='13'):
            show_pdf('files/paper01.pdf')
    with col2:
        st.button('Close PDF', key='14')
    with col3:
        with open("files/paper01.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF", key='15',
                           data=PDFbyte,
                           file_name="paper01.pdf",
                           mime='application/octet-stream')

    # Quinto paper
    with st.container():
        text07 = "<p style='text-align: justify;'> FONSECA, A. A.; SANTOS, D. A.; PASSOS, R. R.; ANDRADE, F. V.; RANGEL, " \
                 "O. J. P. Phosphorus availability and grass growth in biochar-modified acid soil: A study excluding the " \
                 "effects of soil pH. <strong>Soil Use and Management</strong>. v. 36, p. 714-714, 2020. </p> "

        st.markdown(text07, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Read PDF', key='16'):
            show_pdf('files/paper02.pdf')
    with col2:
        st.button('Close PDF', key='17')
    with col3:
        with open("files/paper02.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF", key='18',
                           data=PDFbyte,
                           file_name="paper02.pdf",
                           mime='application/octet-stream')

    st.write("""# Theses and dissertations""")

    # Sexto paper
    with st.container():
        text08 = "<p style='text-align: justify;'> SILVA, Ronaldo Willian da. Dinâmica de fósforo e eficiência " \
                 "agronômica de superfosfato triplo associado a biocarvões. 2021. Tese (Doutorado em Doutorado em " \
                 "Produção Vegetal) - Universidade Federal do Espírito Santo, Alegre, 2021. </p> "

        st.markdown(text08, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Read PDF', key='19'):
            show_pdf('files/Tese_Ronaldo_2021.pdf')
    with col2:
        st.button('Close PDF', key='20')
    with col3:
        with open("files/Tese_Ronaldo_2021.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF", key='21',
                           data=PDFbyte,
                           file_name="Tese_Ronaldo_2021.pdf",
                           mime='application/octet-stream')

    st.write("""# Resumes""")
    # Primeiro Resumo
    with st.container():
        text09 = "<p style='text-align: justify;'>Caracterização de biocarvões, estudo de sua interação com o ânion " \
                 "P e disponibilidade de P no solo. In: Anais de Iniciação Científica da UFES, 2020. Anais [...] " \
                 "Vitória: UFES. 2020.</p> "

        st.markdown(text09, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Read PDF', key='23'):
            show_pdf('files/IC_Mateus_2020.pdf')
    with col2:
        st.button('Close PDF', key='24')
    with col3:
        with open("files/IC_Mateus_2020.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF", key='25',
                           data=PDFbyte,
                           file_name="IC_Mateus_2020.pdf",
                           mime='application/octet-stream')

    # Segundo Resumo
    with st.container():
        text09 = "<p style='text-align: justify;'>Produção de fertilizante organomineral fosfatado de eficiência " \
                 "aumentada baseado em biocarvão. In: Anais de Iniciação Científica da UFES, 2021. Anais [...] " \
                 "Vitória: UFES. 2021.</p> "

        st.markdown(text09, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Read PDF', key='26'):
            show_pdf('files/IC_Mateus_2021.pdf')
    with col2:
        st.button('Close PDF', key='27')
    with col3:
        with open("files/IC_Mateus_2021.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF", key='28',
                           data=PDFbyte,
                           file_name="IC_Mateus_2021.pdf",
                           mime='application/octet-stream')

papers()
