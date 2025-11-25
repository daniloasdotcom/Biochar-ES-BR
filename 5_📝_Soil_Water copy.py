import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# ------------------------------------------------------------------------------
# 1. Configuração da Página
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Biochar & Água no Solo", layout="centered")

# Paleta fixa de cores por tratamento (para consistência)
COLOR_MAP = {
    "Areia (Controle)": "#1f77b4",
    "Biochar Fino (<0.251 mm) + Areia": "#d62728",
    "Biochar Médio (0.251-0.853 mm) + Areia": "#2ca02c",
    "Biochar Grosseiro (0.853-2.00 mm) + Areia": "#ff7f0e",
    "Controle Físico: Areia Fina + Areia": "#9467bd",
    "Controle Físico: Areia Grosseira + Areia": "#8c564b",
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

# ------------------------------------------------------------------------------
# 2. Cabeçalho do "Blog"
# ------------------------------------------------------------------------------
st.title("Biochar: A Esponja do Solo 🧽")
st.markdown("### Como o biocarvão transforma a física de solos arenosos e a disponibilidade de água")

st.divider()

# ------------------------------------------------------------------------------
# 3. Introdução
# ------------------------------------------------------------------------------
st.markdown("""
A gestão da água em solos agrícolas, especialmente os de textura arenosa, é um dos maiores desafios para a agricultura moderna. 
Solos arenosos drenam rapidamente, retendo pouca humidade para as plantas nos períodos de seca.

O **Biocarvão (Biochar)** surge como uma tecnologia promissora para mitigar este problema. Ao ser incorporado ao solo, ele atua como um condicionador físico,
potencialmente aumentando a **Capacidade de Retenção de Água (CRA)** e, mais importante, a **Água Disponível (AD)** para as culturas.

""")

# ------------------------------------------------------------------------------
# 4. Seção – Mecanismos
# ------------------------------------------------------------------------------
st.markdown("### 🔍 O Mecanismo: Por que o Biochar retém mais água?")

st.write("A capacidade do biocarvão de alterar a hidrologia do solo não é mágica, é física e química. Podemos dividir a sua atuação em três pilares principais:")

with st.expander("1. Efeito de Porosidade (Intraporos vs. Interporos)", expanded=True):
    st.markdown("""
    Esta é a chave para entender os dados apresentados no simulador.
    
    * **Intraporos (O "Armazém"):** São poros microscópicos *dentro* da partícula de carvão. Seguram a água contra a gravidade, mas deixam-na disponível para as raízes. É aqui que a **Água Disponível (AD)** aumenta.
    * **Interporos (O "Dreno"):** Espaços *entre* as partículas. Ajudam na aeração, mas drenam rápido.
    
    🧠 **Ponto-chave:** Moer demais o biochar destrói os intraporos. Biochar muito fino perde a sua função de "esponja interna".
    """)

with st.expander("2. Efeito de Adsorção e Superfície"):
    st.markdown("""
    * **Cargas Elétricas:** Biochars oxidados desenvolvem cargas negativas que atraem moléculas de água.
    * **Hidrofilicidade:** Com o tempo no solo, a superfície do carvão torna-se mais "amiga da água" (hidrofílica), facilitando a entrada do líquido nos poros.
    """)

with st.expander("3. Alteração da Estrutura do Solo"):
    st.markdown("""
    Partículas de biochar são angulares e irregulares. Ao misturá-las com a areia (redonda), elas alteram o empacotamento do solo, criando novos caminhos para a retenção e movimento da água.
    """)

st.info("""
**Experimente você mesmo:**
O gráfico interativo abaixo mostra dados reais. Observe como o **Biochar Grosseiro** (que preservou os seus poros internos) aumenta a curva na faixa útil em comparação à areia pura.
""")

# ------------------------------------------------------------------------------
# 5. Dados Experimentais
# ------------------------------------------------------------------------------
data_parameters = {
    "Areia (Controle)": { "theta_s": 0.34, "w1": 0.914, "alpha1": 0.415, "n1": 1.568, "w2": 0.086, "alpha2": 0.013, "n2": 5.790 },
    "Biochar Fino (<0.251 mm) + Areia": { "theta_s": 0.39, "w1": 0.753, "alpha1": 0.375, "n1": 1.396, "w2": 0.247, "alpha2": 0.556, "n2": 6.805 },
    "Biochar Médio (0.251-0.853 mm) + Areia": { "theta_s": 0.41, "w1": 0.890, "alpha1": 0.479, "n1": 2.901, "w2": 0.110, "alpha2": 0.002, "n2": 5.433 },
    "Biochar Grosseiro (0.853-2.00 mm) + Areia": { "theta_s": 0.37, "w1": 0.849, "alpha1": 0.458, "n1": 1.601, "w2": 0.151, "alpha2": 0.010, "n2": 7.740 },
    "Controle Físico: Areia Fina + Areia": { "theta_s": 0.36, "w1": 0.908, "alpha1": 0.387, "n1": 2.256, "w2": 0.092, "alpha2": 0.017, "n2": 7.829 },
    "Controle Físico: Areia Grosseira + Areia": { "theta_s": 0.37, "w1": 0.906, "alpha1": 0.372, "n1": 1.122, "w2": 0.094, "alpha2": 1.442, "n2": 9.029 },
}

# ------------------------------------------------------------------------------
# 6. Funções de Cálculo
# ------------------------------------------------------------------------------
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
    """
    Calcula a capacidade diferencial de água (d_theta / d_psi),
    que representa a distribuição de tamanho de poros.
    A derivada é aproximada numericamente ou analiticamente.
    Aqui usamos a derivada analítica da função VG bimodal.
    """
    # Derivada analítica de van Genuchten: d(theta)/d(psi)
    # theta = theta_s * [ w1*(1+(a1*h)^n1)^(-m1) + w2*(1+(a2*h)^n2)^(-m2) ]
    # dtheta/dh = theta_s * [ w1 * (-m1)*(1+(a1*h)^n1)^(-m1-1) * n1*(a1*h)^(n1-1) * a1 + ... ]
    
    ts = params["theta_s"]
    w1, a1, n1 = params["w1"], params["alpha1"], params["n1"]
    w2, a2, n2 = params["w2"], params["alpha2"], params["n2"]
    m1 = 1 - (1 / n1)
    m2 = 1 - (1 / n2)
    psi = np.maximum(psi, 1e-9)

    # Termo 1
    # (1+(a*h)^n)
    base1 = 1 + (a1 * psi)**n1
    # Derivada interna: n*a*(a*h)^(n-1)
    d_inner1 = n1 * a1 * (a1 * psi)**(n1 - 1)
    # Derivada externa: -m * base^(-m-1)
    d_outer1 = -m1 * (base1)**(-m1 - 1)
    term1_prime = w1 * d_outer1 * d_inner1

    # Termo 2
    base2 = 1 + (a2 * psi)**n2
    d_inner2 = n2 * a2 * (a2 * psi)**(n2 - 1)
    d_outer2 = -m2 * (base2)**(-m2 - 1)
    term2_prime = w2 * d_outer2 * d_inner2

    # dtheta/dpsi total (negativo pois theta diminui com psi, mas queremos a magnitude para distribuição)
    slope = ts * (term1_prime + term2_prime)
    
    # Para distribuição logarítmica (dTheta/d(logPsi)), multiplicamos por psi*ln(10)
    # ou simplesmente plotamos dTheta/d(log10(Psi)) ~ slope * psi * 2.303
    # Vamos plotar a Capacidade Diferencial de Água C(h) = |dtheta/dh|
    return np.abs(slope)

def calculate_awc(params):
    fc = bimodal_van_genuchten(33, params)
    pwp = bimodal_van_genuchten(1500, params)
    return fc, pwp, fc - pwp

@st.cache_data(show_spinner=False)
def compute_curves(data_parameters, psi_min=0.1, psi_max=100000, n_points=1000): # Aumentado para ver poros pequenos
    psi_values = np.logspace(np.log10(psi_min), np.log10(psi_max), n_points)
    curves = {}
    pore_dist = {}
    stats = {}
    for name, params in data_parameters.items():
        theta_values = bimodal_van_genuchten(psi_values, params)
        pore_dist_values = pore_size_distribution(psi_values, params)
        fc, pwp, awc = calculate_awc(params)
        
        curves[name] = theta_values
        pore_dist[name] = pore_dist_values
        stats[name] = {"fc": fc, "pwp": pwp, "awc": awc}
        
    return psi_values, curves, pore_dist, stats

# ------------------------------------------------------------------------------
# 7. Interface do Simulador
# ------------------------------------------------------------------------------
st.markdown("### 📊 Simulador de Curvas de Retenção e Porosidade")

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

# ------------------------------------------------------------------------------
# 8. Abas para Gráficos
# ------------------------------------------------------------------------------
if selected_treatments:
    psi_min_plot = 0.1
    psi_max_plot = 1500  # Para retenção focamos no agrícola
    
    # Calculamos um range maior para a distribuição de poros ficar bonita
    psi_values_calc, curves, pore_dist, stats = compute_curves(data_parameters, psi_min=0.1, psi_max=100000)

    # Filtros para plotagem da retenção (até 1500 kPa)
    mask_retention = psi_values_calc <= 10000 # Mostramos um pouco além do PMP para contexto
    psi_retention = psi_values_calc[mask_retention]

    tab1, tab2 = st.tabs(["💧 Curva de Retenção de Água", "🔬 Distribuição de Tamanho de Poros"])

    # --- TAB 1: RETENÇÃO ---
    with tab1:
        st.caption("Elementos visuais do gráfico:")
        c1, c2, c3 = st.columns(3)
        with c1:
            show_cc = st.checkbox("Capacidade de Campo (33 kPa)", value=True)
        with c2:
            show_pmp = st.checkbox("Ponto de Murcha (1500 kPa)", value=True)
        with c3:
            show_ad = st.checkbox("💧 Água Disponível (faixa CC–PMP)", value=True)

        fig_ret = go.Figure()
        table_data = []
        all_keys = list(data_parameters.keys())

        for treatment in selected_treatments:
            params = data_parameters[treatment]
            
            # Dados filtrados para visualização agronômica
            theta_view = curves[treatment][mask_retention]
            
            fc = stats[treatment]["fc"]
            pwp = stats[treatment]["pwp"]
            awc = stats[treatment]["awc"]
            color = COLOR_MAP.get(treatment, "#000000")
            original_index = all_keys.index(treatment)
            stagger_shift = -30 if (original_index % 2 == 0) else -65

            # Curva Principal
            fig_ret.add_trace(go.Scatter(
                x=theta_view, y=psi_retention, mode="lines",
                name=treatment, line=dict(width=3, color=color),
                legendgroup=treatment
            ))

            # Água Disponível
            if show_ad:
                display_index = selected_treatments.index(treatment)
                y_line_pos = 0.12 * (1.8 ** display_index)
                fig_ret.add_trace(go.Scatter(
                    x=[pwp, fc], y=[y_line_pos, y_line_pos],
                    mode="lines+markers",
                    marker=dict(symbol="line-ns-open", size=12, line_width=2),
                    line=dict(color=color, width=2),
                    showlegend=False, hoverinfo='skip', legendgroup=treatment
                ))
                fig_ret.add_annotation(
                    x=(pwp + fc) / 2, y=np.log10(y_line_pos),
                    text=f"AD: {awc:.3f}", yshift=15,
                    font=dict(color=color, size=11, weight="bold"), showarrow=False
                )

            # Linhas Verticais
            if show_cc:
                fig_ret.add_trace(go.Scatter(
                    x=[fc, fc], y=[0.1, 33], mode="lines",
                    line=dict(width=1, dash="dot", color=color),
                    showlegend=False, hoverinfo="skip", legendgroup=treatment
                ))
                fig_ret.add_annotation(
                    x=fc, y=np.log10(0.1), text=f"{fc:.3f}",
                    showarrow=False, textangle=-90, xanchor="center", yanchor="top",
                    font=dict(color=color, size=11), yshift=stagger_shift
                )

            if show_pmp:
                fig_ret.add_trace(go.Scatter(
                    x=[pwp, pwp], y=[0.1, 1500], mode="lines",
                    line=dict(width=1, dash="dot", color=color),
                    showlegend=False, hoverinfo="skip", legendgroup=treatment
                ))
                fig_ret.add_annotation(
                    x=pwp, y=np.log10(0.1), text=f"{pwp:.3f}",
                    showarrow=False, textangle=-90, xanchor="center", yanchor="top",
                    font=dict(color=color, size=11), yshift=stagger_shift
                )

            table_data.append({
                "Tratamento": treatment,
                "CC": float(fc),
                "PMP": float(pwp),
                "AD": float(awc),
            })

        # Layout Retenção
        fig_ret.add_hline(y=33, line_width=1, line_color="black")
        fig_ret.add_annotation(y=np.log10(33), x=0, text="CC", showarrow=False, yshift=10, xanchor="left", font=dict(color="black"))
        fig_ret.add_hline(y=1500, line_width=2, line_color="black")
        fig_ret.add_annotation(y=np.log10(1500), x=0, text="PMP", showarrow=False, yshift=-15, xanchor="left", font=dict(color="black"))

        fig_ret.update_layout(
            title=dict(text="Curva de Retenção (Log |H|)", font=dict(color="black", size=18)),
            xaxis_title="Umidade Volumétrica (m³/m³)",
            yaxis_title="Potencial Matricial |H| (-kPa)",
            yaxis_type="log", template="plotly_white", plot_bgcolor="white",
            font=dict(color="black", family="Arial", size=14),
            legend=dict(yanchor="top", y=0.98, xanchor="right", x=0.98, bgcolor="rgba(255,255,255,0.9)", bordercolor="black", borderwidth=1),
            margin=dict(l=60, r=20, t=60, b=130), height=600,
        )
        fig_ret.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True, showgrid=True, gridcolor="#dedede", range=[0, 0.5])
        fig_ret.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True, showgrid=True, gridcolor="#dedede", range=[np.log10(0.1), np.log10(10000)])
        
        st.plotly_chart(fig_ret, use_container_width=True)

        # Tabela
        st.subheader("📑 Tabela de Resultados Numéricos")
        df_table = pd.DataFrame(table_data)
        st.dataframe(
            df_table, use_container_width=True, hide_index=True,
            column_config={
                "Tratamento": st.column_config.TextColumn("Tratamento", width="medium"),
                "CC": st.column_config.NumberColumn("Capacidade de Campo", format="%.3f m³/m³"),
                "PMP": st.column_config.NumberColumn("Ponto de Murcha", format="%.3f m³/m³"),
                "AD": st.column_config.ProgressColumn("Água Disponível", format="%.3f m³/m³", min_value=0, max_value=0.15),
            }
        )

    # --- TAB 2: DISTRIBUIÇÃO DE POROS ---
    with tab2:
        st.markdown("""
        **O que este gráfico mostra?**
        Este gráfico representa a frequência de tamanhos de poros (derivada da curva de retenção).
        * **Pico à Esquerda (Baixa Tensão):** Representa os **Macroporos/Interporos** (espaços entre grãos de areia). A água aqui drena facilmente.
        * **Pico/Ombro à Direita (Alta Tensão):** Representa os **Microporos/Intraporos** (dentro do biochar). É onde a água fica retida.
        
        Observe como o **Biochar Grosseiro** apresenta uma "cauda" ou segundo pico mais elevado nas altas tensões (>100 kPa) em comparação à Areia, indicando a presença física de intraporos preservados.
        """)
        
        fig_pore = go.Figure()
        
        for treatment in selected_treatments:
            # Dados completos calculados (sem o filtro curto da retenção)
            dist_values = pore_dist[treatment]
            
            # Multiplicamos por psi para melhor visualização logarítmica (dTheta/dLogPsi)
            # Isso é padrão em física do solo para visualização de distribuição de poros
            # C(h) * h
            log_dist_values = dist_values * psi_values_calc * np.log(10)
            
            color = COLOR_MAP.get(treatment, "#000000")
            
            fig_pore.add_trace(go.Scatter(
                x=psi_values_calc, 
                y=log_dist_values, 
                mode="lines",
                name=treatment,
                fill='tozeroy', # Preenchimento para destacar o volume de poros
                fillcolor=f"rgba{tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (0.1,)}", # Cor transparente
                line=dict(width=2, color=color)
            ))

        # Layout Distribuição
        fig_pore.update_layout(
            title=dict(text="Distribuição de Tamanho de Poros (dθ/d log|H|)", font=dict(color="black", size=18)),
            xaxis_title="Potencial Matricial |H| (-kPa) [↔ Tamanho do Poro]",
            yaxis_title="Frequência de Poros (dθ/d log|H|)",
            xaxis_type="log", # Log no X para ver todas as classes de poros
            template="plotly_white",
            plot_bgcolor="white",
            font=dict(color="black", family="Arial", size=14),
            legend=dict(yanchor="top", y=0.98, xanchor="right", x=0.98, bgcolor="rgba(255,255,255,0.9)", bordercolor="black", borderwidth=1),
            margin=dict(l=60, r=20, t=60, b=60), height=500,
        )
        
        # Inverter eixo X? Não necessariamente, mas lembrar que Baixa Tensão = Poro Grande
        fig_pore.update_xaxes(
            showline=True, linewidth=2, linecolor="black", mirror=True, showgrid=True, gridcolor="#dedede",
            range=[np.log10(0.1), np.log10(100000)],
            title_text="Potencial Matricial (-kPa) <br> (← Poros Grandes  |  Poros Pequenos →)"
        )
        fig_pore.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True, showgrid=True, gridcolor="#dedede")
        
        # Adicionar linhas de referência verticais para classes de poros
        fig_pore.add_vline(x=10, line_dash="dash", line_color="gray", annotation_text="Macroporos", annotation_position="top left")
        fig_pore.add_vline(x=1500, line_dash="dash", line_color="gray", annotation_text="Microporos", annotation_position="top right")

        st.plotly_chart(fig_pore, use_container_width=True)

    # ------------------------------------------------------------------------------
    # 9. Interpretação
    # ------------------------------------------------------------------------------
    st.divider()
    st.markdown("### 🧠 Interpretação Automática")
    for t in selected_treatments:
        cor_badge = COLOR_MAP.get(t, "gray")
        st.markdown(f"<span style='color:{cor_badge}'>**{t}:**</span> {INTERPRETACAO.get(t, 'Sem interpretação.')}", unsafe_allow_html=True)

else:
    st.info("Selecione pelo menos um tratamento acima para gerar a simulação.")