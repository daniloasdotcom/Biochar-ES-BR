import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuração da página
st.set_page_config(
    page_title="Cargas em Biocarvão",
    page_icon="⚡",
    layout="centered"
)

# Estilização personalizada
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

# Título
st.title('⚡ O Lado Positivo dos Biocarvões')

# --- Introdução Teórica ---
st.markdown("### 🔍 A Origem da Carga (Biocarvão Natural)")

texto_intro = """
Para explicar a presença de cargas positivas em biocarvões **não modificados**, Dey et al. (2023) referenciam a literatura estabelecida (Banik et al., 2018).

A teoria aceita é que essas cargas (AEC) surgem principalmente de:
1. <span class='highlight'>Grupos Oxônio:</span> Heterociclos de oxigênio (átomos de O com carga positiva integrados aos anéis aromáticos).
2. **Estruturas de Piridínio:** (Em menor grau, dependendo do nitrogênio).

Esses grupos são tipicamente associados a **altas temperaturas de pirólise** (≥700°C), onde a estrutura aromática está condensada.
"""
st.markdown(texto_intro, unsafe_allow_html=True)

# --- Estudo de Caso: Dey et al. 2023 ---
st.divider()
st.markdown("### 🍚 O Caso Curioso de Dey et al. (2023)")

col1, col2 = st.columns([1.5, 1])

with col1:
    st.write("""
    **O Material:** Palha de Arroz (Rice Straw).
    **A Temperatura:** 400°C.
    
    Aqui temos um ponto interessante. Embora a literatura diga que a 400°C a carga positiva (AEC) deveria ser baixa, o controle de Dey (RBC-W) apresentou uma AEC considerável.
    
    Ainda assim, para **aumentar** drasticamente essa capacidade, eles não dependeram dos grupos oxônio naturais. Eles criaram uma nova superfície via engenharia química.
    """)

with col2:
    st.markdown("""
    <div class='nuance-box'>
    <b>🧐 Nuance Científica:</b><br>
    Dey et al. não explicam a origem específica da AEC no controle a 400°C, mas o mecanismo do material <b>modificado</b> é claro:
    <br><br>
    👉 <b>Complexos de Ferro (Goethite)</b><br>
    👉 <b>Protonação por Ácido</b>
    </div>
    """, unsafe_allow_html=True)

# --- Seção Educativa: Desvendando os Mistérios ---
with st.expander("🕵️ Desvendando os Mistérios (Clique para entender)", expanded=False):
    st.markdown("""
    <div class='mystery-box'>
    <h4>1. Por que a carga deveria ser baixa a 400°C?</h4>
    <p>A literatura (Banik et al., 2018) mostra que em baixas temperaturas (≤ 500°C), a superfície é dominada por grupos <b>negativos</b> (carboxilas -COOH). Os grupos positivos naturais (oxônio) geralmente só se formam quando o carbono se torna aromático/grafítico acima de 700°C.</p>
    <hr>
    <h4>2. De onde vem a Goethita se o material é orgânico?</h4>
    <p>Ela não "nasceu" lá! Foi <b>adicionada</b>. O processo de engenharia envolveu mergulhar o biocarvão em <b>Cloreto Férrico ($FeCl_3$)</b>. O ferro precipitou na superfície do carbono formando um mineral (Goethita), transformando o biocarvão em um material híbrido (orgânico + mineral).</p>
    <hr>
    <h4>3. O que é Protonação por Ácido?</h4>
    <p>É o ato de "colar" prótons ($H^+$) na superfície. Ao lavar o biocarvão com ácido (HCl), os íons $H^+$ se ligam aos grupos funcionais (como OH vira $OH_2^+$). Como o $H^+$ é positivo, a superfície inteira fica mais positiva, atraindo ânions como um ímã.</p>
    </div>
    """, unsafe_allow_html=True)

# Dados Dey et al.
dados_dey = {
    'Biocarvão': ['Não Modificado (400°C)', 'Não Modificado (400°C)', 'Modificado (O₃ + FeCl₃)', 'Modificado (O₃ + FeCl₃)'],
    'Tipo de Carga': ['CTC (Negativa)', 'CTA (Positiva)', 'CTC (Negativa)', 'CTA (Positiva)'],
    'Valor (cmol/kg)': [39.4, 26.6, 65.6, 58.1]
}
df_dey = pd.DataFrame(dados_dey)

# Gráfico Dey et al.
mostrar_modificado = st.toggle("✨ Revelar o efeito da Engenharia Química", value=False)

if mostrar_modificado:
    df_filtrado = df_dey
    st.success("A modificação química dobrou a capacidade de retenção de ânions (CTA)!")
else:
    df_filtrado = df_dey[df_dey['Biocarvão'] == 'Não Modificado (400°C)']

