import streamlit as st
import pages.Coffee_and_potassium as PostPotassium  # Import the potassium graph
import pages.carbon as PostCarbon  # Import the carbon addition graph
from others.sidebar_utils import configure_sidebar

st.set_page_config(
    page_title="Interactive Blog",
    page_icon="🌱",
    layout="centered"
)


# Blog function
def blog():
    configure_sidebar()  # Calls the function to configure the sidebar

    # Blog title and welcome message
    st.title("🌿 Interactive Biochar Blog")
    st.header("Welcome to Our Research Blog!")

    # Initial description
    st.write("""
            Explore our posts to understand how biochars can impact agricultural systems.
            Our interactive graphs provide a dynamic view of the effects of biochars.
        """)

    # Latest posts
    st.subheader("📅 Latest Posts")
    st.markdown("---")

    # Second post
    st.markdown("<h3><em>Biochar and Carbon Addition to Soil</em></h3>", unsafe_allow_html=True)
    st.write("**Date:** 26/11/2024")
    st.write("""
                Learn how biochar application can increase soil carbon levels, contributing to carbon sequestration 
                and improving soil health.
            """)
    if st.button("🔍 View Carbon Post"):
        st.session_state['page'] = 'grafico_carbon'  # Navigate to carbon graph page
    st.markdown("---")

    # First post
    st.markdown("<h3><em>Coffee Husk Biochar: A Source of K</em></h3>", unsafe_allow_html=True)
    st.write("**Date:** 01/10/2024")
    st.write("""
            Depending on the organic material used to produce biochar, there will also be different amounts of potassium.  
            See how different tons of coffee husk biochar influence the amount of potassium present in each application.
        """)
    if st.button("🔍 View Potassium Post"):
        st.session_state['page'] = 'grafico_potassium'  # Navigate to potassium graph page
    st.markdown("---")

# Function for the potassium graph
def potassium_graph():
    PostPotassium.potassium_graph()


# Function for the carbon graph
def carbon_graph():
    PostCarbon.carbon_dashboard()


# Main function to control navigation
def main():
    # Initialize session state if not set
    if 'page' not in st.session_state:
        st.session_state['page'] = 'blog'  # Default page is the blog

    # Display the appropriate page based on session state
    if st.session_state['page'] == 'blog':
        blog()  # Show the blog
    elif st.session_state['page'] == 'grafico_potassium':
        potassium_graph()  # Show the potassium graph
    elif st.session_state['page'] == 'grafico_carbon':
        carbon_graph()  # Show the carbon graph


# Run the app
if __name__ == "__main__":
    main()
