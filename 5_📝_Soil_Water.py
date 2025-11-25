import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# --------------------------------------------------------------------------
# 1. Configuração da Página
# --------------------------------------------------------------------------
st.set_page_config(page_title="Biochar & Água no Solo", layout="centered")

st.markdown("""
<style>

.checkbox-card {
    padding: 8px 12px;
    margin-bottom: 6px;
    border-radius: 4px;
    border: 1px solid #e0e0e0;
    background-color: #fafafa;
    transition: all 0.2s ease-in-out;
}

.checkbox-card:hover {
    background-color: #f0f0f0;
    border-color: #bdbdbd;
}

/* Ajusta alinhamento dos checkboxes */
.stCheckbox > label {
    font-size: 0.92rem;
    line-height: 1.2rem;
}

/* Dá mais espaço vertical entre eles */
.stCheckbox {
    margin-bottom: 4px;

    
}

</style>
""", unsafe_allow_html=True)


# Paleta fixa de cores por tratamento (para o gráfico de poros)
COLOR_MAP_TREATMENTS = {
    "Areia (Controle)": "#1f77b4",
    "Biochar Fino (<0.251 mm) + Areia": "#d62728",
    "Biochar Médio (0.251-0.853 mm) + Areia": "#2ca02c",
    "Biochar Grosseiro (0.853-2.00 mm) + Areia": "#ff7f0e",
    "Controle Físico: Areia Fina + Areia": "#9467bd",
    "Controle Físico: Areia Grosseira + Areia": "#8c564b",
}

# Cores para as barras (Métricas)
COLOR_METRICS = {
    "PMP": "#A52A2A",
    "AD": "#2CA02C",
    "CC": "#1F77B4"
}

# Interpretação automática por tratamento
INTERPRETACAO = {
    "Areia (Controle)": (
        "Solo arenoso puro, com poucos poros finos. "
        "Baixa capacidade de campo e baixa água disponível."
    ),
    "Biochar Fino (<0.251 mm) + Areia": (
        "Os intraporos foram em grande parte destruídos pela moagem. "
        "O aumento de água ocorre sobretudo em potenciais altos (solo muito úmido), "
        "devido ao efeito de interporos. Melhora pouco a água disponível na seca."
    ),
    "Biochar Médio (0.251-0.853 mm) + Areia": (
        "Parte dos intraporos é preservada. "
        "Aumenta a capacidade de campo e a água disponível. "
        "Equilíbrio entre poros internos e alteração de empacotamento."
    ),
    "Biochar Grosseiro (0.853-2.00 mm) + Areia": (
        "Intraporos bem preservados, com forte incremento na água disponível. "
        "A maior parte do ganho vem de poros < 10 µm que retêm água em potenciais mais baixos."
    ),
    "Controle Físico: Areia Fina + Areia": (
        "Mistura física de areias. Muda o empacotamento, mas não adiciona intraporos novos. "
        "Efeito limitado sobre a água disponível."
    ),
    "Controle Físico: Areia Grosseira + Areia": (
        "Controle físico apenas pela granulometria. "
        "Sem intraporos adicionais; efeitos majoritariamente geométricos."
    ),
}

# --------------------------------------------------------------------------
# 2. Cabeçalho
# --------------------------------------------------------------------------
st.title("Biochar: A Esponja do Solo 🧽")
st.markdown("### Como o biocarvão transforma a física de solos arenosos e a disponibilidade de água")

st.divider()

# --------------------------------------------------------------------------
# 3. Introdução
# --------------------------------------------------------------------------
st.markdown("""
A gestão da água em solos agrícolas, especialmente os de textura arenosa, é um dos maiores desafios para a agricultura. 
Quanto maior a proporção de areia, mais rapidamente drenam, retendo pouca humidade para as plantas.

O **Biocarvão (Biochar)** pode atuar como uma tecnologia promissora para mitigar este problema. Ao ser incorporado ao solo, ele pode atuar como um condicionador físico,
potencialmente aumentando a **Capacidade de Retenção de Água (CRA)** e, mais importante, a **Água Disponível (AD)** para as culturas.
""")

# --------------------------------------------------------------------------
# 4. Mecanismos
# --------------------------------------------------------------------------
st.markdown("### 🔍 O Mecanismo: Como Biochars podem contribuir para a retenção de água?")
st.write("A capacidade do biocarvão de alterar a hidrologia do solo não é mágica — é física e química. Podemos dividir sua atuação em três pilares:")

