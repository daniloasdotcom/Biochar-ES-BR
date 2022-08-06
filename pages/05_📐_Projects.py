import streamlit as st
from PIL import Image
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

# 2. horizontal menu
selected = option_menu(menu_title="Menu de Experimentos",
                       options=["Experimento 01", "Experimento 02"],
                       icons=['house', 'cloud-upload'],
                       menu_icon="cast", default_index=0, orientation="horizontal")


def novo():
    if selected == "Experimento 01":
        col1, col2, col3 = st.columns([1, 6, 1])

        img_biochar02 = Image.open("images/plantioEucalipto.png")

        col2.image(img_biochar02, width=1920, use_column_width=True)

        text01 = "<h1 style='text-align: center; line-height: 1.15'> Monitoring of soil attributes, development and " \
                 "nutritional status of eucalyptus plants in the field, under application of biochars</h1> "

        st.markdown(text01, unsafe_allow_html=True)

        st.write("""
            ###  
            """)

        st.write("""
            ## Abstract
            """)

        text02 = "<p style='text-align: justify;'> In March 2018, a field trial was started using resources from EDITAL " \
                 "FAPES/SEAG Nº 06/2015, in the experimental area of IFES - Campus de Alegre - Brazil. In this assay, " \
                 "eucalyptus bark biochars are tested in treatments distributed in a randomized block design in a 5 x 2 " \
                 "factorial scheme, with five doses of biochars (0; 0.25%; 0.5%; 1.0% and 2 % by volume of biochars by " \
                 "volume of furrow) produced under two temperatures (350 ºc and 600 ºc). The trial is now maintained with " \
                 "resources from Fapes/Cnpq Nº 11/2019 - Regional technological and scientific development program - " \
                 "PDCTR 2019.</p> "

        st.markdown(text02, unsafe_allow_html=True)

    elif selected == "Experimento 02":
        text01 = "<h1 style='text-align: center; line-height: 1.15'>P availability in soil aggregates: effect of " \
                 "pyrolysis temperature and doses of eucalyptus bark biochars</h1> "

        st.markdown(text01, unsafe_allow_html=True)

        st.write("""
            ###  
            """)

        st.write("""
            ## Abstract
            """)

        text02 = "<p style='text-align: justify;'> Degradation of soil structure is one of the main processes for " \
                 "reducing the productive potential of agricultural areas, resulting in a cascading effect on other soil " \
                 "attributes, including negative effects on aggregation, aggregate stability and consequent loss of soil. " \
                 "important macronutrient compartments. Biochars have the potential to positively affect both the " \
                 "aggregation and stability of soil aggregates, as well as the availability of nutrients for plants. " \
                 "Therefore, the present work aims to evaluate the availability of P in soil macro and microaggregates " \
                 "formed from the addition of doses of biochars obtained at two pyrolysis temperatures in samples of a " \
                 "Red-Yellow Latosol. The experiment will be carried out in the laboratory, under a randomized block " \
                 "design in a controlled environment with a temperature of ± 25 ºC for a period of 161 days. The " \
                 "experimental test will be arranged in a 2 x 5 factorial scheme in which the factors under study will " \
                 "be: eucalyptus bark biochars produced from two final temperatures of pyrolysis, 350 ºC and 600 ºC; five " \
                 "doses of biochars, corresponding to 0, 10, 20, 40 and 80 t ha-1; with three replications for each " \
                 "treatment. At the end of the wetting and drying cycles, the experimental plots will be subjected to " \
                 "sieving in a sieve set to obtain different classes of aggregates that will later be gathered into macro " \
                 "and microaggregates. The macro and microaggregates will be subjected to determinations of P extracted " \
                 "from solutions Mehlich-1 (Teixeira et al., 2017), H2O and organic acids (at a concentration of 1 mM); " \
                 "For the evaluation of the effect of the pyrolysis temperature on the P levels obtained, " \
                 "the significance of the F test will be observed. Adjustments of regression models will also be tested " \
                 "as a function of the doses of biochars for each type of biochar.</p> "

        st.markdown(text02, unsafe_allow_html=True)



