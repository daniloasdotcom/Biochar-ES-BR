import streamlit as st

def publica():
    text01 = "<h1 style='text-align: center; line-height: 1.15'>Publications in production</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.write("""
    ## Book chapters
    """)

    text02 = "<p style='text-align: justify;'> Effects of biochars on soil aggregation</p> "

    st.markdown(text02, unsafe_allow_html=True)

    text03 = "<p style='text-align: justify;'> Biochar functionalization </p> "

    st.markdown(text03, unsafe_allow_html=True)

    text04 = "<p style='text-align: justify;'>The relationship between microorganism and soil phosphorus</p> "

    st.markdown(text04, unsafe_allow_html=True)

    text05 = "<p style='text-align: justify;'>Methods of chemical characterization of biochars</p> "

    st.markdown(text05, unsafe_allow_html=True)

    st.write("""
        ## Artigos
        """)

    text06 = "<p style='text-align: justify;'> Biochar: Soil Aggregation from Degraded Pastures </p> "

    st.markdown(text06, unsafe_allow_html=True)