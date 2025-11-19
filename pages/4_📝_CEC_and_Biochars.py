import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# ------------------- STREAMLIT SETUP ---------------------
# ---------------------------------------------------------
st.set_page_config(page_title="Soil CEC Simulator", page_icon="🧪", initial_sidebar_state="expanded")

# ---------------------------------------------------------
# --------------- DATA FROM THE SCIENTIFIC PAPER ----------
# ---------------------------------------------------------

# Soil CEC (cmolc/kg)
soil_cec = {
    "Red Latosol": 16,
    "Red-Yellow Latosol": 2.4
}

# Biochar CEC (cmolc/kg) from Table 2 (Domingues et al., 2020)
biochar_cec = {
    "Chicken Manure":  {350: 41.6, 450: 40.7, 750: 21.3},
    "Eucalyptus Sawdust": {350: 10.8, 450: 2.2, 750: 1.4},
    "Coffee Husk": {350: 69.7, 450: 72.0, 750: 18.9},
    "Sugarcane Bagasse": {350: 4.6, 450: 1.8, 750: 1.3}
}

# Local path to the scientific PDF (ensure file exists)
pdf_path = "agronomy-10-00824-v3.pdf"

# ---------------------------------------------------------
# ----------------------- HEADER --------------------------
# ---------------------------------------------------------

st.title("🔬 Dynamic Soil CEC Simulator with Biochar")

st.markdown("""
## 🧪 Understanding CEC and Biochar Effects

### **What is CEC?**
CEC (**Cation Exchange Capacity**) is the soil's ability to retain and exchange nutrient cations such as **Ca²⁺, Mg²⁺, K⁺, and NH₄⁺**.

Since these nutrients carry a **positive charge**, soil particles with **negative charges** attract and hold them, acting like "magnets" or "hooks." This prevents nutrients from leaching away and keeps them available for plant uptake.

Higher CEC generally indicates better fertility and nutrient buffering capacity.

---

### **How does biochar develop CEC?**
Biochar CEC is generated primarily through:
1.  **Surface functional groups:** Oxygen-containing groups (carboxyl, phenolic, hydroxyl) release H⁺ ions, leaving behind negative charges.
2.  **Pyrolysis Temperature:** * **Low temp (e.g., 350°C):** Preserves more functional groups → **Higher CEC**.
    * **High temp (>700°C):** Removes volatile matter and functional groups → **Lower CEC**.
""")

# ---------------------------------------------------------
# -------- NEW EXPANDER: ARTIFICIAL OXIDATION -------------
# ---------------------------------------------------------

with st.expander("🚀 Can we boost Biochar CEC artificially? (Oxidation)"):
    st.markdown("""
    **Yes.** While biochar naturally oxidizes (ages) in the soil over years, we can accelerate this process in the lab/industry.

    **Chemical Oxidation** involves treating biochar with oxidizing agents such as **Nitric Acid (HNO₃)** or **Hydrogen Peroxide (H₂O₂)**.

    **This process:**
    * "Attacks" the aromatic carbon rings.
    * Creates a massive amount of new **Carboxyl (-COOH)** groups on the surface.
    * Can increase the CEC by **5x to 10x** compared to fresh biochar.
    * Transforms hydrophobic biochar into a hydrophilic material with high nutrient retention.
    """)

st.markdown("""
---
### **Factors that determine biochar impact on soil CEC**
1. **Feedstock type:** High-ash materials (Manure/Coffee husk) generally have higher CEC than woody biomass.
2. **Soil type:** The initial CEC of the soil determines if biochar will have an additive or dilutive effect.
3. **Application rate:** The % of biochar in the mixture.

Below is the dataset of CEC values used in this simulator (Domingues et al., 2020).
""")

# ---------------------------------------------------------
# -------------- DISPLAY TABLE (CENTERED + NO INDEX) ------
# ---------------------------------------------------------

st.subheader("Biochar CEC Dataset")
st.caption("Source: Domingues et al., 2020 | Units: **cmolc/kg**")

# Convert to table structure
table_data = []
for feedstock, temps in biochar_cec.items():
    for temp, cec in temps.items():
        table_data.append({
            "Feedstock": feedstock,
            "Pyrolysis Temp (°C)": temp,
            "Biochar CEC (cmolc/kg)": cec
        })

df_biochar = pd.DataFrame(table_data)