# --- SEÇÃO 1: POROSIDADE (ATUALIZADA) ---
with st.expander("1. Efeito de Porosidade (Intraporos vs. Interporos)", expanded=True):
    st.markdown("""
    Esta é a chave para compreender como diferentes granulometrias de biochar modificam o comportamento hídrico do solo.

    **• Intraporos (os “micro-reservatórios”):**  
    São poros internos, localizados **dentro** da partícula de biochar e suficientemente pequenos para reter água sob tensões elevadas, mas ainda acessível às plantas — por isso são os principais responsáveis pelo aumento da **Água Disponível (AD)**.

    **• Interporos (o “espaço entre partículas”):**  
    São poros maiores,  formados **entre** as partículas do solo e as partículas de biochar.  
    Promovem drenagem rápida e boa aeração, mas contribuem pouco para o armazenamento de água.

    🌾 **Origem:**
    Estes espaços porosos são oriundos da estrutura do mateiral original (vasos condutores de seiva, por exemplo) e do processo de pirólise (desobstrução de espaços internos, por exemplo).  
    Materiais com alta porosidade (como cascas) e pirólise em temperaturas moderadas tendem a gerar biochars com mais intraporos.

    🧠 **Ponto central:**  
    Moer os biocarvões excessivamente destrói os intraporos, reduzindo drasticamente a capacidade do biochar de funcionar como “esponja interna”.  
    Biochars mais grossos preservam esses poros e, portanto, aumentam muito melhor a retenção de água útil.
    """)

# --- SEÇÃO 2: OXIDAÇÃO (ATUALIZADA) ---
with st.expander("2. Efeito de Adsorção e Superfície"):
    st.markdown("""
    Além da porosidade, a **química da superfície** do biochar pode ser modificada — e isso altera profundamente sua afinidade pela água.

    **• Oxidação superficial (envelhecimento):**  
    Quando exposto ao ar, ao solo ou a tratamentos químicos, o biochar desenvolve grupos funcionais como **carboxilas (–COOH)**.  
    Esses grupos aumentam as cargas negativas da superfície, tornando o material mais **hidrofílico**.

    **• Adsorção facilitada de água:**  
    A superfície oxidada atrai moléculas de água e reduz a hidrofobicidade inicial, permitindo também que a água penetre nos intraporos com mais facilidade.

    ➤ Em termos práticos:  
      - Biochars **não oxidados (UO)** tendem a repelir água no início.  
      - Biochars **oxidados (AO)** absorvem água com muito mais eficiência, maximizando também a ocupação dos poros internos.
    """)

# --- SEÇÃO 3 (inalterada) ---
with st.expander("3. Alteração da Estrutura do Solo"):
    st.markdown("""
    Partículas de biochar são angulares, irregulares e possuem cargas elétricas. Ao misturá-las com as particulas do solo, alteram o empacotamento do solo, criando novos sítios de interação ecaminhos para a retenção e movimento da água.
    """)

st.info("""
**Experimente você mesmo:**
O gráfico interativo abaixo mostra dados reais baseados em Liu et al. (2017). Observe como o **Biochar Grosseiro** (que preservou seus poros internos) altera os parâmetros hídricos em comparação à areia pura.
""")

# --------------------------------------------------------------------------
# 5. Dados Experimentais (Parâmetros do Artigo)
# --------------------------------------------------------------------------

data_parameters = {
    "Areia (Controle)": { "theta_s": 0.34, "w1": 0.914, "alpha1": 0.415, "n1": 1.568, "w2": 0.086, "alpha2": 0.013, "n2": 5.790 },
    "Biochar Fino (<0.251 mm) + Areia": { "theta_s": 0.39, "w1": 0.753, "alpha1": 0.375, "n1": 1.396, "w2": 0.247, "alpha2": 0.556, "n2": 6.805 },
    "Biochar Médio (0.251-0.853 mm) + Areia": { "theta_s": 0.41, "w1": 0.890, "alpha1": 0.479, "n1": 2.901, "w2": 0.110, "alpha2": 0.002, "n2": 5.433 },
    "Biochar Grosseiro (0.853-2.00 mm) + Areia": { "theta_s": 0.37, "w1": 0.849, "alpha1": 0.458, "n1": 1.601, "w2": 0.151, "alpha2": 0.010, "n2": 7.740 },
    "Controle Físico: Areia Fina + Areia": { "theta_s": 0.36, "w1": 0.908, "alpha1": 0.387, "n1": 2.256, "w2": 0.092, "alpha2": 0.017, "n2": 7.829 },
    "Controle Físico: Areia Grosseira + Areia": { "theta_s": 0.37, "w1": 0.906, "alpha1": 0.372, "n1": 1.122, "w2": 0.094, "alpha2": 1.442, "n2": 9.029 },
}

