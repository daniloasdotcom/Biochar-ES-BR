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

# --- Título e Cabeçalho ---
st.title("🌱 Perssitencia do biocarvão no solo")

st.markdown("""
Confiar nas propriedades químicas do biocarvão para garantir sua permanência no solo pode ser enganoso. Estudos mostram que, mesmo materiais altamente estáveis, podem migrar ou ser perdidos do solo devido a fatores físicos como erosão hídrica e movimentação vertical.

Tais efeitos, sobretudo as perdas por erosão, devem ser considerados em projetos de uso de biocarvão seja para melhoria do solo ou remoção de carbono, a fim de que sejam desenvolvidas estratégias de manejo adequadas para mitigar esses riscos.
""")

st.markdown("""
**Baseado no estudo:** *Obia et al. (2024). Biochar dispersion in a tropical soil and its effects on native soil organic carbon. PLOS ONE.*

Este dashboard interativo explora o destino do biocarvão (Biochar) aplicado em um solo arenoso (Acrisol) na Zâmbia após 4,5 anos.
""")

st.divider()

# --- NOVO: Contexto Experimental (Atualizado com Chuva e Adubação) ---
st.header("📍 Contexto Experimental")
st.markdown("Características do local (Mkushi, Zâmbia) e manejo adotado durante os 4,5 anos:")

# Exibindo dados chave em colunas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Solo (Acrisol)", value="Franco-Arenoso", delta="75% Areia")
    st.caption("Baixa agregação")

with col2:
    st.metric(label="Chuva (Sazonal)", value="1220 mm/ano", delta="Invernos Secos")
    st.caption("Alto Risco Erosivo")

with col3:
    st.metric(label="Relevo", value="Terreno Plano", delta="Erosão Hídrica")
    st.caption("Flat terrain")

with col4:
    st.metric(label="Adubação", value="Anual", delta="NPK + Ureia")
    st.caption("Todo ciclo")

