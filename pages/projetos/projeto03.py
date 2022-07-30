import streamlit as st
import matplotlib.pyplot as plt
from pages.others.load_css import local_css

# Usando nosso recursos css
local_css("pages/others/style.css")

def Projeto03():
    text01 = "<h1 style='text-align: center; line-height: 1.15'>Movement of nutrients in leach columns under " \
             "different modes of application of biochars</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.write("""
    ###  
    """)

    st.write("""
    ## Abstract
    """)

    text02 = "<p style='text-align: justify;'> Biochar is formed from the pyrolysis of different types of biomass " \
             "residues, under low or absent oxygen concentration and high temperatures. The presence of functional " \
             "groups on the surface of biochars can improve the chemical attributes of the soil, increasing the " \
             "cation exchange capacity and reducing the leaching of nutrients from the soil. However, the effects of " \
             "nutrient movement along the soil profile under application of biochars are still unclear. Thus, " \
             "the present work aims to evaluate the displacement of cationic elements (Ca, Mg, K and Na) in PVC " \
             "columns filled with soil, under application of eucalyptus bark biochar on the surface and incorporated " \
             "into the soil in association with limestone and agricultural gypsum. , when receiving water depths " \
             "exceeding the water retention capacity of the soil. Three tests will be carried out with the objective " \
             "of evaluating three different situations of application of biochars in the soil, each one of them in a " \
             "completely randomized design (DIC) in a controlled environment with a temperature of ± 25 °C in the " \
             "Soil Laboratory of the Agricultural Sciences Center and Engineering at the Federal University of " \
             "Espirito Santo, Campus de Alegre. The three experimental tests will be established in a 2 x 5 factorial " \
             "scheme, in which the factors under study will be: eucalyptus bark biochars produced at two final " \
             "temperatures of pyrolysis, 350 and 600 ºC and five doses of biochar, corresponding to 0.5 , 10, " \
             "15 and 20 t ha-1; with three replications for each treatment. In the first trial, the biochars will be " \
             "applied to the surface; in the second trial, the biochars will be incorporated into a 20 cm layer of " \
             "soil; and in the third trial, the biochars will be incorporated into a 40 cm layer of soil. In all " \
             "tests, biochar doses will be combined with pre-established doses of CaCO3 necessary to reach a soil pH " \
             "equal to 6. The soil layers of the first and second tests, in which they will not undergo the " \
             "incorporation of biochars and CaCO3, will receive doses of CaSO4 as a subsurface soil conditioner. In " \
             "all tests, water depths will also be applied in 5 installments, each application equivalent to a rain " \
             "of 50 mm in an interval of 4 days, totaling 250 mm of water. At the end, the content of elements K, Na, " \
             "Ca and Mg will be evaluated in the leachates and in the soil layers of the leaching columns (0-5, 5-10, " \
             "10-15, 15-20, 20-30 and 30- 40 cm). Data will be subjected to analysis of variance (ANOVA). For the " \
             "evaluation of the effect of pyrolysis temperature on the chemical determinations obtained both in the " \
             "soil and in the leachate, the significance of the F test will be observed. studied soil.</p> "

    st.markdown(text02, unsafe_allow_html=True)