VALORES_EXPERIMENTAIS = {
    "Areia (Controle)":                         {"cc": 0.025, "pmp": 0.005, "ad": 0.018},
    "Biochar Fino (<0.251 mm) + Areia":         {"cc": 0.028, "pmp": 0.007, "ad": 0.021},
    "Biochar Médio (0.251-0.853 mm) + Areia":   {"cc": 0.042, "pmp": 0.010, "ad": 0.032},
    "Biochar Grosseiro (0.853-2.00 mm) + Areia":{"cc": 0.050, "pmp": 0.010, "ad": 0.040},
}

# --------------------------------------------------------------------------
# 6. Funções
# --------------------------------------------------------------------------
def bimodal_van_genuchten(psi, params):
    ts = params["theta_s"]
    w1, a1, n1 = params["w1"], params["alpha1"], params["n1"]
    w2, a2, n2 = params["w2"], params["alpha2"], params["n2"]
    m1 = 1 - (1 / n1)
    m2 = 1 - (1 / n2)
    psi = np.maximum(psi, 1e-9)
    term1 = w1 * ((1 + (a1 * psi) ** n1) ** (-m1))
    term2 = w2 * ((1 + (a2 * psi) ** n2) ** (-m2))
    return ts * (term1 + term2)

def pore_size_distribution(psi, params):
    ts = params["theta_s"]
    w1, a1, n1 = params["w1"], params["alpha1"], params["n1"]
    w2, a2, n2 = params["w2"], params["alpha2"], params["n2"]
    m1 = 1 - (1 / n1)
    m2 = 1 - (1 / n2)
    psi = np.maximum(psi, 1e-9)

    base1 = 1 + (a1 * psi)**n1
    d_inner1 = n1 * a1 * (a1 * psi)**(n1 - 1)
    d_outer1 = -m1 * (base1)**(-m1 - 1)
    term1_prime = w1 * d_outer1 * d_inner1

    base2 = 1 + (a2 * psi)**n2
    d_inner2 = n2 * a2 * (a2 * psi)**(n2 - 1)
    d_outer2 = -m2 * (base2)**(-m2 - 1)
    term2_prime = w2 * d_outer2 * d_inner2

    slope = ts * (term1_prime + term2_prime)
    return np.abs(slope)

def calculate_awc_vg(params):
    fc = bimodal_van_genuchten(33, params)
    pwp = bimodal_van_genuchten(1500, params)
    return fc, pwp, fc - pwp

def format_label(t):
    # Remove + Areia (caso queira simplificar)
    clean = t.replace(" + Areia", "").replace("Controle Físico: ", "")
    
    # Se tiver parênteses, separar o nome e o detalhe
    if "(" in clean and ")" in clean:
        main, detail = clean.split("(", 1)
        detail = "(" + detail  # recoloca o parênteses removido no split
        return main.strip() + "<br>" + detail.strip()
    else:
        return clean

@st.cache_data(show_spinner=False)
def compute_data(data_parameters, psi_min=0.1, psi_max=100000, n_points=1000):
    psi_values = np.logspace(np.log10(psi_min), np.log10(psi_max), n_points)
    curves = {}
    pore_dist = {}
    
    for name, params in data_parameters.items():
        theta_values = bimodal_van_genuchten(psi_values, params)
        pore_dist_values = pore_size_distribution(psi_values, params)
        
        curves[name] = theta_values
        pore_dist[name] = pore_dist_values
        
    return psi_values, curves, pore_dist

# --------------------------------------------------------------------------
# 7. Interface do Simulador
# --------------------------------------------------------------------------
st.markdown("### 📊 Simulador de Parâmetros Hídricos")
st.caption("Selecione os tratamentos para comparar:")

col_t1, col_t2 = st.columns(2)
treatments_list = list(data_parameters.keys())
selected_treatments = []
defaults = ["Areia (Controle)", "Biochar Grosseiro (0.853-2.00 mm) + Areia"]

