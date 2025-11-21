import streamlit as st
from utils import show_sidebar

# ---------------------------------------------------------
# ------------------- PAGE CONFIGURATION ------------------
# ---------------------------------------------------------
st.set_page_config(
    page_title="Biochar Data Blog",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# ------------------ CALL SIDEBAR MODULE ------------------
# ---------------------------------------------------------
show_sidebar()

# ---------------------------------------------------------
# --------------------- HOME FUNCTION ---------------------
# ---------------------------------------------------------
def home():
    # --- Banner Image ---
    try:
        st.image("images/biochar.png", use_container_width=True)
    except:
        st.warning("Note: 'images/biochar.png' was not found.")

    # --- Header ---
    st.markdown("<h1 style='text-align: center; line-height: 1.15;'>Biochar Data Blog</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 18px; color: #666;'>Insights on biochar for soil improvement and carbon management</p>",
        unsafe_allow_html=True)

    st.markdown("""<hr style="height:1px; border:none; color:#e0e0e0; background-color:#e0e0e0;" /> """,
                unsafe_allow_html=True)

    # --- About the Author ---
    with st.expander("👨‍🔬 About the Author"):
        st.markdown("""
            <div style="text-align: justify;">
            Hi, I'm <a href="https://daniloas.com" target="_blank"><strong>Danilo Andrade Santos</strong></a>.
            Since 2012, I’ve been researching biochars and their effects on tropical soils.
            This blog is a space to share insights and data visualizations related to the use of biochar.
            </div>
        """, unsafe_allow_html=True)

    # --- BLOG POSTS SECTION ---
    st.markdown("### 📰 Latest Blog Posts")

    col1, col2 = st.columns(2)

    # --- CARD 1: Coffee & Potassium ---
    with col1:
        with st.container(border=True):
            # 1. TITLE (Fixed Height ~ 60px to allow 2 lines)
            st.markdown("""
                <div style="min-height: 60px; font-weight: 600; font-size: 1.5rem; line-height: 1.2;">
                    ☕ Coffee & Potassium
                </div>
                """, unsafe_allow_html=True)
            
            st.caption("Experimental Data Analysis")
            
            # 2. DESCRIPTION (Fixed Height ~ 100px to allow 3-4 lines)
            st.markdown("""
                <div style="min-height: 100px; text-align: justify;">
                    See how potassium levels vary with temperature and biomass source. 
                    We analyze different pyrolysis conditions.
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            st.page_link("pages/1_📝_Coffee_and_potassium.py", label="Read Analysis", icon="📊", use_container_width=True)

    # --- CARD 2: Soil Carbon ---
    with col2:
        with st.container(border=True):
            # 1. TITLE (Fixed Height ~ 60px)
            # Even if text is short, it occupies the space of 2 lines
            st.markdown("""
                <div style="min-height: 60px; font-weight: 600; font-size: 1.5rem; line-height: 1.2;">
                    🌍 Soil Carbon
                </div>
                """, unsafe_allow_html=True)
            
            st.caption("Simulation Tool")
            
            # 2. DESCRIPTION (Fixed Height ~ 100px)
            st.markdown("""
                <div style="min-height: 100px; text-align: justify;">
                    Estimate how biochar application can increase soil carbon stocks 
                    based on different soil densities and application rates.
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            st.page_link("pages/2_📝_Carbon_in_Soil.py", label="Open Simulator", icon="🚀", use_container_width=True)

    # --- Footer ---
    st.markdown("""<hr style="height:1px; border:none; color:#e0e0e0; background-color:#e0e0e0; margin-top: 50px;" /> """,
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #999; font-size: 12px;'>© 2025 - Danilo Andrade Santos</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    home()