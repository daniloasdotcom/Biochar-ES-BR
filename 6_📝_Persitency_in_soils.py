import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Configuração da Página
st.set_page_config(
    page_title="Biochar Dispersion Tracker",
    page_icon="🌱",
    layout="centered"
)

# --- CSS para Estilização (Justificado e Cards) ---
st.markdown("""
<style>
    /* Justificar textos gerais */
    .stMarkdown p, .stExpander p, .stMarkdown li {
        text-align: justify;
    }
    /* Estilo para os Cards de Estudos */
    div.study-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #ff4b4b; /* Vermelho Streamlit */
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

# --- Título e Cabeçalho ---
st.title("🌱 Persistência do biocarvão no solo")

# --- Introdução ---
st.markdown("""
Confiar nas propriedades químicas do biocarvão para garantir sua permanência no solo pode ser enganoso. Estudos mostram que, mesmo materiais altamente estáveis, podem migrar ou ser "perdidos" do solo devido a erosão e movimentação vertical.

Tais efeitos, sobretudo as perdas por erosão, devem ser considerados em projetos de uso de biocarvão, seja para melhoria agronômica ou para projetos de remoção de carbono atmosférico, a fim de que sejam desenvolvidas estratégias de manejo adequadas.
""")

st.subheader("📉 Evidências de Perda em Longa Duração")

st.markdown("""
Examinemos, primeiramente, dados que evidenciam a movimentação vertical. **Ding et al. (2023)** e **Gross et al. (2024)**, por exemplo, relatam reduções significativas do estoque de Carbono oriundo dos biocarvões, quantificando movimentações verticais, especialmente em solos com menor teor de argila.
""")

st.markdown("Resumo dos experimentos de campo citados:")

# --- LAYOUT DE CARDS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="study-card">
        <div>
            <div class="study-title">Ding et al. (2023)</div>
            <div class="study-location">📍 Shangzhuang, China</div>
            <div class="study-metric">~49–61% não recuperado</div>
            <div class="study-time">após 11 Anos</div>
            <span class="highlight-climate">Monção Continental (400 mm/ano)</span>
            <hr>
            <div class="study-detail">
                <span class="highlight-soil">Solo Calcário (Franco siltoso)</span><br>
                <small>28% Areia, 52% Silte, 20% Argila</small>
            </div>
            <div class="study-detail">
                <b>Dose:</b> 30, 60 e 90 Mg/ha ou 15, 30 e 45 g/dm³<br>
                <b>Incorp.:</b> 0–20 cm<br>
                <b>Biochar:</b> Casca de arroz + algodão (400°C)<br>
                <b>Causa:</b> Redistribuição vertical, possível transporte abaixo de 30 cm e/ou mineralização; perdas laterais não avaliadas.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="study-card">
        <div>
            <div class="study-title">Gross et al. (2024) [I]</div>
            <div class="study-location">📍 Bayreuth, Alemanha</div>
            <div class="study-metric">~19% não recuperado</div>
            <div class="study-time">após 11 Anos</div>
            <span class="highlight-climate">Temperado Oceânico</span>
            <hr>
            <div class="study-detail">
                <span class="highlight-soil">Solo Franco-Argiloso</span><br>
                <small>62% Areia, 26% Argila</small>
            </div>
            <div class="study-detail">
                <b>Dose:</b> 31,5 Mg/ha ou 31,5 g/dm³<br>
                <b>Incorp.:</b> 0–10 cm<br>
                <b>Biochar:</b> Madeira (≈550°C)<br>
                <b>Causa:</b> Forte redistribuição vertical (0–10 → 10–30 cm); movimentação lateral não mensurada.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="study-card">
        <div>
            <div class="study-title">Gross et al. (2024) [II]</div>
            <div class="study-location">📍 Gartow, Alemanha</div>
            <div class="study-metric">~56% não recuperado</div>
            <div class="study-time">após 9 Anos</div>
            <span class="highlight-climate">Temperado Oceânico</span>
            <hr>
            <div class="study-detail">
                <span class="highlight-soil">Solo Arenoso</span><br>
                <small>94% Areia, 2% Argila</small>
            </div>
            <div class="study-detail">
                <b>Dose:</b> 40 Mg/ha ou 26,7 g/dm³<br>
                <b>Incorp.:</b> 0–15 cm<br>
                <b>Biochar:</b> Madeira (≈650°C)<br>
                <b>Causa:</b> Redistribuição vertical intensa e baixa proteção física do solo arenoso; perdas laterais não quantificadas.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("""

""")
st.markdown("""
Como observado **Ding et al. (2023)** e **Gross et al. (2024)** não fizeram quantificações de movimentação lateral. Além disso, será que a granulometria ou dose aplicada influenciam essa movimentação? 
""")

# --- Transição para Obia et al. ---
st.markdown("""
O trabalho de **Obia et al. (2024)** trás insights importantes sobre essa questão. Eles aprofundaram essa investigação focando na física do transporte. Os dados a seguir são um extrato das observações de **Obia et al. (2024)** em solo franco-arenoso (75% de areia) cultivado com milho, testando o efeito da granulometria e da dose.*

Observemos:
""")

st.divider()

# --- Contexto Experimental ---
st.header("📍 Contexto Experimental")

with st.expander("📋 Ver detalhes completos de Solo, Manejo e Clima", expanded=False):
    st.markdown("""
    * **O Biocarvão:** dry corncob in a retort kiln at a temperature of approximately 400 to 500˚C with a residence time of 24 hrs.
    * **Profundidade de aplicação:** 0-7 cm.
    * **O Solo (Fator Crítico):** Classificado como **Acrisol (FAO)**, textura **Franco-Arenosa**.
        * **Composição Granulométrica:** 75,1% Areia, 15,9% Silte, 9,0% Argila.
        * **Química:** Solo ácido (pH 5,8) e pobre em Carbono Orgânico (0,74%).
        * *Impacto:* A alta porcentagem de areia e baixa quantidade de argila limitam a agregação física, facilitando a migração vertical de partículas finas e a erosão superficial.
    * **Regime de Chuvas:** Clima subtropical úmido com média de **1220 mm/ano**. As chuvas são concentradas na estação quente, criando eventos de precipitação intensa que favorecem o transporte lateral.
    * **Manejo e Adubação:**
        * Cultivo anual de milho com fertilização (NPK + Ureia) em todas as estações.
        * **Preparo:** O solo foi revolvido manualmente (enxada) até **30 cm** para incorporação inicial. O plantio anual envolveu revolvimento superficial recorrente.
    """)

st.divider()

# --- Controles ---
st.subheader("⚙️ Configurações do Cenário")

biochar_size = st.radio(
    "Escolha a Granulometria do Biocarvão:",
    ["Fino (<0.5 mm)", "Médio (0.5-1 mm)", "Grosso (1-5 mm)"],
    index=0,
    horizontal=True 
)

st.sidebar.info(
    """
    **Base de Dados:**
    Os valores percentuais são baseados na recuperação de Carbono do Biocarvão (BC) reportados na Tabela S2 e no texto principal de Obia et al. (2024).
    """
)

# --- Lógica de Dados (Obia et al.) ---
def get_data_profile(size, dosage_type):
    if "Fino" in size:
        if "Baixa" in dosage_type: # BC2
            profile = [41.2, 5.8, 2.3, 1.6, 1.6, 1.5, 5.9, 6.1, 0.5]
            expl = "<b>Alta migração vertical:</b> Partículas finas em dose baixa descem facilmente (efeito peneira). ~25% migrou verticalmente."
        else: # BC4
            profile = [33.3, 1.0, 0.5, 0.3, 0.2, 0.1, 0.9, 0.6, 0.3]
            expl = "<b>Efeito de Bloqueio (Clogging):</b> Dose alta colmatou poros, reduzindo migração vertical (~4%), mas aumentando perda superficial."
    elif "Médio" in size:
        if "Baixa" in dosage_type: # BC1.5
            profile = [35.9, 2.6, 1.8, 1.2, 0.6, 0.8, 3.3, 3.4, 1.0]
            expl = "<b>Comportamento Misto:</b> Recuperação total de ~50%. Migração moderada (~15%) e alta erosão."
        else: # BC3
            profile = [25.2, 0.8, 0.5, 0.3, 0.2, 0.1, 1.5, 2.5, 0.5]
            expl = "<b>Cenário Crítico:</b> Apenas ~25% retido. Combinação de tamanho e dose facilitou erosão lateral extrema (>60% perda)."
    else: # Grosso
        if "Baixa" in dosage_type: # BC2
            profile = [61.9, 1.8, 0.6, 0.2, 0.2, 0.1, 1.1, 0.6, 0.2]
            expl = "<b>Maior Estabilidade:</b> Grosso/Baixa dose teve maior retenção superficial (~62%) e migração insignificante."
        else: # BC4
            profile = [40.8, 1.2, 0.8, 0.4, 0.2, 0.1, 1.2, 2.9, 1.0]
            expl = "<b>Efeito de Dose Inverso:</b> Alta dose criou macroporos, permitindo leve migração, mas erosão dominou."

    return profile, expl

def process_metrics(profile):
    top = profile[0]
    vert = sum(profile[1:])
    loss = max(0, 100 - (top + vert))
    return top, vert, loss

# Obter dados Obia
prof_low, expl_low = get_data_profile(biochar_size, "Baixa")
top_low, vert_low, loss_low = process_metrics(prof_low)

prof_high, expl_high = get_data_profile(biochar_size, "Alta")
top_high, vert_high, loss_high = process_metrics(prof_high)

# --- Layout do Dashboard (Gráficos) ---

# 1. Balanço de Massa
st.header("1. Balanço de Massa")
st.markdown("Comparativo entre Doses:")

col1, col2 = st.columns(2)
labels_pie = ['Retido (0-7cm)', 'Migração Vertical (7-30cm)', 'Perda (Erosão/Min.)']
colors_pie = ['#3498db', '#f1c40f', '#8c564b']

with col1:
    st.subheader("Dose Baixa (1.5-2%)")
    st.subheader("(19-25,3 g/dm³)")
    fig_pie_low = go.Figure(data=[go.Pie(
        labels=labels_pie, values=[top_low, vert_low, loss_low], hole=.4,
        marker=dict(colors=colors_pie), textinfo='percent', textposition='inside',
        insidetextfont=dict(size=14), sort=False, pull=[0, 0, 0.1]
    )])
    fig_pie_low.update_layout(legend=dict(orientation="h", y=-0.1), margin=dict(t=20, b=20, l=10, r=10))
    st.plotly_chart(fig_pie_low, use_container_width=True)
    st.info(expl_low, icon="ℹ️")

with col2:
    st.subheader("Dose Alta (3-4%)")
    st.subheader("(37,9-50,4 g/dm³)")
    fig_pie_high = go.Figure(data=[go.Pie(
        labels=labels_pie, values=[top_high, vert_high, loss_high], hole=.4,
        marker=dict(colors=colors_pie), textinfo='percent', textposition='inside',
        insidetextfont=dict(size=14), sort=False, pull=[0, 0, 0.1]
    )])
    fig_pie_high.update_layout(legend=dict(orientation="h", y=-0.1), margin=dict(t=20, b=20, l=10, r=10))
    st.plotly_chart(fig_pie_high, use_container_width=True)
    st.info(expl_high, icon="ℹ️")

st.divider()

# 2. Migração Vertical
st.header("2. Detalhe do Perfil de Profundidade")
st.markdown("Distribuição do biocarvão remanescente nas camadas do solo:")

col3, col4 = st.columns(2)
global_max_x = max(max(prof_low), max(prof_high)) * 1.15 
layers_label = ["0-7 cm", "7-8 cm", "8-9 cm", "9-10 cm", "10-11 cm", "11-12 cm", "12-17 cm", "17-25 cm", "25-30 cm"]
color_map_bar = {"Retido (0-7cm)": "#3498db", "Migração Vertical": "#f1c40f"}

def create_bar_chart(profile, max_x_range):
    colors_bar = ["Retido (0-7cm)"] + ["Migração Vertical"] * (len(profile)-1)
    df = pd.DataFrame({"Camada": layers_label, "Recuperação (%)": profile, "Categoria": colors_bar})
    
    fig = px.bar(df, x='Recuperação (%)', y='Camada', color='Categoria', orientation='h', 
                 text_auto='.1f', color_discrete_map=color_map_bar)
    
    fig.update_yaxes(autorange="reversed", tickfont=dict(color="black"))
    fig.update_xaxes(
        range=[0, max_x_range], showline=True, linewidth=1, linecolor='black',
        tickfont=dict(color="black"), title_font=dict(color="black")
    )
    fig.update_layout(showlegend=False, xaxis_title="Recuperação (%)", margin=dict(t=10))
    return fig

with col3:
    st.markdown("**Perfil - Dose Baixa**")
    st.plotly_chart(create_bar_chart(prof_low, global_max_x), use_container_width=True)

with col4:
    st.markdown("**Perfil - Dose Alta**")
    st.plotly_chart(create_bar_chart(prof_high, global_max_x), use_container_width=True)

st.divider()

# --- CONCLUSÃO ---
st.subheader("🚨 Implicações para Mercados de Carbono e Manejo")

st.markdown("""
Os dados apresentados evidenciam um risco estrutural: do ponto de vista agronômico é desejável que o biocarvão permaneça no solo para que expresse seus efeitos positivos na produção agricola; já no que se refere à sua função como sumidouro de carbono atmosférico, **a contabilidade de créditos de carbono baseada apenas na "aplicação" mostra-se insuficiente e arriscada.** Para ambos os pontos de vista, se as perdas observadas são resultado de **movimentação lateral (erosão)**, a premissa fundamental de que o biocarvão permanece no solo é quebrada. Essa migração não representa apenas uma falha contábil no mercado de carbono; ela representa perda de insumos e introduz o risco de carrear o material para cursos d'água ou ecossistemas adjacentes.

Para garantir que os biocarvões possam cumprir com sucesso suas funções, algumas recomendações práticas são essenciais:

1.  **Monitoramento da Estabilidade Física:** Não basta medir a estabilidade química (razão H/C); é imperativo monitorar a permanência física do material no local (risco de erosão).
2.  **Manejo Conservacionista Obrigatório:** A elegibilidade para créditos deve estar condicionada à adoção de práticas que mitiguem a erosão (como plantio direto, curvas de nível e cobertura de solo), criando redundância na segurança do armazenamento.
3.  **Método de Aplicação e Incorporação:** Aplicações superficiais sem a devida incorporação representam um alto risco de "fuga" do material. **É fundamental incorporar o biocarvão à matriz do solo** (via meios mecânicos ou biológicos) para reduzir sua exposição direta aos agentes erosivos (água e vento) e aumentar seu tempo de residência.
""")

st.divider()

# --- Referências ---
st.markdown("### 📚 Referências")
st.markdown("""
> Obia A, Lyu J, Mulder J, Martinsen V, Cornelissen G, Smebye AB, et al. (2024) **Biochar dispersion in a tropical soil and its effects on native soil organic carbon.** PLoS ONE 19(4): e0300387.

> Ding X, Li G, Zhao X, Lin Q, Wang X (2023) **Biochar application significantly increases soil organic carbon under conservation tillage: an 11-year field experiment.** Biochar 5:28.

> Gross A, Bromm T, Polifka S, Fischer D, Glaser B (2024) **Long-term biochar and soil organic carbon stability - Evidence from field experiments in Germany.** Science of The Total Environment 954:176340.
""")