for i, treatment in enumerate(treatments_list):
    col_to_use = col_t1 if i % 2 == 0 else col_t2
    with col_to_use:
        is_checked = st.checkbox(treatment, value=(treatment in defaults), key=f"chk_{i}")
        if is_checked:
            selected_treatments.append(treatment)

st.divider()

# --------------------------------------------------------------------------
# 8. Abas
# --------------------------------------------------------------------------
if selected_treatments:
    psi_values_calc, curves, pore_dist = compute_data(data_parameters)

    tab1, tab2 = st.tabs(["📊 PMP, CC e AD (Barras - Dados Experimentais)", "🔬 Distribuição de Tamanho de Poros"])

    # --- TAB 1 ---
    with tab1:
        st.markdown("""
        **Comparativo de Disponibilidade Hídrica (Valores reportados por Liu et al., 2017):**
        * **PMP (Ponto de Murcha Permanente):** Água retida com muita força, indisponível para plantas.
        * **AD (Água Disponível):** O "tanque" de água que a planta consegue beber.
        * **CC (Capacidade de Campo):** Soma de PMP + AD. O máximo que o solo segura sem drenar.
        """)
        
        fig_bar = go.Figure()
        
        names = []
        vals_pmp = []
        vals_ad = []
        vals_cc = []
        
        for t in selected_treatments:
            names.append(format_label(t))
            
            if t in VALORES_EXPERIMENTAIS:
                pmp = VALORES_EXPERIMENTAIS[t]["pmp"]
                cc = VALORES_EXPERIMENTAIS[t]["cc"]
                ad = VALORES_EXPERIMENTAIS[t]["ad"]
            else:
                cc_calc, pmp_calc, ad_calc = calculate_awc_vg(data_parameters[t])
                pmp, cc, ad = pmp_calc, cc_calc, ad_calc
            
            vals_pmp.append(pmp)
            vals_ad.append(ad)
            vals_cc.append(cc)

        fig_bar.add_trace(go.Bar(
            name="PMP (Indisponível)", 
            x=names, y=vals_pmp, 
            marker_color=COLOR_METRICS["PMP"],
            text=[f"{v:.3f}" for v in vals_pmp], textposition='auto'
        ))

        fig_bar.add_trace(go.Bar(
            name="AD (Água Disponível)", 
            x=names, y=vals_ad, 
            marker_color=COLOR_METRICS["AD"],
            text=[f"{v:.3f}" for v in vals_ad], textposition='auto'
        ))

        fig_bar.add_trace(go.Bar(
            name="CC (Capacidade Campo)", 
            x=names, y=vals_cc, 
            marker_color=COLOR_METRICS["CC"],
            text=[f"{v:.3f}" for v in vals_cc], textposition='auto'
        ))

        fig_bar.update_layout(
            barmode='group',
            title="Parâmetros Hídricos Experimentais (m³/m³)",
            yaxis_title="Umidade Volumétrica (m³/m³)",
            xaxis_tickangle=0,
            template="plotly_white",
            height=500,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        fig_bar.update_xaxes(
            tickfont=dict(color="black"),
            title_font=dict(color="black"),
            tickangle=0
        )

        fig_bar.update_yaxes(
            title_font=dict(color="black"),
            tickfont=dict(color="black")
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)

        df_data = []
        for i, t in enumerate(selected_treatments):
            df_data.append({
                "Tratamento": t,
                "PMP": vals_pmp[i],
                "AD": vals_ad[i],
                "CC": vals_cc[i]
            })

    # --- TAB 2 ---
    with tab2:
        st.markdown("""
        **Distribuição de Tamanho de Poros:**
        Este gráfico mostra a frequência de poros baseada na derivada das curvas ajustadas de Van Genuchten.
        * **Esquerda (< 100 kPa):** Macroporos (drenagem).
        * **Direita (> 100 kPa):** Microporos e Intraporos (armazenamento).
        """)
        
        fig_pore = go.Figure()
        
        for treatment in selected_treatments:
            dist_values = pore_dist[treatment]
            log_dist_values = dist_values * psi_values_calc * np.log(10)
            
            color = COLOR_MAP_TREATMENTS.get(treatment, "#000000")
            
            fig_pore.add_trace(go.Scatter(
                x=psi_values_calc, 
                y=log_dist_values, 
                mode="lines",
                name=treatment,
                fill='tozeroy', 
                fillcolor=f"rgba{tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (0.1,)}",
                line=dict(width=2, color=color)
            ))

        fig_pore.update_layout(
            title=dict(text="Frequência de Tamanho de Poros", font=dict(color="black", size=18)),
            xaxis_title="Potencial Matricial |H| (-kPa) [↔ Tamanho do Poro]",
            yaxis_title="Frequência Relativa (dθ/d log|H|)",
           
            xaxis_type="log",
            template="plotly_white",
            legend=dict(yanchor="top", y=0.98, xanchor="right", x=0.98, bgcolor="rgba(255,255,255,0.9)"),
            margin=dict(l=60, r=20, t=60, b=60), height=500,
        )
        
        fig_pore.update_xaxes(
            showline=True, linewidth=2, linecolor="black", mirror=True, showgrid=True, gridcolor="#dedede",
            range=[np.log10(0.1), np.log10(100000)],
            title_text="Potencial Matricial (-kPa) <br> (← Poros Grandes  |  Poros Pequenos →)",
            title_font=dict(color="black"),
            tickfont=dict(color="black")
        )
        fig_pore.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True, showgrid=True, gridcolor="#dedede",
        title_font=dict(color="black"),
        tickfont=dict(color="black"))
        
        fig_pore.add_vline(x=10, line_dash="dash", line_color="gray", annotation_text="Macro", annotation_position="top left")
        fig_pore.add_vline(x=1500, line_dash="dash", line_color="gray", annotation_text="Micro", annotation_position="top right")

        st.plotly_chart(fig_pore, use_container_width=True)

    # ------------------------------------------------------------------
    # 9. Interpretação
    # ------------------------------------------------------------------
    st.divider()
    st.markdown("### 🧠 Interpretação")
    for t in selected_treatments:
        cor_badge = COLOR_MAP_TREATMENTS.get(t, "gray")
        st.markdown(f"<span style='color:{cor_badge}'>**{t}:**</span> {INTERPRETACAO.get(t, 'Sem interpretação.')}", unsafe_allow_html=True)