fig_dey = px.bar(
    df_filtrado, x='Biocarvão', y='Valor (cmol/kg)', color='Tipo de Carga',
    barmode='group', text_auto=True,
    color_discrete_map={'CTC (Negativa)': '#81c784', 'CTA (Positiva)': '#ffb74d'},
    title="Capacidade de Troca Iônica (Dey et al. 2023)"
)
# Atualizado para notação científica
fig_dey.update_layout(yaxis_title="Carga (cmol · kg⁻¹)", xaxis_title="", template="plotly_white", font=dict(size=14))
st.plotly_chart(fig_dey, use_container_width=True)

st.markdown("""
<div class='citation'>
"Banik et al. (2018) relataram que em temperaturas mais altas, grupos heterocíclicos de oxigênio (grupos oxônio em ponte) dominavam, aumentando a carga positiva..."
<br>— <em>Citado na Introdução de Dey et al. (2023)</em>
</div>
""", unsafe_allow_html=True)

# --- Seção Nova: Banik 2018 e a Temperatura ---
st.write("---")
st.markdown("### 🔥 O Efeito da Temperatura (Banik et al., 2018)")

st.write("""
Para entender a "escolha" da natureza entre carga positiva ou negativa, **Banik et al. (2018)** produziram biocarvões de Palha de Milho (*Corn Stover*) em diversas temperaturas.

O resultado mostra uma troca clara (Trade-off):
""")

col_temp1, col_temp2 = st.columns(2)

with col_temp1:
    st.markdown("""
    <div class='temp-box'>
    <b>⬇️ CTC (Negativa) Cai:</b><br>
    Grupos funcionais ácidos (como carboxilas) são voláteis. Eles são "queimados" e perdidos conforme a temperatura sobe.
    </div>
    """, unsafe_allow_html=True)

with col_temp2:
    st.markdown("""
    <div class='temp-box'>
    <b>⬆️ CTA (Positiva) Sobe:</b><br>
    A estrutura do carbono se condensa (aromatização). Formam-se os grupos Oxônio estáveis e estruturas grafíticas que seguram a carga positiva.
    </div>
    """, unsafe_allow_html=True)

# --- Seletor de pH para Banik ---
st.write("#### 🧪 Escolha o Ambiente Químico (pH):")
ph_opcao = st.radio(
    "Em qual pH você deseja visualizar as cargas?",
    options=[5, 8, 10],
    format_func=lambda x: f"pH {x} ({'Ácido' if x==5 else 'Neutro' if x==8 else 'Alcalino'})",
    horizontal=True
)

# Dados Completos de Banik 2018 (Tabela 1 - Corn Stover)
# Estruturados para fácil filtragem
dados_banik_full = [
    # pH 5
    {'Temperatura': 400, 'pH': 5, 'CTC': 8.0, 'CTA': 1.0},
    {'Temperatura': 500, 'pH': 5, 'CTC': 5.4, 'CTA': 4.0},
    {'Temperatura': 600, 'pH': 5, 'CTC': 5.3, 'CTA': 6.8},
    {'Temperatura': 700, 'pH': 5, 'CTC': 3.0, 'CTA': 13.7},
    {'Temperatura': 900, 'pH': 5, 'CTC': 3.7, 'CTA': 13.6},
    # pH 8
    {'Temperatura': 400, 'pH': 8, 'CTC': 23.9, 'CTA': 0.1},
    {'Temperatura': 500, 'pH': 8, 'CTC': 20.1, 'CTA': 1.5},
    {'Temperatura': 600, 'pH': 8, 'CTC': 21.6, 'CTA': 1.8},
    {'Temperatura': 700, 'pH': 8, 'CTC': 6.5, 'CTA': 7.0},
    {'Temperatura': 900, 'pH': 8, 'CTC': 9.9, 'CTA': 11.5},
    # pH 10
    {'Temperatura': 400, 'pH': 10, 'CTC': 25.9, 'CTA': 0.0},
    {'Temperatura': 500, 'pH': 10, 'CTC': 27.1, 'CTA': 1.2},
    {'Temperatura': 600, 'pH': 10, 'CTC': 18.0, 'CTA': 0.8},
    {'Temperatura': 700, 'pH': 10, 'CTC': 9.0, 'CTA': 5.0},
    {'Temperatura': 900, 'pH': 10, 'CTC': 11.7, 'CTA': 8.8},
]

df_banik = pd.DataFrame(dados_banik_full)
df_banik_filtrado = df_banik[df_banik['pH'] == ph_opcao]

# Gráfico de Eixo Duplo para Banik (Dinâmico)
fig_banik = make_subplots(specs=[[{"secondary_y": True}]])

