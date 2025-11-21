# utils.py
import streamlit as st

def show_sidebar():
    # Sidebar Content
    st.sidebar.image("images/projectLogo.png", width=200)
    
    # The Footer
    st.sidebar.markdown(
        """
        <div style='text-align: center; font-size: 1.0rem; color: #666;'>
            Developed by<br>
            <a href="https://daniloas.com" target="_blank" style="text-decoration: none; color: #4A90E2; font-weight: bold;">
                daniloas.com
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )