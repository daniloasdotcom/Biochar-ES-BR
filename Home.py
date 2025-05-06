import streamlit as st
from others.load_css import local_css
from others.sidebar_utils import configure_sidebar

# Configuração inicial da página
st.set_page_config(
    page_title="Biochar Blog",
    page_icon="🌱",
    layout="centered"
)


def home():
    configure_sidebar()
    local_css("others/style.css")

    st.image("images/biochar.png", use_column_width=True)

    st.markdown("<h1 style='text-align: center; line-height: 1.15;'>Biochar Blog</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>Insights on biochar for soil improvement and carbon management</p>",
        unsafe_allow_html=True)

    st.markdown("""<hr style="height:1px; border:none; color:#333; background-color:#333;" /> """,
                unsafe_allow_html=True)

    # Sobre o autor
    with st.expander("👨‍🔬 About the Author"):
        st.markdown("""
            <p class="justified-text">Hi, I'm <a href="https://daniloas.com" target="_blank"><strong>Danilo Andrade Santos</strong></a>. 
            Since 2012, I’ve been researching biochars and their effects on tropical soils, especially in Espírito Santo, Brazil. 
            Here you’ll find blog posts, experiments, and data visualizations related to the use of biochar as a soil conditioner.</p>
        """, unsafe_allow_html=True)

    # Seção de posts recentes
    st.markdown("## 📰 Latest Blog Posts")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ☕ Potassium in Coffee Husk Biochar")
        st.markdown("See how potassium levels vary with temperature and biomass source.")
        st.markdown("""
            <a href="https://biocharbydanilo.streamlit.app/Coffee_and_potassium" target="_self" style="
                display: inline-block;
                padding: 0.5em 1em;
                background-color: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                margin-top: 10px;
            ">Read Post</a>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 🌍 Carbon Addition to Soil")
        st.markdown("Estimate how biochar application can increase soil carbon stocks.")
        st.markdown("""
            <a href="https://biocharbydanilo.streamlit.app/Carbon" target="_self" style="
                display: inline-block;
                padding: 0.5em 1em;
                background-color: #27ae60;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                margin-top: 10px;
            ">Read Post</a>
        """, unsafe_allow_html=True)

    # Rodapé
    st.markdown("""<hr style="height:1px; border:none; color:#333; background-color:#333;" /> """,
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>© 2025 - Danilo Andrade Santos</p>", unsafe_allow_html=True)


# Executar home
if __name__ == "__main__":
    home()