else:
    st.info("Selecione pelo menos um tratamento acima para gerar a simulação.")

# --------------------------------------------------------------------------
# SEGUNDA METADE DO SEU CÓDIGO (SULIMAN 2017)
# --------------------------------------------------------------------------

HEX_SOIL = "#1f77b4"
HEX_UO = "#ff7f0e"
HEX_AO = "#2ca02c"

RGBA_SOIL = "rgba(31, 119, 180, 0.15)"
RGBA_UO = "rgba(255, 127, 14, 0.2)"
RGBA_AO = "rgba(44, 160, 44, 0.2)"

DATA_SULIMAN = {
    "Areia Quincy (Controle)": {
        "vg_params": {"theta_s": 0.285, "theta_r": 0.063, "alpha": 0.20, "n": 9.44},
        "metrics": {"bd": 1.49, "awc": 11.59, "pmp": 5.32},
        "desc": "Solo arenoso puro."
    },
    "Pinus 350°C": {
        "UO": { 
            "vg_params": {"theta_s": 0.261, "theta_r": 0.062, "alpha": 0.18, "n": 4.46},
            "metrics": {"bd": 1.27, "awc": 20.40, "pmp": 6.15},
            "desc": "Hidrofóbico inicial."
        },
        "AO": { 
            "vg_params": {"theta_s": 0.271, "theta_r": 0.067, "alpha": 0.16, "n": 2.85},
            "metrics": {"bd": 1.28, "awc": 20.40, "pmp": 6.69},
            "desc": "Oxidado (COOH aumentou)."
        }
    },
    "Pinus 600°C": {
        "UO": { 
            "vg_params": {"theta_s": 0.261, "theta_r": 0.066, "alpha": 0.19, "n": 2.80},
            "metrics": {"bd": 1.26, "awc": 19.15, "pmp": 6.56},
            "desc": "Alta área superficial."
        },
        "AO": { 
            "vg_params": {"theta_s": 0.271, "theta_r": 0.066, "alpha": 0.16, "n": 3.72},
            "metrics": {"bd": 1.27, "awc": 20.94, "pmp": 6.56},
            "desc": "Molhabilidade melhorada."
        }
    },
    "Casca Pinus 350°C": {
        "UO": { 
            "vg_params": {"theta_s": 0.261, "theta_r": 0.064, "alpha": 0.17, "n": 4.17},
            "metrics": {"bd": 1.28, "awc": 17.27, "pmp": 6.41},
            "desc": "Muito hidrofóbico."
        },
        "AO": { 
            "vg_params": {"theta_s": 0.271, "theta_r": 0.066, "alpha": 0.16, "n": 4.52},
            "metrics": {"bd": 1.27, "awc": 19.27, "pmp": 6.60},
            "desc": "Retenção aumentada."
        }
    },
    "Casca Pinus 600°C": {
        "UO": { 
            "vg_params": {"theta_s": 0.261, "theta_r": 0.064, "alpha": 0.16, "n": 5.98},
            "metrics": {"bd": 1.29, "awc": 19.02, "pmp": 6.41},
            "desc": "Estrutura rígida."
        },
        "AO": { 
            "vg_params": {"theta_s": 0.271, "theta_r": 0.059, "alpha": 0.15, "n": 3.86},
            "metrics": {"bd": 1.27, "awc": 21.29, "pmp": 5.89},
            "desc": "Melhor desempenho Casca."
        }
    },
    "Álamo 350°C": {
        "UO": { 
            "vg_params": {"theta_s": 0.261, "theta_r": 0.061, "alpha": 0.18, "n": 2.96},
            "metrics": {"bd": 1.28, "awc": 22.59, "pmp": 6.09},
            "desc": "Alta porosidade natural."
        },
        "AO": { 
            "vg_params": {"theta_s": 0.271, "theta_r": 0.063, "alpha": 0.17, "n": 4.48},
            "metrics": {"bd": 1.26, "awc": 23.90, "pmp": 6.32},
            "desc": "Campeão em AWC."
        }
    },
    "Álamo 600°C": {
        "UO": { 
            "vg_params": {"theta_s": 0.261, "theta_r": 0.068, "alpha": 0.17, "n": 3.03},
            "metrics": {"bd": 1.27, "awc": 18.71, "pmp": 6.79},
            "desc": "pH alto."
        },
        "AO": { 
            "vg_params": {"theta_s": 0.271, "theta_r": 0.065, "alpha": 0.15, "n": 4.78},
            "metrics": {"bd": 1.28, "awc": 19.34, "pmp": 6.52},
            "desc": "Oxidação pouco efetiva."
        }
    }
}

