import streamlit as st
from others.load_css import local_css

# Configuração inicial da página
st.set_page_config(
    page_title="Biochar Data Blog",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.sidebar.image("images/projectLogo.png", use_container_width=True)
st.sidebar.markdown(
    """
    <div style='text-align: center; font-size: 1.2rem; margin-top: 0.5rem;'>
        Developed by<br><a href="https://daniloas.com" target="_blank" style="text-decoration: none;">daniloas.com</a>
    </div>
    """,
    unsafe_allow_html=True
)

def home():

    st.image("images/biochar.png", use_container_width=True)

    st.markdown("<h1 style='text-align: center; line-height: 1.15;'>Biochar Data Blog</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>Insights on biochar for soil improvement and carbon management</p>",
        unsafe_allow_html=True)

    st.markdown("""<hr style="height:1px; border:none; color:#333; background-color:#333;" /> """,
                unsafe_allow_html=True)

    # Sobre o autor
    with st.expander("👨‍🔬 About the Author"):
        st.markdown("""
            <p class="justified-text">
            Hi, I'm <a href="https://daniloas.com" target="_blank"><strong>Danilo Andrade Santos</strong></a>.
            Since 2012, I’ve been researching biochars and their effects on tropical soils, especially in Espírito Santo, Brazil.
            This blog is a space to share insights and data visualizations related to the use of biochar for soil improvement and carbon management.
            </p>
        """, unsafe_allow_html=True)

    # Seção de posts recentes
    st.markdown("### 📰 Latest Blog Posts - Click on the sidebar")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### ☕ Potassium in Coffee Husk Biochar")
        st.markdown("See how potassium levels vary with temperature and biomass source.")
        st.markdown("*Navigate to this post using the sidebar.*")

    with col2:
        st.markdown("#### 🌍 Carbon Addition to Soil")
        st.markdown("Estimate how biochar application can increase soil carbon stocks.")
        st.markdown("*Navigate to this post using the sidebar.*")

    # Rodapé
    st.markdown("""<hr style="height:1px; border:none; color:#333; background-color:#333;" /> """,
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>© 2025 - Danilo Andrade Santos</p>", unsafe_allow_html=True)


# Executar home
if __name__ == "__main__":
    home()