# Linha CTC
fig_banik.add_trace(
    go.Scatter(x=df_banik_filtrado['Temperatura'], y=df_banik_filtrado['CTC'], name="CTC (Negativa)",
               mode='lines+markers', line=dict(color='#4caf50', width=3)),
    secondary_y=False,
)

# Linha CTA
fig_banik.add_trace(
    go.Scatter(x=df_banik_filtrado['Temperatura'], y=df_banik_filtrado['CTA'], name="CTA (Positiva)",
               mode='lines+markers', line=dict(color='#ff9800', width=3)),
    secondary_y=True,
)

# ATUALIZAÇÃO: Fixando range do eixo Y
fig_banik.update_layout(
    title_text=f"O 'Trade-off' da Temperatura no pH {ph_opcao} (Banik et al., 2018)",
    template="plotly_white",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

fig_banik.update_xaxes(title_text="Temperatura de Pirólise (°C)")
# Eixo Esquerdo (CTC) - Range Fixo 0-30
fig_banik.update_yaxes(title_text="CTC (cmol · kg⁻¹)", secondary_y=False, title_font=dict(color='#4caf50'), range=[0, 30])
# Eixo Direito (CTA) - Range Fixo 0-30 para facilitar comparação direta
fig_banik.update_yaxes(title_text="CTA (cmol · kg⁻¹)", secondary_y=True, title_font=dict(color='#ff9800'), range=[0, 30])

st.plotly_chart(fig_banik, use_container_width=True)
st.caption(f"Nota: Dados para Palha de Milho (CS). Visualizando comportamento específico em pH {ph_opcao}. Eixos fixos em 0-30 cmol·kg⁻¹ para facilitar comparação.")

# --- Seção Nova: Lawrinenko 2015 e o pH ---
st.write("---")
st.markdown("### 📉 A Influência do pH (Lawrinenko et al., 2015)")

st.write("""
Além da temperatura, **Lawrinenko et al. (2015)** mostram que a carga positiva (CTA) é altamente sensível ao pH do solo.
""")

col_ph1, col_ph2 = st.columns(2)

with col_ph1:
    st.markdown("""
    <div class='ph-box'>
    <b>🧪 Em pH Ácido (pH 4):</b><br>
    Há abundância de prótons (H⁺).<br>
    Estruturas como anéis aromáticos e nitrogênios piridínicos são <b>protonadas</b>, gerando muita carga positiva extra.
    </div>
    """, unsafe_allow_html=True)

with col_ph2:
    st.markdown("""
    <div class='ph-box'>
    <b>💧 Em pH Alcalino (pH 8):</b><br>
    A concentração de H⁺ cai.<br>
    Apenas as cargas "permanentes" restam (Grupos Oxônio).
    </div>
    """, unsafe_allow_html=True)

# --- Dados Completos Lawrinenko 2015 (Tabela 1) ---
data_lawrinenko = [
    # Albumin
    {'Biomassa': 'Albumina', 'Temp': '500°C', 'pH': 4, 'AEC': 14.7},
    {'Biomassa': 'Albumina', 'Temp': '500°C', 'pH': 6, 'AEC': 2.45},
    {'Biomassa': 'Albumina', 'Temp': '500°C', 'pH': 8, 'AEC': 1.65},
    {'Biomassa': 'Albumina', 'Temp': '700°C', 'pH': 4, 'AEC': 15.5},
    {'Biomassa': 'Albumina', 'Temp': '700°C', 'pH': 6, 'AEC': 5.95},
    {'Biomassa': 'Albumina', 'Temp': '700°C', 'pH': 8, 'AEC': 2.32},
    # Alfalfa
    {'Biomassa': 'Alfafa', 'Temp': '500°C', 'pH': 4, 'AEC': 10.9},
    {'Biomassa': 'Alfafa', 'Temp': '500°C', 'pH': 6, 'AEC': 3.1},
    {'Biomassa': 'Alfafa', 'Temp': '500°C', 'pH': 8, 'AEC': 0.94},
    {'Biomassa': 'Alfafa', 'Temp': '700°C', 'pH': 4, 'AEC': 25.8},
    {'Biomassa': 'Alfafa', 'Temp': '700°C', 'pH': 6, 'AEC': 9.6},
    {'Biomassa': 'Alfafa', 'Temp': '700°C', 'pH': 8, 'AEC': 2.1},
    # Cellulose
    {'Biomassa': 'Celulose', 'Temp': '500°C', 'pH': 4, 'AEC': 7.8},
    {'Biomassa': 'Celulose', 'Temp': '500°C', 'pH': 6, 'AEC': 2.6},
    {'Biomassa': 'Celulose', 'Temp': '500°C', 'pH': 8, 'AEC': 0.60},
    {'Biomassa': 'Celulose', 'Temp': '700°C', 'pH': 4, 'AEC': 24.2},
    {'Biomassa': 'Celulose', 'Temp': '700°C', 'pH': 6, 'AEC': 18.1},
    {'Biomassa': 'Celulose', 'Temp': '700°C', 'pH': 8, 'AEC': 4.1},
    # Maize Stover
    {'Biomassa': 'Palha de Milho', 'Temp': '500°C', 'pH': 4, 'AEC': 17.5},
    {'Biomassa': 'Palha de Milho', 'Temp': '500°C', 'pH': 6, 'AEC': 3.8},
    {'Biomassa': 'Palha de Milho', 'Temp': '500°C', 'pH': 8, 'AEC': 1.0},
    {'Biomassa': 'Palha de Milho', 'Temp': '700°C', 'pH': 4, 'AEC': 27.8},
    {'Biomassa': 'Palha de Milho', 'Temp': '700°C', 'pH': 6, 'AEC': 13.8},
    {'Biomassa': 'Palha de Milho', 'Temp': '700°C', 'pH': 8, 'AEC': 7.2},
]

df_ph = pd.DataFrame(data_lawrinenko)

st.subheader("📊 Comparativo Interativo (Lawrinenko et al., 2015)")

# Widgets de Filtro
col_sel1, col_sel2 = st.columns(2)
biomassas_disponiveis = df_ph['Biomassa'].unique()
temps_disponiveis = df_ph['Temp'].unique()

with col_sel1:
    biomassas_selecionadas = st.multiselect(
        "Selecione as Biomassas:", 
        options=biomassas_disponiveis,
        default=['Palha de Milho', 'Celulose']
    )

with col_sel2:
    temps_selecionadas = st.multiselect(
        "Selecione as Temperaturas:", 
        options=temps_disponiveis,
        default=['500°C', '700°C']
    )

# Filtragem do DataFrame
df_filtrado_ph = df_ph[
    (df_ph['Biomassa'].isin(biomassas_selecionadas)) & 
    (df_ph['Temp'].isin(temps_selecionadas))
]

if df_filtrado_ph.empty:
    st.warning("Por favor, selecione pelo menos uma biomassa e uma temperatura.")
else:
    # GRÁFICO ATUALIZADO:
    # Cor = Biomassa
    # Estilo da Linha/Símbolo = Temperatura
    fig_ph = px.line(
        df_filtrado_ph, 
        x='pH', 
        y='AEC', 
        color='Biomassa',     # Cores diferentes para materiais diferentes
        symbol='Temp',        # Símbolos diferentes para temperaturas
        line_dash='Temp',     # Linha sólida vs tracejada
        markers=True,
        title="Decaimento da Carga Positiva (AEC) com o pH",
        color_discrete_sequence=px.colors.qualitative.Set1 # Paleta de alto contraste
    )

    fig_ph.update_layout(
        xaxis=dict(tickmode='linear', tick0=4, dtick=2),
        yaxis_title="AEC (cmol · kg⁻¹)",
        template="plotly_white",
        hovermode="x unified",
        legend_title="Variáveis"
    )

    st.plotly_chart(fig_ph, use_container_width=True)

st.info("💡 **Dica de Visualização:** Agora, a **COR** indica o material e o **ESTILO DA LINHA** (sólida/tracejada) indica a temperatura de produção.")

# --- Nova Seção: Aplicação Prática no Solo ---
st.write("---")
st.markdown("### 🌱 Aplicação Prática no Solo")

st.markdown("""
<div class='soil-box'>
<h4>O que isso significa para o agricultor?</h4>
A <b>influência do pH</b> não é apenas um detalhe de laboratório. Ela dita a eficiência do seu biocarvão no campo:
<br><br>
🟡 <b>Solo Ácido:</b> O biocarvão terá sua <b>Carga Positiva (AEC) maximizada</b>.<br>
Isso ajuda a reter ânions importantes como <b>Nitrato ($NO_3^-$)</b> e <b>Fosfato ($PO_4^{3-}$)</b>, reduzindo a lixiviação.
<br><br>
🟢 <b>Solo Alcalino (ou após Calagem):</b> A Carga Positiva cai, mas a <b>Carga Negativa (CTC) aumenta</b>.<br>
Isso melhora a retenção de cátions como <b>Cálcio ($Ca^{2+}$)</b>, <b>Magnésio ($Mg^{2+}$)</b> e <b>Potássio ($K^+$)</b>.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='citation'>
"Biochars produzidos a ≥700°C têm baixa CEC e alta AEC... consistentes com a dominância de carga positiva decorrente de grupos oxônio (heterociclos de oxigênio)."
<br>— <em>Banik et al. (2018)</em>
</div>
""", unsafe_allow_html=True)