def van_genuchten(psi, params):
    tr = params["theta_r"]
    ts = params["theta_s"]
    alpha = params["alpha"]
    n = params["n"]
    m = 1 - (1/n)
    psi = np.maximum(psi, 1e-9)
    denom = (1 + (alpha * psi)**n)**m
    return tr + ((ts - tr) / denom)

def pore_size_dist_slope(psi, params):
    delta = 1e-4
    log_psi = np.log10(psi)
    psi_plus = 10**(log_psi + delta)
    psi_minus = 10**(log_psi - delta)
    theta_plus = van_genuchten(psi_plus, params)
    theta_minus = van_genuchten(psi_minus, params)
    slope = (theta_minus - theta_plus) / (2 * delta)
    return np.abs(slope)

st.markdown("### Funcionalização de Biochars e Retenção de Água no Solo")
st.markdown("""
Selecione individualmente os tratamentos (Oxidados ou Não Oxidados) para comparação detalhada.
""")

flat_options = [
    {"label": "Areia Quincy (Controle)", "type": "control", "key": "Areia Quincy (Controle)"}
]

feedstocks = ["Pinus 350°C", "Pinus 600°C", "Casca Pinus 350°C", "Casca Pinus 600°C", "Álamo 350°C", "Álamo 600°C"]

for fs in feedstocks:
    flat_options.append({"label": f"{fs} - Não Oxidado (UO)", "type": "UO", "key": fs})
    flat_options.append({"label": f"{fs} - Oxidado (AO)", "type": "AO", "key": fs})

selected_options = []
cols = st.columns(3)

for i, opt in enumerate(flat_options):
    col = cols[i % 3]
    with col:
        st.markdown('<div class="checkbox-card">', unsafe_allow_html=True)

        is_default = (
            opt["label"] == "Areia Quincy (Controle)" or 
            opt["label"] == "Álamo 350°C - Oxidado (AO)"
        )

        if st.checkbox(opt["label"], value=is_default, key=f"chk2_{i}"):
            selected_options.append(opt)

        st.markdown('</div>', unsafe_allow_html=True)