with st.expander("📋 Ver detalhes completos do manejo e clima"):
    st.markdown("""
    * [cite_start]**Regime de Chuvas (Fator Crítico):** Clima subtropical úmido com média de **1220 mm/ano**[cite: 81]. As chuvas são concentradas na estação quente, com invernos secos, criando eventos de precipitação intensa que favorecem a migração lateral e vertical.
    * [cite_start]**Adubação (Nutrição):** O solo foi fertilizado **todos os anos** (durante cada estação de crescimento) com 'Compound D' (NPK 10:20:10 a 200 kg/ha) e cobertura de Ureia (140 kg/ha)[cite: 137].
    * **Preparo do Solo (Tillage):**
        * [cite_start]**Inicial:** Revolvimento manual profundo (enxada) até **30 cm** antes da aplicação do biocarvão para incorporação[cite: 91].
        * [cite_start]**Manutenção:** Plantio de milho realizado anualmente (sem pousio) por 4,5 anos, o que implica revolvimento superficial recorrente para semeadura[cite: 137].
    * [cite_start]**Histórico:** Área já cultivada com milho há 10-15 anos antes do experimento[cite: 80].
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

# Sidebar
st.sidebar.header("⚙️ Filtros Adicionais")
dose = st.sidebar.radio(
    "Selecione a dose:",
    ["Baixa (1.5-2%)", "Alta (3-4%)"]
)

st.sidebar.info(
    """
    **Consistência dos Dados:**
    Agora os gráficos de Pizza (Balanço) e Barras (Perfil) utilizam os mesmos valores percentuais extraídos da Tabela S2 do estudo.
    """
)

# --- Base de Dados Unificada (Tabela S2 - Percentagens Reais) ---
def get_data_profile(size, dosage_type):
    """
    Retorna um dicionário com o perfil de recuperação (%) camada a camada.
    Dados extraídos da Tabela S2 (colunas de %).
    """
    # Estrutura: [0-7, 7-8, 8-9, 9-10, 10-11, 11-12, 12-17, 17-25, 25-30]
    
    if "Fino" in size:
        if "Baixa" in dosage_type: # BC2
            # Perfil de alta infiltração
            profile = [41.2, 5.8, 2.3, 1.6, 1.6, 1.5, 5.9, 6.1, 0.5]
            expl = "Alta migração vertical (total ~25%), com acúmulo notável nas camadas 12-25cm."
        else: # BC4
            # Perfil de bloqueio
            profile = [33.3, 1.0, 0.5, 0.3, 0.2, 0.1, 0.9, 0.6, 0.3]
            expl = "A dose alta bloqueou os poros: retenção superficial menor e migração mínima (~4%). Perda alta por erosão."
            
    elif "Médio" in size:
        if "Baixa" in dosage_type: # BC1.5
            # Perfil de alta migração relativa à retenção
            profile = [35.9, 2.6, 1.8, 1.2, 0.6, 0.8, 3.3, 3.4, 1.0]
            expl = "Recuperação total de ~50%. Migração vertical moderada (~15%)."
        else: # BC3
            # Perfil de alta perda
            profile = [25.2, 0.8, 0.5, 0.3, 0.2, 0.1, 1.5, 2.5, 0.5]
            expl = "Cenário crítico: Apenas ~25% retido na superfície. Perda massiva (>68%)."
            
    else: # Grosso
        if "Baixa" in dosage_type: # BC2
            # Perfil estável
            profile = [61.9, 1.8, 0.6, 0.2, 0.2, 0.1, 1.1, 0.6, 0.2]
            expl = "Alta retenção na superfície (~62%). Migração vertical quase inexistente."
        else: # BC4
            # Perfil com leve descida
            profile = [40.8, 1.2, 0.8, 0.4, 0.2, 0.1, 1.2, 2.9, 1.0]
            expl = "Menor retenção que a dose baixa. Macroporos permitiram leve descida para 17-25cm."

    return profile, expl

# Obtendo os dados
profile_data, text_explanation = get_data_profile(biochar_size, dose)

# Calculando os agregados para o Balanço de Massa
top_layer = profile_data[0] # 0-7cm
vertical_mig = sum(profile_data[1:]) # Soma de 7-30cm
loss = 100 - (top_layer + vertical_mig) # O que falta para 100%

# Ajuste fino para não dar negativo por arredondamento (caso dados originais tenham gap)
loss = max(0, loss)

# --- Layout do Dashboard ---

# 1. Balanço de Massa
st.header("1. Balanço de Massa")
st.caption(f"Cenário: **{biochar_size}** - **{dose}**")

labels_pie = ['Retido (0-7cm)', 'Migração Vertical (7-30cm)', 'Perda (Erosão + Mineralização)']
values_pie = [top_layer, vertical_mig, loss]
colors_pie = ['#3498db', '#f1c40f', '#8c564b']

# Configuração do deslocamento (pull)
pull_config = [0, 0, 0.1] 

fig_pie = go.Figure(data=[go.Pie(
    labels=labels_pie, 
    values=values_pie, 
    hole=.4, 
    marker=dict(colors=colors_pie),
    textinfo='percent',  
    textposition='inside',
    insidetextfont=dict(size=24),
    sort=False, 
    pull=pull_config
)])

fig_pie.update_layout(
    legend=dict(
        orientation="h",       
        yanchor="bottom",
        y=1.1,                 
        xanchor="center",
        x=0.5
    ),
    margin=dict(t=80, b=20, l=20, r=20) 
)

st.plotly_chart(fig_pie, use_container_width=True)
st.info(text_explanation)

st.divider()

# 2. Migração Vertical
st.header("2. Detalhe do Perfil de Profundidade")
st.markdown("""
Este gráfico expande as fatias "Retido" (azul) e "Migração Vertical" (amarelo) do gráfico acima, 
mostrando exatamente em quais camadas o biocarvão foi encontrado.
""")

layers_label = ["0-7 cm", "7-8 cm", "8-9 cm", "9-10 cm", "10-11 cm", "11-12 cm", "12-17 cm", "17-25 cm", "25-30 cm"]

colors_bar = []
for i, val in enumerate(profile_data):
    if i == 0:
        colors_bar.append("Retido (0-7cm)") 
    else:
        colors_bar.append("Migração Vertical") 

df_bar = pd.DataFrame({
    "Camada": layers_label,
    "Recuperação (%)": profile_data,
    "Categoria": colors_bar
})

fig_bar = px.bar(
    df_bar, 
    x='Recuperação (%)', 
    y='Camada', 
    color='Categoria',
    orientation='h',
    text_auto='.1f',
    color_discrete_map={
        "Retido (0-7cm)": "#3498db", 
        "Migração Vertical": "#f1c40f"
    }
)

fig_bar.update_yaxes(autorange="reversed")

fig_bar.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    xaxis_title="Recuperação do Biocarvão Aplicado (%)",
    yaxis_title="Profundidade",
    margin=dict(t=30)
)

st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# --- CONCLUSÃO / TEXTO FINAL ---
st.subheader("🚨 Implicações para Mercados de Carbono e Manejo")

st.markdown("""
Os dados apresentados evidenciam um risco estrutural: **a contabilidade de créditos de carbono baseada apenas na "aplicação" mostrou-se insuficiente e arriscada.** Se as perdas observadas são resultado de **movimentação lateral (erosão)**, a premissa fundamental de que o biocarvão permanece no solo é quebrada. Essa migração não representa apenas uma falha contábil; ela introduz o risco de carrear o material para cursos d'água ou ecossistemas adjacentes, podendo gerar efeitos adversos indesejáveis nesses locais, em vez dos benefícios climáticos esperados.

Para garantir a integridade dos créditos de carbono via biocarvão (Biochar Carbon Removal - BCR), os protocolos devem evoluir para exigir:

1.  **Monitoramento da Estabilidade Física:** Não basta medir a estabilidade química (razão H/C); é imperativo monitorar a permanência física do material no local (risco de erosão).
2.  **Manejo Conservacionista Obrigatório:** A elegibilidade para créditos deve estar condicionada à adoção de práticas que mitiguem a erosão (como plantio direto, curvas de nível e cobertura de solo), criando redundância na segurança do armazenamento.
3.  **Método de Aplicação e Incorporação:** Aplicações superficiais sem a devida incorporação representam um alto risco de "fuga". O protocolo deve certificar que a técnica de aplicação minimize a exposição do material ao transporte hídrico e eólico.
""")