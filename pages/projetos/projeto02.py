import streamlit as st
from pages.others.load_css import local_css

# Usando nosso recursos css
local_css("pages/others/style.css")

def Projeto02():
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

