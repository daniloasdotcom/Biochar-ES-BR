import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="Biochar Dispersion Tracker",
    page_icon="🌱",
    layout="centered"
)

st.sidebar.markdown(
    """
    <div style='text-align: center; font-size: 1.2rem; margin-top: 0.5rem;'>
        Developed by<br><a href="https://daniloas.com" target="_blank" style="text-decoration: none;">daniloas.com</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Make sure you have this image in your folder, or comment this line out if not
st.sidebar.image("images/projectLogo.png", use_container_width=True)

# --- CSS for Styling (Justified text and Cards) ---
st.markdown("""
<style>
    /* Justify general text */
    .stMarkdown p, .stExpander p, .stMarkdown li {
        text-align: justify;
    }
    /* Style for Study Cards */
    div.study-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #ff4b4b; /* Streamlit Red */
        border-right: 1px solid #e0e0e0;
        border-top: 1px solid #e0e0e0;
        border-bottom: 1px solid #e0e0e0;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .study-title {
        font-weight: bold;
        font-size: 1.0em;
        margin-bottom: 2px;
        color: #0e1117;
    }
    .study-location {
        font-size: 0.8em;
        color: #666;
        margin-bottom: 8px;
        font-style: italic;
    }
    .study-metric {
        font-size: 1.4em;
        font-weight: 800;
        color: #d63031;
        margin-bottom: 0px;
    }
    .study-time {
        font-size: 0.85em;
        color: #444;
        font-weight: 500;
        margin-bottom: 8px;
    }
    .study-detail {
        font-size: 0.85em;
        color: #333;
        margin-top: 4px;
        line-height: 1.3;
    }
    .highlight-soil {
        background-color: #e8f4f9;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.85em;
        color: #005f73;
    }
    .highlight-climate {
        background-color: #f0fff4;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 0.85em;
        color: #2d6a4f;
        border: 1px solid #c6f6d5;
    }
    hr {
        margin: 8px 0 !important;
        border-top: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# --- Title and Header ---
st.title("🌱 Biochar Persistence in Soil")

# --- Introduction ---
st.markdown("""
Relying on the chemical properties of biochar to ensure its permanence in the soil can be misleading. Studies show that even highly stable materials can migrate or be "lost" from the soil due to erosion and vertical movement.

Such effects, especially losses due to erosion, must be considered in biochar projects—whether for agronomic improvement or atmospheric carbon removal projects—so that appropriate management strategies can be developed.
""")

st.subheader("📉 Evidence of Long-Term Loss")

st.markdown("""
Let us first examine data evidencing vertical movement. **Ding et al. (2023)** and **Gross et al. (2024)**, for example, report significant reductions in Carbon stocks derived from biochars, quantifying vertical movements, especially in soils with lower clay content.
""")

st.markdown("Summary of referenced field experiments:")

# --- CARD LAYOUT ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="study-card">
        <div>
            <div class="study-title">Ding et al. (2023)</div>
            <div class="study-location">📍 Shangzhuang, China</div>
            <div class="study-metric">~49–61% not recovered</div>
            <div class="study-time">after 11 Years</div>
            <span class="highlight-climate">Continental Monsoon (400 mm/yr)</span>
            <hr>
            <div class="study-detail">
                <span class="highlight-soil">Calcareous Soil (Silt Loam)</span><br>
                <small>28% Sand, 52% Silt, 20% Clay</small>
            </div>
            <div class="study-detail">
                <b>Dose:</b> 30, 60 & 90 Mg/ha or 15, 30 & 45 g/dm³<br>
                <b>Incorp.:</b> 0–20 cm<br>
                <b>Biochar:</b> Rice husk + cotton (400°C)<br>
                <b>Cause:</b> Vertical redistribution, possible transport below 30 cm and/or mineralization; lateral losses not assessed.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="study-card">
        <div>
            <div class="study-title">Gross et al. (2024) [I]</div>
            <div class="study-location">📍 Bayreuth, Germany</div>
            <div class="study-metric">~19% not recovered</div>
            <div class="study-time">after 11 Years</div>
            <span class="highlight-climate">Temperate Oceanic</span>
            <hr>
            <div class="study-detail">
                <span class="highlight-soil">Sandy Clay Loam</span><br>
                <small>62% Sand, 26% Clay</small>
            </div>
            <div class="study-detail">
                <b>Dose:</b> 31.5 Mg/ha or 31.5 g/dm³<br>
                <b>Incorp.:</b> 0–10 cm<br>
                <b>Biochar:</b> Wood (≈550°C)<br>
                <b>Cause:</b> Strong vertical redistribution (0–10 → 10–30 cm); lateral movement not measured.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="study-card">
        <div>
            <div class="study-title">Gross et al. (2024) [II]</div>
            <div class="study-location">📍 Gartow, Germany</div>
            <div class="study-metric">~56% not recovered</div>
            <div class="study-time">after 9 Years</div>
            <span class="highlight-climate">Temperate Oceanic</span>
            <hr>
            <div class="study-detail">
                <span class="highlight-soil">Sandy Soil</span><br>
                <small>94% Sand, 2% Clay</small>
            </div>
            <div class="study-detail">
                <b>Dose:</b> 40 Mg/ha or 26.7 g/dm³<br>
                <b>Incorp.:</b> 0–15 cm<br>
                <b>Biochar:</b> Wood (≈650°C)<br>
                <b>Cause:</b> Intense vertical redistribution and low physical protection in sandy soil; lateral losses not quantified.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("""

""")
st.markdown("""
As observed, **Ding et al. (2023)** and **Gross et al. (2024)** did not quantify lateral movement. Furthermore, do particle size or applied dose influence this movement?
""")

# --- Transition to Obia et al. ---
st.markdown("""
The work by **Obia et al. (2024)** brings important insights into this issue. They deepened this investigation by focusing on transport physics. The following data is an extract of observations by **Obia et al. (2024)** in sandy loam soil (75% sand) cultivated with maize, testing the effect of particle size and dose.*

Let's observe:
""")

st.divider()

# --- Experimental Context ---
st.header("📍 Experimental Context")

with st.expander("📋 View full details on Soil, Management, and Climate", expanded=False):
    st.markdown("""
    * **The Biochar:** Dry corncob in a retort kiln at a temperature of approximately 400 to 500˚C with a residence time of 24 hrs.
    * **Application Depth:** 0-7 cm.
    * **The Soil (Critical Factor):** Classified as **Acrisol (FAO)**, **Sandy Loam** texture.
        * **Granulometric Composition:** 75.1% Sand, 15.9% Silt, 9.0% Clay.
        * **Chemistry:** Acidic soil (pH 5.8) and poor in Organic Carbon (0.74%).
        * *Impact:* The high percentage of sand and low amount of clay limit physical aggregation, facilitating vertical migration of fine particles and surface erosion.
    * **Rainfall Regime:** Humid subtropical climate with an average of **1220 mm/year**. Rains are concentrated in the hot season, creating intense precipitation events that favor lateral transport.
    * **Management and Fertilization:**
        * Annual maize cultivation with fertilization (NPK + Urea) in all seasons.
        * **Tillage:** The soil was manually turned (hoe) up to **30 cm** for initial incorporation. Annual planting involved recurrent surface tillage.
    """)

st.divider()

# --- Controls ---
st.subheader("⚙️ Scenario Settings")

biochar_size = st.radio(
    "Choose Biochar Particle Size:",
    ["Fine (<0.5 mm)", "Medium (0.5-1 mm)", "Coarse (1-5 mm)"],
    index=0,
    horizontal=True 
)

# --- Data Logic (Obia et al.) ---
def get_data_profile(size, dosage_type):
    if "Fine" in size:
        if "Low" in dosage_type: # BC2
            profile = [41.2, 5.8, 2.3, 1.6, 1.6, 1.5, 5.9, 6.1, 0.5]
            expl = "<b>High vertical migration:</b> Fine particles in low dose descend easily (sieving effect). ~25% migrated vertically."
        else: # BC4
            profile = [33.3, 1.0, 0.5, 0.3, 0.2, 0.1, 0.9, 0.6, 0.3]
            expl = "<b>Clogging Effect:</b> High dose clogged pores, reducing vertical migration (~4%), but increasing surface loss."
    elif "Medium" in size:
        if "Low" in dosage_type: # BC1.5
            profile = [35.9, 2.6, 1.8, 1.2, 0.6, 0.8, 3.3, 3.4, 1.0]
            expl = "<b>Mixed Behavior:</b> Total recovery of ~50%. Moderate migration (~15%) and high erosion."
        else: # BC3
            profile = [25.2, 0.8, 0.5, 0.3, 0.2, 0.1, 1.5, 2.5, 0.5]
            expl = "<b>Critical Scenario:</b> Only ~25% retained. Combination of size and dose facilitated extreme lateral erosion (>60% loss)."
    else: # Coarse
        if "Low" in dosage_type: # BC2
            profile = [61.9, 1.8, 0.6, 0.2, 0.2, 0.1, 1.1, 0.6, 0.2]
            expl = "<b>Higher Stability:</b> Coarse/Low dose had higher surface retention (~62%) and insignificant migration."
        else: # BC4
            profile = [40.8, 1.2, 0.8, 0.4, 0.2, 0.1, 1.2, 2.9, 1.0]
            expl = "<b>Inverse Dose Effect:</b> High dose created macropores, allowing slight migration, but erosion dominated."

    return profile, expl

def process_metrics(profile):
    top = profile[0]
    vert = sum(profile[1:])
    loss = max(0, 100 - (top + vert))
    return top, vert, loss

# Get Obia Data
prof_low, expl_low = get_data_profile(biochar_size, "Low")
top_low, vert_low, loss_low = process_metrics(prof_low)

prof_high, expl_high = get_data_profile(biochar_size, "High")
top_high, vert_high, loss_high = process_metrics(prof_high)

# --- Dashboard Layout (Charts) ---

# 1. Mass Balance
st.header("1. Mass Balance")
st.markdown("Comparison between Doses:")

col1, col2 = st.columns(2)
labels_pie = ['Retained (0-7cm)', 'Vertical Migration (7-30cm)', 'Loss (Erosion/Min.)']
colors_pie = ['#3498db', '#f1c40f', '#8c564b']

with col1:
    st.subheader("Low Dose (1.5-2%)")
    st.subheader("(19-25.3 g/dm³)")
    fig_pie_low = go.Figure(data=[go.Pie(
        labels=labels_pie, values=[top_low, vert_low, loss_low], hole=.4,
        marker=dict(colors=colors_pie), textinfo='percent', textposition='inside',
        insidetextfont=dict(size=14), sort=False, pull=[0, 0, 0.1]
    )])
    fig_pie_low.update_layout(legend=dict(orientation="h", y=-0.1), margin=dict(t=20, b=20, l=10, r=10))
    st.plotly_chart(fig_pie_low, use_container_width=True)
    st.info(expl_low, icon="ℹ️")

with col2:
    st.subheader("High Dose (3-4%)")
    st.subheader("(37.9-50.4 g/dm³)")
    fig_pie_high = go.Figure(data=[go.Pie(
        labels=labels_pie, values=[top_high, vert_high, loss_high], hole=.4,
        marker=dict(colors=colors_pie), textinfo='percent', textposition='inside',
        insidetextfont=dict(size=14), sort=False, pull=[0, 0, 0.1]
    )])
    fig_pie_high.update_layout(legend=dict(orientation="h", y=-0.1), margin=dict(t=20, b=20, l=10, r=10))
    st.plotly_chart(fig_pie_high, use_container_width=True)
    st.info(expl_high, icon="ℹ️")

st.divider()

# 2. Vertical Migration
st.header("2. Depth Profile Detail")
st.markdown("Distribution of remaining biochar across soil layers:")

col3, col4 = st.columns(2)
global_max_x = max(max(prof_low), max(prof_high)) * 1.15 
layers_label = ["0-7 cm", "7-8 cm", "8-9 cm", "9-10 cm", "10-11 cm", "11-12 cm", "12-17 cm", "17-25 cm", "25-30 cm"]
color_map_bar = {"Retained (0-7cm)": "#3498db", "Vertical Migration": "#f1c40f"}

def create_bar_chart(profile, max_x_range):
    colors_bar = ["Retained (0-7cm)"] + ["Vertical Migration"] * (len(profile)-1)
    df = pd.DataFrame({"Layer": layers_label, "Recovery (%)": profile, "Category": colors_bar})
    
    fig = px.bar(df, x='Recovery (%)', y='Layer', color='Category', orientation='h', 
                 text_auto='.1f', color_discrete_map=color_map_bar)
    
    fig.update_yaxes(autorange="reversed", tickfont=dict(color="black"))
    fig.update_xaxes(
        range=[0, max_x_range], showline=True, linewidth=1, linecolor='black',
        tickfont=dict(color="black"), title_font=dict(color="black")
    )
    fig.update_layout(showlegend=False, xaxis_title="Recovery (%)", margin=dict(t=10))
    return fig

with col3:
    st.markdown("**Profile - Low Dose**")
    st.plotly_chart(create_bar_chart(prof_low, global_max_x), use_container_width=True)

with col4:
    st.markdown("**Profile - High Dose**")
    st.plotly_chart(create_bar_chart(prof_high, global_max_x), use_container_width=True)

st.divider()

# --- CONCLUSION ---
st.subheader("🚨 Implications for Soil Management and Carbon Markets")

st.markdown("""
The presented data highlights a structural risk: from an agronomic point of view, it is desirable for biochar to remain in the soil to express its positive effects on agricultural production; however, regarding its function as an atmospheric carbon sink, **carbon credit accounting based solely on "application" proves insufficient and risky.** For both perspectives, if the observed losses are the result of **lateral movement (erosion)**, the fundamental premise that biochar remains in the soil is broken. This migration does not only represent an accounting failure in the carbon market; it represents a loss of inputs and introduces the risk of carrying the material into watercourses or adjacent ecosystems.

To ensure that biochars can successfully fulfill their functions, some practical recommendations are essential:

1.  **Monitoring Physical Stability:** It is not enough to measure chemical stability (H/C ratio); it is imperative to monitor the physical permanence of the material on-site (erosion risk).
2.  **Mandatory Conservation Management:** Eligibility for credits must be conditioned on the adoption of practices that mitigate erosion (such as no-till farming, contour farming, and soil cover), creating redundancy in storage security.
3.  **Application and Incorporation Method:** Surface applications without proper incorporation represent a high risk of material "flight". **It is fundamental to incorporate the biochar into the soil matrix** (via mechanical or biological means) to reduce its direct exposure to erosive agents (water and wind) and increase its residence time.
""")

st.divider()

# --- References ---
st.markdown("### 📚 References")
st.markdown("""
> Obia A, Lyu J, Mulder J, Martinsen V, Cornelissen G, Smebye AB, et al. (2024) **Biochar dispersion in a tropical soil and its effects on native soil organic carbon.** PLoS ONE 19(4): e0300387.

> Ding X, Li G, Zhao X, Lin Q, Wang X (2023) **Biochar application significantly increases soil organic carbon under conservation tillage: an 11-year field experiment.** Biochar 5:28.

> Gross A, Bromm T, Polifka S, Fischer D, Glaser B (2024) **Long-term biochar and soil organic carbon stability - Evidence from field experiments in Germany.** Science of The Total Environment 954:176340.
""")