import streamlit as st
import pages.posts.potassium as PostPotassium  # Import the potassium graph
from pages.others.sidebar_utils import configure_sidebar

st.set_page_config(
    page_title="Interactive Blog",
    page_icon="✏️",
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

    # Latest post with subtitle and content
    st.subheader("📅 Latest Post")
    st.markdown("---")
    st.markdown("<h3><em>Coffee Husk Biochar: A Source of K</em></h3>", unsafe_allow_html=True)
    st.write("**Date:** 01/10/2024")
    st.write("""
            Depending on the organic material used to produce biochar, there will also be different amounts of potassium.  
            See how different tons of coffee husk biochar influence the amount of potassium present in each application.
        """)

    # Spacing before the button
    st.markdown("<br>", unsafe_allow_html=True)

    # Button to view the full potassium graph
    if st.button("🔍 View full post"):
        st.session_state['page'] = 'grafico'  # Change the page state to 'grafico'

    # Separator between posts (if there are more posts in the future)
    st.markdown("---")

# Function for the potassium graph
def potassium_graph():
    PostPotassium.potassium_graph()

# Main function to control navigation
def main():
    # Initialize session if not set
    if 'page' not in st.session_state:
        st.session_state['page'] = 'blog'  # The initial page is the blog

    # Check which page to display based on the state
    if st.session_state['page'] == 'blog':
        blog()  # Show the blog
    elif st.session_state['page'] == 'grafico':
        potassium_graph()  # Show the potassium graph

# Run the app
if __name__ == "__main__":
    main()
