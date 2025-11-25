import streamlit as st

# Page Configuration
st.set_page_config(page_title="Danilo Andrade Santos", layout="centered", initial_sidebar_state="expanded")

st.sidebar.image("images/projectLogo.png", use_container_width=True)
st.sidebar.markdown(
    """
    <div style='text-align: center; font-size: 1.2rem; margin-top: 0.5rem;'>
        Developed by<br><a href="https://daniloas.com" target="_blank" style="text-decoration: none;">daniloas.com</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Adding Font Awesome for icons and CSS styling
st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <style>
        .perfil-box {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 2px;
            margin-bottom: 30px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
        .icon-link {
            font-size: 18px;
            margin-right: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Section: Developer Profile
st.markdown("""<div class='perfil-box'>""", unsafe_allow_html=True)
st.title("Danilo Andrade Santos")

st.subheader("🔬 Education & Research")
st.markdown(
    """
    - Agronomist  
    - [Biochemistry Professor (UFES - 2022-2024)](https://bioquimicacomdanilo.com.br/)
    - Researcher in Plant Production (M.Sc., D.Sc. - UFES)  
    - [Biochar Specialist (since 2012)](https://biochardatablog.streamlit.app/)
    - [Agroecology Specialist (IFES)](https://agroecossistemas.online/home)  
    - Specializing in Bio-inputs (IFGO)
    - Specializing in Sustainable Agriculture (IFRO)    
    """,
    unsafe_allow_html=True
)

st.subheader("🤖 Technology & Data")
st.markdown(
    """
    - AI Manager  
    - Jr. Web/Mobile Developer  
    - Data Analyst (Python, VBA, R, GIS)  
    - Studying Systems Analysis & Development (UNIP)  
    - Specializing in AI for Agriculture (UTFPR)  
    """
)

st.subheader("🌿 Values & Approach")
st.markdown(
    """
    - Christian  
    - Lifelong Learner  
    - Problem Solver  
    """
)

st.markdown(
    """
    <a class="icon-link" href="https://www.instagram.com/daniloas.com_" target="_blank"><i class="fab fa-instagram"></i> Instagram</a>
    <a class="icon-link" href="https://daniloas.com" target="_blank"><i class="fas fa-globe"></i> Website</a>
    <a class="icon-link" href="https://www.linkedin.com/in/daniloandradesantos/" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>
    <a class="icon-link" href="https://github.com/daniloasdotcom" target="_blank"><i class="fab fa-github"></i> GitHub</a>
    <a class="icon-link" href="mailto:danilo_as@live.com" target="_blank"><i class="fas fa-envelope"></i> Email</a>
    """,
    unsafe_allow_html=True
)
st.markdown("""</div>""", unsafe_allow_html=True)

# Section: Código Agro
st.markdown("""<div class='perfil-box'>""", unsafe_allow_html=True)
st.subheader("🤝 Supported by:")
col1, col2 = st.columns([1, 2])
with col1:
    # Ensure this image path is correct in your project
    st.image("images/codigo_agro.png", use_container_width=True)
with col2:
    st.subheader("Código Agro")
    st.markdown("Technology to transform agriculture.")
    st.markdown(
        """
        <a class="icon-link" href="https://www.instagram.com/codigo.agro/" target="_blank"><i class="fab fa-instagram"></i> Instagram</a>
        """,
        unsafe_allow_html=True
    )
st.markdown("""</div>""", unsafe_allow_html=True)

# Section: Dados Agro
# Added the opening div below to ensure consistency with the other boxes
st.markdown("""<div class='perfil-box'>""", unsafe_allow_html=True) 
col1, col2 = st.columns([1, 2])
with col1:
    # Ensure this image path is correct in your project
    st.image("images/dados_agro.png", use_container_width=True)
with col2:
    st.subheader("Dados Agro")
    st.markdown("Technology, data, and agriculture connected!")
    st.markdown(
        """
        <a class="icon-link" href="https://dadosagro.com" target="_blank"><i class="fas fa-globe"></i> dadosagro.com</a>
        """,
        unsafe_allow_html=True
    )
st.markdown("""</div>""", unsafe_allow_html=True)