# Apply styling
styled_html = (df_biochar.style
    .format({
        "Pyrolysis Temp (°C)": "{:.0f}", 
        "Biochar CEC (cmolc/kg)": "{:.1f}"
    })
    .hide(axis="index")
    .set_properties(**{
        'text-align': 'center',
        'border': '1px solid #e0e0e0',
        'padding': '8px'
    })
    .set_table_styles([
        {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#f8f9fa'), ('color', '#333')]},
        {'selector': 'table', 'props': [('width', '100%'), ('border-collapse', 'collapse')]}
    ])
    .to_html()
)

st.markdown(styled_html, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 👈 Use the Sidebar Panel to simulate the mixture")

# ---------------------------------------------------------
# ----------------- USER INPUT PANEL ----------------------
# ---------------------------------------------------------

# RESTORED ORIGINAL SIDEBAR STRUCTURE
st.sidebar.header("Adjust Biochar Application")

dose = st.sidebar.slider("Biochar rate (% w/w)", 0.0, 20.0, 5.0, step=0.5)
soil_choice = st.sidebar.selectbox("Select Soil", list(soil_cec.keys()))
biochar_choice = st.sidebar.selectbox("Select Biochar Feedstock", list(biochar_cec.keys()))
temperature_choice = st.sidebar.selectbox("Select Pyrolysis Temperature (°C)", [350, 450, 750])

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


# ---------------------------------------------------------
# ---- CALCULATE RESULTING SOIL CEC BASED ON MIXTURE -----
# ---------------------------------------------------------

initial_soil_cec = soil_cec[soil_choice]
selected_biochar_cec = biochar_cec[biochar_choice][temperature_choice]

soil_fraction = (100 - dose) / 100
biochar_fraction = dose / 100

# Mixture rule (weighted average)
final_cec = (soil_fraction * initial_soil_cec) + (biochar_fraction * selected_biochar_cec)

# ---------------------------------------------------------
# --------------------- RESULT BOX ------------------------
# ---------------------------------------------------------

st.subheader("📊 Simulation Results")

st.markdown(f"""
<div style='
    border: 2px solid #4A90E2; 
    padding: 20px; 
    border-radius: 10px; 
    background-color: #F0F7FF;
    text-align: center;
    margin-bottom: 20px;
'>
    <h3 style='color:#1A5276; margin:0;'>Soil: {soil_choice}</h3>
    <h4 style='color:#21618C; margin-top:5px;'>+ {biochar_choice} ({temperature_choice}°C)</h4>
    <hr style='margin: 15px 0; border-top: 1px solid #bcd;'>
    <p style='font-size:22px; color: #000;'>
        Final CEC: <b>{final_cec:.2f}</b> cmolc/kg
    </p>
    <div style='font-size:16px; color: #555; display: flex; justify-content: space-around;'>
        <span>🌱 Initial Soil CEC: <b>{initial_soil_cec}</b></span>
        <span>⚫ Biochar CEC: <b>{selected_biochar_cec}</b></span>
    </div>
    <p style='font-size:14px; margin-top:10px; color:#777;'>Application rate: {dose:.1f}% (w/w)</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ------------------ INTERACTIVE GRAPH --------------------
# ---------------------------------------------------------

# Generate data for plotting 0% to 20%
rates = list(range(0, 21))
cecs = [((1 - r/100) * initial_soil_cec) + ((r/100) * selected_biochar_cec) for r in rates]

df_graph = pd.DataFrame({"Biochar Rate (%)": rates, "Soil CEC (cmolc/kg)": cecs})

fig = px.line(
    df_graph,
    x="Biochar Rate (%)",
    y="Soil CEC (cmolc/kg)",
    title=f"Effect of {biochar_choice} dose on {soil_choice} CEC",
    markers=True
)

# Add reference line for initial soil CEC
fig.add_hline(y=initial_soil_cec, line_dash="dot", 
              annotation_text="Initial Soil CEC", annotation_position="bottom right")

fig.update_layout(
    xaxis_title="Biochar Application Rate (%)",
    yaxis_title="Final Soil CEC (cmolc/kg)",
    hovermode="x"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# ------------------ INFORMATION (DILUTION) ----------------
# ---------------------------------------------------------

with st.expander("💡 Why do some biochars reduce soil CEC? (The Dilution Effect)"):
    st.markdown("""
    <div style="padding: 10px; text-align: justify;">
    Some biochars, like <b>Eucalyptus Sawdust</b> or <b>Bagasse</b> produced at high temperatures, have extremely low CEC (often lower than the soil itself).<br><br>

    When you mix a soil that has moderate CEC (e.g., 16 cmolc/kg) with a biochar that has very low CEC (e.g., 1.4 cmolc/kg), the biochar acts as an "inert" filler regarding charge.<br><br>
    
    This lowers the average charge per kg of the mixture. This is called the <b>Dilution Effect</b>.
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# -------------------- REFERENCE ---------------------------
# ---------------------------------------------------------

st.markdown("""
---
**Source of data:** Domingues, R.R.; Trugilho, P.F.; Silva, C.A.; Melo, I.C.N.A.; Melo, L.C.A.; Magriotis, Z.M.; Sanches, F.L. *Enhancing Cation Exchange Capacity of Weathered Soils Using Biochar*. **Agronomy**, 2020, 10, 824.
""")