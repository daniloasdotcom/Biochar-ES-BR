import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page Configuration
st.set_page_config(
    page_title="Biochar Charges",
    page_icon="⚡",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .highlight {
        background-color: #e8f5e9;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        font-weight: 600;
        color: #1b5e20;
    }
    .citation {
        font-size: 0.9rem;
        color: #555;
        border-left: 4px solid #4CAF50;
        background-color: #f9f9f9;
        padding: 10px;
        margin-top: 5px;
        border-radius: 0 5px 5px 0;
    }
    .nuance-box {
        background-color: #fff3e0;
        border: 1px solid #ffe0b2;
        padding: 15px;
        border-radius: 5px;
        margin-top: 15px;
    }
    .ph-box {
        background-color: #e3f2fd;
        border: 1px solid #90caf9;
        padding: 15px;
        border-radius: 5px;
        margin-top: 15px;
    }
    .mystery-box {
        background-color: #f3e5f5;
        border: 1px solid #ce93d8;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .temp-box {
        background-color: #ffebee;
        border: 1px solid #ef9a9a;
        padding: 15px;
        border-radius: 5px;
        margin-top: 15px;
    }
    .soil-box {
        background-color: #e8f5e9;
        border: 1px solid #a5d6a7;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title('⚡ The Positive Side of Biochar')

# --- Theoretical Introduction ---
st.markdown("### 🔍 The Origin of Charge (Natural Biochar)")

texto_intro = """

The positive charges of non-oxidized biochars originate from <span class='highlight'>oxonium functional groups (oxygen heterocycles)</span> 
and, to a lesser extent, pyridinium structures. They play a fundamental role in <span class='highlight'>anion retention (such as nitrate and phosphate)</span>, 
in addition to contributing (like CEC) to the wettability (hydrophilicity) of biochars.

These groups are typically associated with **high pyrolysis temperatures** (≥700°C), where the aromatic structure is condensed.
"""
st.markdown(texto_intro, unsafe_allow_html=True)

# --- New Section: Banik 2018 and Temperature ---
st.write("---")
st.markdown("### 🔥 The Temperature Effect (Banik et al., 2018)")

st.write("""
To understand nature's "choice" between positive or negative charge, **Banik et al. (2018)** produced *Corn Stover* biochars at various temperatures.

The result shows a clear Trade-off:
""")

col_temp1, col_temp2 = st.columns(2)

with col_temp1:
    st.markdown("""
    <div class='temp-box'>
    <b>⬇️ CEC (Negative) Drops:</b><br>
    Acidic functional groups (like carboxyls) are volatile. They are "burned" and lost as the temperature rises.
    </div>
    """, unsafe_allow_html=True)

with col_temp2:
    st.markdown("""
    <div class='temp-box'>
    <b>⬆️ AEC (Positive) Rises:</b><br>
    The carbon structure condenses (aromatization). Stable Oxonium groups and graphitic structures form, holding the positive charge.
    </div>
    """, unsafe_allow_html=True)

# --- pH Selector for Banik ---
st.write("#### 🧪 Choose Chemical Environment (pH):")
ph_opcao = st.radio(
    "At which pH do you want to visualize the charges?",
    options=[5, 8, 10],
    format_func=lambda x: f"pH {x} ({'Acidic' if x==5 else 'Neutral' if x==8 else 'Alkaline'})",
    horizontal=True
)

# Full Data Banik 2018 (Table 1 - Corn Stover)
# Structured for easy filtering
dados_banik_full = [
    # pH 5
    {'Temperature': 400, 'pH': 5, 'CEC': 8.0, 'AEC': 1.0},
    {'Temperature': 500, 'pH': 5, 'CEC': 5.4, 'AEC': 4.0},
    {'Temperature': 600, 'pH': 5, 'CEC': 5.3, 'AEC': 6.8},
    {'Temperature': 700, 'pH': 5, 'CEC': 3.0, 'AEC': 13.7},
    {'Temperature': 900, 'pH': 5, 'CEC': 3.7, 'AEC': 13.6},
    # pH 8
    {'Temperature': 400, 'pH': 8, 'CEC': 23.9, 'AEC': 0.1},
    {'Temperature': 500, 'pH': 8, 'CEC': 20.1, 'AEC': 1.5},
    {'Temperature': 600, 'pH': 8, 'CEC': 21.6, 'AEC': 1.8},
    {'Temperature': 700, 'pH': 8, 'CEC': 6.5, 'AEC': 7.0},
    {'Temperature': 900, 'pH': 8, 'CEC': 9.9, 'AEC': 11.5},
    # pH 10
    {'Temperature': 400, 'pH': 10, 'CEC': 25.9, 'AEC': 0.0},
    {'Temperature': 500, 'pH': 10, 'CEC': 27.1, 'AEC': 1.2},
    {'Temperature': 600, 'pH': 10, 'CEC': 18.0, 'AEC': 0.8},
    {'Temperature': 700, 'pH': 10, 'CEC': 9.0, 'AEC': 5.0},
    {'Temperature': 900, 'pH': 10, 'CEC': 11.7, 'AEC': 8.8},
]

df_banik = pd.DataFrame(dados_banik_full)
df_banik_filtrado = df_banik[df_banik['pH'] == ph_opcao]

# Dual Axis Chart for Banik (Dynamic)
fig_banik = make_subplots(specs=[[{"secondary_y": True}]])

# CEC Line
fig_banik.add_trace(
    go.Scatter(x=df_banik_filtrado['Temperature'], y=df_banik_filtrado['CEC'], name="CEC (Negative)",
               mode='lines+markers', line=dict(color='#4caf50', width=3)),
    secondary_y=False,
)

# AEC Line
fig_banik.add_trace(
    go.Scatter(x=df_banik_filtrado['Temperature'], y=df_banik_filtrado['AEC'], name="AEC (Positive)",
               mode='lines+markers', line=dict(color='#ff9800', width=3)),
    secondary_y=True,
)

# UPDATE: Fixing Y-axis range
fig_banik.update_layout(
    title_text=f"The Temperature 'Trade-off' at pH {ph_opcao} (Banik et al., 2018)",
    template="plotly_white",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

fig_banik.update_xaxes(title_text="Pyrolysis Temperature (°C)")
# Left Axis (CEC) - Fixed Range 0-30
fig_banik.update_yaxes(title_text="CEC (cmol · kg⁻¹)", secondary_y=False, title_font=dict(color='#4caf50'), range=[0, 30])
# Right Axis (AEC) - Fixed Range 0-30 for easy direct comparison
fig_banik.update_yaxes(title_text="AEC (cmol · kg⁻¹)", secondary_y=True, title_font=dict(color='#ff9800'), range=[0, 30])

st.plotly_chart(fig_banik, use_container_width=True)
st.caption(f"Note: Data for Corn Stover (CS). Visualizing specific behavior at pH {ph_opcao}. Axes fixed at 0-30 cmol·kg⁻¹ for easier direct comparison.")

# --- New Section: Lawrinenko 2015 and pH ---
st.write("---")
st.markdown("### 📉 The Influence of pH (Lawrinenko et al., 2015)")

st.write("""
As seen above, besides temperature, the chemical environment (pH) also significantly influences charges. 

See the experimental data below from **Lawrinenko et al. (2015)**, investigating AEC as a function of pH for various biochars. 
""")

col_ph1, col_ph2 = st.columns(2)

with col_ph1:
    st.markdown("""
    <div class='ph-box'>
    <b>🧪 In Acidic pH (pH 4):</b><br>
    There is an abundance of protons (H⁺).<br>
    Structures like aromatic rings and pyridinic nitrogens are <b>protonated</b>, generating extra positive charge.
    </div>
    """, unsafe_allow_html=True)

with col_ph2:
    st.markdown("""
    <div class='ph-box'>
    <b>💧 In Alkaline pH (pH 8):</b><br>
    H⁺ concentration drops.<br>
    Only "permanent" charges remain (Oxonium Groups).
    </div>
    """, unsafe_allow_html=True)
    
# --- Full Data Lawrinenko 2015 (Table 1) ---
data_lawrinenko = [
    # Albumin
    {'Biomass': 'Albumin', 'Temp': '500°C', 'pH': 4, 'AEC': 14.7},
    {'Biomass': 'Albumin', 'Temp': '500°C', 'pH': 6, 'AEC': 2.45},
    {'Biomass': 'Albumin', 'Temp': '500°C', 'pH': 8, 'AEC': 1.65},
    {'Biomass': 'Albumin', 'Temp': '700°C', 'pH': 4, 'AEC': 15.5},
    {'Biomass': 'Albumin', 'Temp': '700°C', 'pH': 6, 'AEC': 5.95},
    {'Biomass': 'Albumin', 'Temp': '700°C', 'pH': 8, 'AEC': 2.32},
    # Alfalfa
    {'Biomass': 'Alfalfa', 'Temp': '500°C', 'pH': 4, 'AEC': 10.9},
    {'Biomass': 'Alfalfa', 'Temp': '500°C', 'pH': 6, 'AEC': 3.1},
    {'Biomass': 'Alfalfa', 'Temp': '500°C', 'pH': 8, 'AEC': 0.94},
    {'Biomass': 'Alfalfa', 'Temp': '700°C', 'pH': 4, 'AEC': 25.8},
    {'Biomass': 'Alfalfa', 'Temp': '700°C', 'pH': 6, 'AEC': 9.6},
    {'Biomass': 'Alfalfa', 'Temp': '700°C', 'pH': 8, 'AEC': 2.1},
    # Cellulose
    {'Biomass': 'Cellulose', 'Temp': '500°C', 'pH': 4, 'AEC': 7.8},
    {'Biomass': 'Cellulose', 'Temp': '500°C', 'pH': 6, 'AEC': 2.6},
    {'Biomass': 'Cellulose', 'Temp': '500°C', 'pH': 8, 'AEC': 0.60},
    {'Biomass': 'Cellulose', 'Temp': '700°C', 'pH': 4, 'AEC': 24.2},
    {'Biomass': 'Cellulose', 'Temp': '700°C', 'pH': 6, 'AEC': 18.1},
    {'Biomass': 'Cellulose', 'Temp': '700°C', 'pH': 8, 'AEC': 4.1},
    # Maize Stover
    {'Biomass': 'Corn Stover', 'Temp': '500°C', 'pH': 4, 'AEC': 17.5},
    {'Biomass': 'Corn Stover', 'Temp': '500°C', 'pH': 6, 'AEC': 3.8},
    {'Biomass': 'Corn Stover', 'Temp': '500°C', 'pH': 8, 'AEC': 1.0},
    {'Biomass': 'Corn Stover', 'Temp': '700°C', 'pH': 4, 'AEC': 27.8},
    {'Biomass': 'Corn Stover', 'Temp': '700°C', 'pH': 6, 'AEC': 13.8},
    {'Biomass': 'Corn Stover', 'Temp': '700°C', 'pH': 8, 'AEC': 7.2},
]

df_ph = pd.DataFrame(data_lawrinenko)

st.subheader("📊 Interactive Comparison (Lawrinenko et al., 2015)")

# Filter Widgets
col_sel1, col_sel2 = st.columns(2)
biomassas_disponiveis = df_ph['Biomass'].unique()
temps_disponiveis = df_ph['Temp'].unique()

with col_sel1:
    biomassas_selecionadas = st.multiselect(
        "Select Feedstocks:", 
        options=biomassas_disponiveis,
        default=['Corn Stover', 'Cellulose']
    )

with col_sel2:
    temps_selecionadas = st.multiselect(
        "Select Temperatures:", 
        options=temps_disponiveis,
        default=['500°C', '700°C']
    )

# DataFrame Filtering
df_filtrado_ph = df_ph[
    (df_ph['Biomass'].isin(biomassas_selecionadas)) & 
    (df_ph['Temp'].isin(temps_selecionadas))
]

if df_filtrado_ph.empty:
    st.warning("Please select at least one feedstock and one temperature.")
else:
    # UPDATED CHART:
    # Color = Biomass
    # Line Style/Symbol = Temperature
    fig_ph = px.line(
        df_filtrado_ph, 
        x='pH', 
        y='AEC', 
        color='Biomass',    # Different colors for different materials
        symbol='Temp',        # Different symbols for temperatures
        line_dash='Temp',     # Solid vs dashed line
        markers=True,
        title="Decay of Positive Charge (AEC) with pH",
        color_discrete_sequence=px.colors.qualitative.Set1 # High contrast palette
    )

    fig_ph.update_layout(
        xaxis=dict(tickmode='linear', tick0=4, dtick=2),
        yaxis_title="AEC (cmol · kg⁻¹)",
        template="plotly_white",
        hovermode="x unified",
        legend_title="Variables"
    )

    st.plotly_chart(fig_ph, use_container_width=True)

# --- New Section: Practical Soil Application ---
st.write("---")
st.markdown("### 🌱 Practical Soil Application")

st.markdown("""
<div class='soil-box'>
<h4>What does this mean for the farmer?</h4>
The <b>influence of pH</b> is not just a lab detail. It dictates your biochar's efficiency in the field:
<br><br>
🟡 <b>Acidic Soil:</b> Biochar will have its <b>Positive Charge (AEC) maximized</b>.<br>
This helps retain important anions like <b>Nitrate (NO<sub>3</sub><sup>-</sup>)</b> and <b>Phosphate (PO<sub>4</sub><sup>3-</sup>)</b>, reducing leaching.
<br><br>
🟢 <b>Alkaline Soil (or after Liming):</b> Positive Charge drops, but <b>Negative Charge (CEC) increases</b>.<br>
This improves retention of cations like <b>Calcium (Ca<sup>2+</sup>)</b>, <b>Magnesium (Mg<sup>2+</sup>)</b> and <b>Potassium (K<sup>+</sup>)</b>.
</div>
""", unsafe_allow_html=True)

# --- Case Study: Dey et al. 2023 ---
st.divider()
st.markdown("### 🍚 The Curious Case of Dey et al. (2023)")

col1, col2 = st.columns([1.5, 1])

with col1:
    st.write("""
    **The Material:** Rice Straw.
    **The Temperature:** 400°C.
    
    As we saw, CEC and AEC are present in biochars. However, we can **chemically modify** the surface to increase them, and the possibilities are many.

    Dey et al. (2023), for example, applied 15 types of chemical modifications, and presented the results of the three with the highest increases in CEC and AEC.

    See an example in the chart below:
    """)

with col2:
    st.markdown("""
    <div class='nuance-box'>
    <b>🧐 Scientific Nuance:</b><br>
    Dey et al. do not explain the specific origin of AEC in the control at 400°C, but the mechanism of the <b>modified</b> material is clear:
    <br><br>
    👉 <b>Iron Complexes (Goethite)</b><br>
    👉 <b>Acid Protonation</b>
    </div>
    """, unsafe_allow_html=True)

# --- Educational Section: Unraveling Mysteries ---
with st.expander("🕵️ Unraveling the Mysteries (Click to understand)", expanded=False):
    st.markdown("""
    <div class='mystery-box'>
    <h4>1. Why should the charge be low at 400°C?</h4>
    <p>Literature (Banik et al., 2018) shows that at low temperatures (≤ 500°C), the surface is dominated by <b>negative</b> groups (carboxyls -COOH). Natural positive groups (oxonium) generally only form when carbon becomes aromatic/graphitic above 700°C.</p>
    <hr>
    <h4>2. Where does Goethite come from if the material is organic?</h4>
    <p>It wasn't "born" there! It was <b>added</b>. The engineering process involved soaking the biochar in <b>Ferric Chloride ($FeCl_3$)</b>. Iron precipitated on the carbon surface forming a mineral (Goethite), turning the biochar into a hybrid material (organic + mineral).</p>
    <hr>
    <h4>3. What is Acid Protonation?</h4>
    <p>It is the act of "gluing" protons ($H^+$) to the surface. By washing the biochar with acid (HCl), $H^+$ ions bind to functional groups (like OH turning into $OH_2^+$). Since $H^+$ is positive, the entire surface becomes more positive, attracting anions like a magnet.</p>
    </div>
    """, unsafe_allow_html=True)

# Data Dey et al.
dados_dey = {
    'Biochar': ['Unmodified (400°C)', 'Unmodified (400°C)', 'Modified (O₃ + FeCl₃)', 'Modified (O₃ + FeCl₃)'],
    'Charge Type': ['CEC (Negative)', 'AEC (Positive)', 'CEC (Negative)', 'AEC (Positive)'],
    'Value (cmol/kg)': [39.4, 26.6, 65.6, 58.1]
}
df_dey = pd.DataFrame(dados_dey)

# Chart Dey et al.
mostrar_modificado = st.toggle("✨ Reveal the effect of Chemical Engineering", value=False)

if mostrar_modificado:
    df_filtrado = df_dey
    st.success("Chemical modification doubled the anion retention capacity (AEC)!")
else:
    df_filtrado = df_dey[df_dey['Biochar'] == 'Unmodified (400°C)']

fig_dey = px.bar(
    df_filtrado, x='Biochar', y='Value (cmol/kg)', color='Charge Type',
    barmode='group', text_auto=True,
    color_discrete_map={'CEC (Negative)': '#81c784', 'AEC (Positive)': '#ffb74d'},
    title="Ion Exchange Capacity (Dey et al. 2023)"
)
# Updated to scientific notation
fig_dey.update_layout(yaxis_title="Charge (cmol · kg⁻¹)", xaxis_title="", template="plotly_white", font=dict(size=14))
st.plotly_chart(fig_dey, use_container_width=True)


st.markdown("---")
st.header("📚 References")

st.markdown("""
    **Dey et al. (2023)**
    
    Dey, S., Purakayastha, T. J., Sarkar, B., Rinklebe, J., Kumar, S., Chakraborty, R., Datta, A., Lal, K., & Shivay, Y. S. (2023). **Enhancing cation and anion exchange capacity of rice straw biochar by chemical modification for increased plant nutrient retention**. *Science of the Total Environment*, 886, 163681.
    > [🔗 DOI: 10.1016/j.scitotenv.2023.163681](http://dx.doi.org/10.1016/j.scitotenv.2023.163681)
    
    **Banik et al. (2018)**
    
    Banik, C., Lawrinenko, M., Bakshi, S., & Laird, D. A. (2018). **Impact of Pyrolysis Temperature and Feedstock on Surface Charge and Functional Group Chemistry of Biochars**. *Journal of Environmental Quality*, 47, 452–461.
    > [🔗 DOI: 10.2134/jeq2017.11.0432](https://doi.org/10.2134/jeq2017.11.0432)
    
    **Lawrinenko & Laird (2015)**
    
    Lawrinenko, M., & Laird, D. A. (2015). **Anion exchange capacity of biochar**. *Green Chemistry*, 17, 4628-4636.
    > [🔗 DOI: 10.1039/c5gc00828j](https://doi.org/10.1039/c5gc00828j)
    """)