if not selected_options:
    st.warning("⚠️ Selecione pelo menos um tratamento.")
    st.stop()

st.divider()

psi_points = np.logspace(-1, 5, 500)
soil_data = DATA_SULIMAN["Areia Quincy (Controle)"]
dist_soil = pore_size_dist_slope(psi_points, soil_data["vg_params"])

tab1, tab2 = st.tabs(["📊 Água Disponível (AWC)", "🔬 Distribuição de Poros"])

with tab1:
    st.markdown("### Comparativo de Água Disponível (AWC)")
    
    names = []
    values = []
    colors = []
    
    for item in selected_options:
        label = item["label"]
        treatment_key = item["key"]
        t_type = item["type"]
        
        names.append(label)
        
        if t_type == "control":
            val = soil_data["metrics"]["awc"]
            colors.append(HEX_SOIL)
        else:
            val = DATA_SULIMAN[treatment_key][t_type]["metrics"]["awc"]
            colors.append(HEX_UO if t_type == "UO" else HEX_AO)
            
        values.append(val)
        
    fig_bar = go.Figure(data=[
        go.Bar(
            x=names, 
            y=values, 
            marker_color=colors,
            text=values,
            textposition='auto'
        )
    ])

    fig_bar.update_layout(
        title="Capacidade de Água Disponível (AWC) %",
        yaxis_title="AWC (% Volumétrico)",
        template="plotly_white",
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    st.markdown("### Distribuição de Tamanho de Poros")
    fig_dist = go.Figure()
    
    for item in selected_options:
        label = item["label"]
        treatment_key = item["key"]
        t_type = item["type"]
        
        if t_type == "control":
            fig_dist.add_trace(go.Scatter(
                x=psi_points, y=dist_soil, 
                mode='lines', 
                name='Areia (Controle)',
                line=dict(color=HEX_SOIL, width=2),
                fill='tozeroy',
                fillcolor=RGBA_SOIL
            ))
        else:
            data = DATA_SULIMAN[treatment_key][t_type]
            dist_val = pore_size_dist_slope(psi_points, data["vg_params"])
            
            color_line = HEX_UO if t_type == "UO" else HEX_AO
            color_fill = RGBA_UO if t_type == "UO" else RGBA_AO
            line_style = 'solid' if t_type == "UO" else 'dot'
            
            fig_dist.add_trace(go.Scatter(
                x=psi_points, y=dist_val, 
                mode='lines', 
                name=label,
                line=dict(color=color_line, width=2, dash=line_style),
                fill='tozeroy',
                fillcolor=color_fill
            ))

    fig_dist.update_layout(
        xaxis_type="log",
        xaxis_title="Potencial Matricial (-kPa)",
        yaxis_title="Frequência Relativa",
        template="plotly_white",
        height=500,
        margin=dict(l=50, r=50, t=50, b=50),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    fig_dist.add_vline(x=10, line_dash="dash", line_color="gray", opacity=0.5)
    fig_dist.add_annotation(x=np.log10(10), y=0.25, text="Macro", showarrow=False, xshift=-20, font=dict(color="gray"))
    fig_dist.add_vline(x=1500, line_dash="dash", line_color="gray", opacity=0.5)
    fig_dist.add_annotation(x=np.log10(1500), y=0.25, text="PMP", showarrow=False, xshift=20, font=dict(color="gray"))

    st.plotly_chart(fig_dist, use_container_width=True)



st.title("Referências")

st.markdown("""
**Suliman et al. (2017)**  
Suliman, W., Harsh, J. B., Abu-Lail, N. I., Fortuna, A.-M., Dallmeyer, I., & Garcia-Pérez, M. (2017).  *The role of biochar porosity and surface functionality in augmenting hydrologic properties of a sandy soil.*  
Science of The Total Environment, 574, 139–147. https://doi.org/10.1016/j.scitotenv.2016.09.025
""")

st.markdown("""
**Liu et al. (2017)**  
Liu, Z., Dugan, B., Masiello, C. A., & Gonnermann, H. M. (2017). *Biochar particle size, shape, and porosity act together to influence soil water properties.*  
PLOS ONE, 12(6), e0179079. https://doi.org/10.1371/journal.pone.0179079
""")
