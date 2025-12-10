import streamlit as st
import pandas as pd

# ------------------------------------------------------------
# ESTILO CUSTOMIZADO
# ------------------------------------------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.card {
    padding: 20px;
    background: #F7F9FC;
    border: 1px solid #E0E4EB;
    border-radius: 10px;
    margin-bottom: 20px;
}
.big-title {
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 10px;
    color: #1A365D;
}
.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 5px;
    color: #2D4A77;
}
.streamlit-expanderHeader {
    font-size: 18px !important;
    font-weight: 600 !important;
    color: #1A365D !important;
}
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# Conversão de densidade para kg/m³
# ------------------------------------------------------------
def converter_densidade_para_kgm3(valor, unidade):
    if unidade in ["Mg/m³", "g/cm³", "kg/dm³"]:
        return valor * 1000
    if unidade == "g/dm³":
        return valor
    return valor

# ------------------------------------------------------------
# Formatador com vírgula (GLOBAL)
# ------------------------------------------------------------
def fmt(x, casas=4):
    return f"{x:.{casas}f}".replace(".", ",")

# ------------------------------------------------------------
# Conjunto de cálculos principais
# ------------------------------------------------------------
def calcular_conversoes(kg_ha, prof, dens_solo, dens_bio):
    t_ha = kg_ha / 1000

    volume_solo = 10_000 * prof
    massa_solo = dens_solo * volume_solo

    frac_mm = kg_ha / massa_solo
    perc_mm = frac_mm * 100

    volume_bio = kg_ha / dens_bio
    frac_vv = volume_bio / volume_solo
    perc_vv = frac_vv * 100

    m_vol = kg_ha / volume_solo

    return {
        "t/ha": t_ha,
        "kg/ha": kg_ha,
        "massa/massa (%)": perc_mm,
        "massa/massa (fração)": frac_mm,
        "volume/volume (%)": perc_vv,
        "volume/volume (fração)": frac_vv,
        "massa/volume (kg/m³)": m_vol
    }

st.markdown("<div class='big-title'>Conversor Guiado de Quantidades de Biocarvão no Solo</div>", unsafe_allow_html=True)
st.write("Selecione a unidade de entrada e o sistema mostrará apenas as informações necessárias.")
st.markdown("---")

dens_unit_options = ["kg/m³", "Mg/m³", "g/cm³", "kg/dm³", "g/dm³"]

st.markdown("<div class='section-title'>📌 Unidade de entrada</div>", unsafe_allow_html=True)
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    unidade = st.selectbox(
        "Selecione sua unidade original:",
        ["t/ha", "kg/ha", "massa/massa (%)", "volume/volume (%)", "massa/volume"]
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# ENTRADAS E CÁLCULOS POR UNIDADE
# ============================================================

resultados = {}
unidade_mvol_usuario = None
valor_mvol_usuario = None

# ============================================================
# 1) ENTRADA EM t/ha
# ============================================================
if unidade == "t/ha":

    st.markdown("<div class='section-title'>🌱 Entrada em t/ha</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    t_ha = st.number_input("Valor em t/ha:", min_value=0.0, value=10.0)
    kg_ha = t_ha * 1000
    st.success(f"Convertido automaticamente para kg/ha: **{fmt(kg_ha,2)} kg/ha**")

    st.markdown("</div>", unsafe_allow_html=True)

    # parâmetros adicionais
    st.markdown("<div class='section-title'>⚙️ Parâmetros adicionais</div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            prof = st.number_input("Profundidade (m):", min_value=0.01, value=0.20)

        with col2:
            dens_solo_val = st.number_input("Densidade do solo:", min_value=0.0, value=1300.0)
            dens_solo_unit = st.selectbox("Unidade solo:", dens_unit_options, index=0)
            dens_solo = converter_densidade_para_kgm3(dens_solo_val, dens_solo_unit)

        with col3:
            dens_bio_val = st.number_input("Densidade do biocarvão:", min_value=0.0, value=250.0)
            dens_bio_unit = st.selectbox("Unidade biocarvão:", dens_unit_options, index=0)
            dens_bio = converter_densidade_para_kgm3(dens_bio_val, dens_bio_unit)

        st.caption(f"Densidade solo convertida: **{fmt(dens_solo,2)} kg/m³**")
        st.caption(f"Densidade biocarvão convertida: **{fmt(dens_bio,2)} kg/m³**")

        st.markdown("</div>", unsafe_allow_html=True)

    resultados = calcular_conversoes(kg_ha, prof, dens_solo, dens_bio)

elif unidade == "kg/ha":

    st.markdown("<div class='section-title'>⚖️ Entrada em kg/ha</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    kg_ha = st.number_input("Valor em kg/ha:", min_value=0.0, value=10000.0)
    t_ha = kg_ha / 1000
    st.success(f"Convertido automaticamente para t/ha: **{fmt(t_ha,4)} t/ha**")

    st.markdown("</div>", unsafe_allow_html=True)

    # parâmetros adicionais
    st.markdown("<div class='section-title'>⚙️ Parâmetros adicionais</div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            prof = st.number_input("Profundidade (m):", min_value=0.01, value=0.20)

        with col2:
            dens_solo_val = st.number_input("Densidade do solo:", min_value=0.0, value=1300.0)
            dens_solo_unit = st.selectbox("Unidade solo:", dens_unit_options, index=0)
            dens_solo = converter_densidade_para_kgm3(dens_solo_val, dens_solo_unit)

        with col3:
            dens_bio_val = st.number_input("Densidade do biocarvão:", min_value=0.0, value=250.0)
            dens_bio_unit = st.selectbox("Unidade biocarvão:", dens_unit_options, index=0)
            dens_bio = converter_densidade_para_kgm3(dens_bio_val, dens_bio_unit)

        st.caption(f"Densidade solo convertida: **{fmt(dens_solo,2)} kg/m³**")
        st.caption(f"Densidade biocarvão convertida: **{fmt(dens_bio,2)} kg/m³**")

        st.markdown("</div>", unsafe_allow_html=True)

    resultados = calcular_conversoes(kg_ha, prof, dens_solo, dens_bio)

elif unidade == "massa/massa (%)":

    st.markdown("<div class='section-title'>🧪 Entrada em massa/massa (%)</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    perc_mm = st.number_input("massa/massa (%) :", min_value=0.0, value=1.0)
    frac_mm = perc_mm / 100

    st.markdown("</div>", unsafe_allow_html=True)

    # parâmetros
    st.markdown("<div class='section-title'>⚙️ Parâmetros adicionais</div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            prof = st.number_input("Profundidade (m):", min_value=0.01, value=0.20)

        with col2:
            dens_solo_val = st.number_input("Densidade do solo:", min_value=0.0, value=1300.0)
            dens_solo_unit = st.selectbox("Unidade solo:", dens_unit_options, index=0)
            dens_solo = converter_densidade_para_kgm3(dens_solo_val, dens_solo_unit)

        st.caption(f"Densidade solo convertida: **{fmt(dens_solo,2)} kg/m³**")
        st.markdown("</div>", unsafe_allow_html=True)

    massa_solo_ha = dens_solo * 10_000 * prof
    kg_ha = frac_mm * massa_solo_ha
    t_ha = kg_ha / 1000

    st.success(f"Isso equivale a **{fmt(kg_ha,2)} kg/ha**")

    # precisa densidade do bio para v/v
    dens_bio_val = st.number_input("Densidade do biocarvão:", min_value=0.0, value=250.0)
    dens_bio_unit = st.selectbox("Unidade biocarvão:", dens_unit_options, index=0)
    dens_bio = converter_densidade_para_kgm3(dens_bio_val, dens_bio_unit)
    st.caption(f"Densidade biocarvão convertida: **{fmt(dens_bio,2)} kg/m³**")

    resultados = calcular_conversoes(kg_ha, prof, dens_solo, dens_bio)

elif unidade == "volume/volume (%)":

    st.markdown("<div class='section-title'>🔳 Entrada em volume/volume (%)</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    perc_vv = st.number_input("volume/volume (%) :", min_value=0.0, value=2.0)
    frac_vv = perc_vv / 100

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>⚙️ Parâmetros adicionais</div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            prof = st.number_input("Profundidade (m):", min_value=0.01, value=0.20)

        with col2:
            dens_bio_val = st.number_input("Densidade do biocarvão:", min_value=0.0, value=250.0)
            dens_bio_unit = st.selectbox("Unidade biocarvão:", dens_unit_options, index=0)
            dens_bio = converter_densidade_para_kgm3(dens_bio_val, dens_bio_unit)

        st.caption(f"Densidade biocarvão convertida: **{fmt(dens_bio,2)} kg/m³**")
        st.markdown("</div>", unsafe_allow_html=True)

    volume_solo_ha = 10_000 * prof
    volume_bio = frac_vv * volume_solo_ha

    kg_ha = volume_bio * dens_bio
    t_ha = kg_ha / 1000

    st.success(f"Isso equivale a **{fmt(kg_ha,2)} kg/ha**")

    # agora densidade do solo
    dens_solo_val = st.number_input("Densidade do solo:", min_value=0.0, value=1300.0)
    dens_solo_unit = st.selectbox("Unidade solo:", dens_unit_options, index=0)
    dens_solo = converter_densidade_para_kgm3(dens_solo_val, dens_solo_unit)

    st.caption(f"Densidade solo convertida: **{fmt(dens_solo,2)} kg/m³**")

    resultados = calcular_conversoes(kg_ha, prof, dens_solo, dens_bio)

elif unidade == "massa/volume":

    st.markdown("<div class='section-title'>🧯 Entrada em massa/volume</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    colA, colB = st.columns(2)

    with colA:
        mvol_val = st.number_input("massa/volume:", min_value=0.0, value=1.0)

    with colB:
        mvol_unit = st.selectbox("Unidade m/v:", dens_unit_options, index=0)

    mvol_kgm3 = converter_densidade_para_kgm3(mvol_val, mvol_unit)

    unidade_mvol_usuario = mvol_unit   # salva unidade original
    valor_mvol_usuario = mvol_val      # salva valor na unidade original

    st.caption(f"Massa/volume convertida: **{fmt(mvol_kgm3,4)} kg/m³**")
    st.markdown("</div>", unsafe_allow_html=True)

    # parâmetros
    st.markdown("<div class='section-title'>⚙️ Parâmetros adicionais</div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            prof = st.number_input("Profundidade (m):", min_value=0.01, value=0.20)

        with col2:
            dens_solo_val = st.number_input("Densidade do solo:", min_value=0.0, value=1300.0)
            dens_solo_unit = st.selectbox("Unidade solo:", dens_unit_options, index=0)
            dens_solo = converter_densidade_para_kgm3(dens_solo_val, dens_solo_unit)

        with col3:
            dens_bio_val = st.number_input("Densidade do biocarvão:", min_value=0.0, value=250.0)
            dens_bio_unit = st.selectbox("Unidade biocarvão:", dens_unit_options, index=0)
            dens_bio = converter_densidade_para_kgm3(dens_bio_val, dens_bio_unit)

        st.caption(f"Densidade solo convertida: **{fmt(dens_solo,2)} kg/m³**")
        st.caption(f"Densidade biocarvão convertida: **{fmt(dens_bio,2)} kg/m³**")

        st.markdown("</div>", unsafe_allow_html=True)

    volume_solo_ha = 10_000 * prof
    kg_ha = mvol_kgm3 * volume_solo_ha
    t_ha = kg_ha / 1000

    st.success(f"Isso equivale a **{fmt(kg_ha,2)} kg/ha**")

    resultados = calcular_conversoes(kg_ha, prof, dens_solo, dens_bio)

# ============================================================
# 📊 TABELA FINAL
# ============================================================

# Se a unidade original foi massa/volume, adiciona também a unidade original do usuário
if unidade == "massa/volume" and unidade_mvol_usuario is not None:
    resultados[f"massa/volume ({unidade_mvol_usuario})"] = valor_mvol_usuario

st.markdown("<div class='section-title'>📊 Resultados das Conversões</div>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)

# Monta tabela com valores formatados como texto usando vírgula
linhas = []
for nome_unidade, valor in resultados.items():
    # formata com vírgula e 6 casas para manter boa precisão visual
    linhas.append({
        "Unidade": nome_unidade,
        "Valor": fmt(valor, 6)
    })

df = pd.DataFrame(linhas)
st.dataframe(df, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# 📘 EXPANDER DINÂMICO (CÁLCULOS DETALHADOS)
# ============================================================
with st.expander("📘 Mostrar cálculos detalhados das conversões"):

    st.header("Cálculos realizados")

    # Valores base (reutilizados)
    volume_solo = 10_000 * prof                      # m³
    massa_solo = dens_solo * volume_solo             # kg
    frac_vv = resultados["volume/volume (fração)"]
    perc_vv = resultados["volume/volume (%)"]
    frac_mm_res = resultados["massa/massa (fração)"]
    perc_mm_res = resultados["massa/massa (%)"]
    mvol_res = resultados["massa/volume (kg/m³)"]

    # ============================================================
    # ENTRADA ORIGINAL EM t/ha
    # ============================================================
    if unidade == "t/ha":

        st.subheader("1) Conversão t/ha → kg/ha")
        st.latex(r"kg/ha = t/ha \times 1000")
        st.latex(
            fr"kg/ha = {fmt(t_ha,4)} \times 1000 = {fmt(kg_ha,2)}\ \text{{kg/ha}}"
        )

        st.divider()

        st.subheader("2) Volume de solo na camada considerada")
        st.latex(r"V_{solo} = 10\,000 \times profundidade")
        st.latex(
            fr"V_{{solo}} = 10\,000 \times {fmt(prof,2)} = {fmt(volume_solo,2)}\ \text{{m³}}"
        )

        st.divider()

        st.subheader("3) Massa total de solo")
        st.latex(r"M_{solo} = \rho_{solo} \times V_{solo}")
        st.latex(
            fr"M_{{solo}} = {fmt(dens_solo,2)}\ \text{{kg/m³}} \times {fmt(volume_solo,2)}\ \text{{m³}}"
            fr" = {fmt(massa_solo,2)}\ \text{{kg}}"
        )

        st.divider()

        st.subheader("4) Massa/massa")
        st.latex(r"\text{fração massa/massa} = \frac{kg/ha}{M_{solo}}")
        st.latex(
            fr"\frac{{{fmt(kg_ha,2)}\ \text{{kg}}}}{{{fmt(massa_solo,2)}\ \text{{kg}}}}"
            fr" = {fmt(frac_mm_res,6)}"
        )
        st.latex(r"\text{massa/massa (\%)} = \text{fração massa/massa} \times 100")
        st.latex(
            fr"{fmt(frac_mm_res,6)} \times 100 = {fmt(perc_mm_res,4)}\ \%"
        )

        st.divider()

        st.subheader("5) Volume/volume")
        volume_bio = kg_ha / dens_bio
        st.latex(r"V_{bio} = \frac{kg/ha}{\rho_{bio}}")
        st.latex(
            fr"V_{{bio}} = \frac{{{fmt(kg_ha,2)}\ \text{{kg}}}}{{{fmt(dens_bio,2)}\ \text{{kg/m³}}}}"
            fr" = {fmt(volume_bio,4)}\ \text{{m³}}"
        )

        st.latex(r"\text{fração v/v} = \frac{V_{bio}}{V_{solo}}")
        st.latex(
            fr"\frac{{{fmt(volume_bio,4)}\ \text{{m³}}}}{{{fmt(volume_solo,2)}\ \text{{m³}}}}"
            fr" = {fmt(frac_vv,6)}"
        )

        st.latex(r"\text{v/v (\%)} = \text{fração v/v} \times 100")
        st.latex(
            fr"{fmt(frac_vv,6)} \times 100 = {fmt(perc_vv,4)}\ \%"
        )

        st.divider()

        st.subheader("6) Massa/volume")
        st.latex(r"\text{massa/volume} = \frac{kg/ha}{V_{solo}}")
        st.latex(
            fr"\frac{{{fmt(kg_ha,2)}\ \text{{kg/ha}}}}{{{fmt(volume_solo,2)}\ \text{{m³/ha}}}}"
            fr" = {fmt(mvol_res,4)}\ \text{{kg/m³}}"
        )

    # ============================================================
    # ENTRADA ORIGINAL EM kg/ha
    # ============================================================
    elif unidade == "kg/ha":

        st.subheader("1) Conversão kg/ha → t/ha")
        st.latex(r"t/ha = \frac{kg/ha}{1000}")
        st.latex(
            fr"t/ha = \frac{{{fmt(kg_ha,2)}}}{1000} = {fmt(t_ha,4)}"
        )

        st.divider()

        st.subheader("2) Volume de solo na camada considerada")
        st.latex(r"V_{solo} = 10\,000 \times profundidade")
        st.latex(
            fr"V_{{solo}} = 10\,000 \times {fmt(prof,2)} = {fmt(volume_solo,2)}\ \text{{m³}}"
        )

        st.divider()

        st.subheader("3) Massa total de solo")
        st.latex(r"M_{solo} = \rho_{solo} \times V_{solo}")
        st.latex(
            fr"M_{{solo}} = {fmt(dens_solo,2)}\ \text{{kg/m³}} \times {fmt(volume_solo,2)}\ \text{{m³}}"
            fr" = {fmt(massa_solo,2)}\ \text{{kg}}"
        )

        st.divider()

        st.subheader("4) Massa/massa")
        st.latex(r"\text{fração massa/massa} = \frac{kg/ha}{M_{solo}}")
        st.latex(
            fr"\frac{{{fmt(kg_ha,2)}\ \text{{kg}}}}{{{fmt(massa_solo,2)}\ \text{{kg}}}}"
            fr" = {fmt(frac_mm_res,6)}"
        )
        st.latex(r"\text{massa/massa (\%)} = \text{fração massa/massa} \times 100")
        st.latex(
            fr"{fmt(frac_mm_res,6)} \times 100 = {fmt(perc_mm_res,4)}\ \%"
        )

        st.divider()

        st.subheader("5) Volume/volume")
        volume_bio = kg_ha / dens_bio
        st.latex(r"V_{bio} = \frac{kg/ha}{\rho_{bio}}")
        st.latex(
            fr"V_{{bio}} = \frac{{{fmt(kg_ha,2)}\ \text{{kg}}}}{{{fmt(dens_bio,2)}\ \text{{kg/m³}}}}"
            fr" = {fmt(volume_bio,4)}\ \text{{m³}}"
        )

        st.latex(r"\text{fração v/v} = \frac{V_{bio}}{V_{solo}}")
        st.latex(
            fr"\frac{{{fmt(volume_bio,4)}\ \text{{m³}}}}{{{fmt(volume_solo,2)}\ \text{{m³}}}}"
            fr" = {fmt(frac_vv,6)}"
        )

        st.latex(r"\text{v/v (\%)} = \text{fração v/v} \times 100")
        st.latex(
            fr"{fmt(frac_vv,6)} \times 100 = {fmt(perc_vv,4)}\ \%"
        )

        st.divider()

        st.subheader("6) Massa/volume")
        st.latex(r"\text{massa/volume} = \frac{kg/ha}{V_{solo}}")
        st.latex(
            fr"\frac{{{fmt(kg_ha,2)}\ \text{{kg/ha}}}}{{{fmt(volume_solo,2)}\ \text{{m³/ha}}}}"
            fr" = {fmt(mvol_res,4)}\ \text{{kg/m³}}"
        )

    # ============================================================
    # ENTRADA ORIGINAL EM massa/massa (%)
    # ============================================================
    elif unidade == "massa/massa (%)":

        st.subheader("1) massa/massa (%) → fração e kg/ha")
        st.latex(r"\text{fração} = \frac{\text{massa/massa (\%)}}{100}")
        st.latex(
            fr"\text{{fração}} = \frac{{{fmt(perc_mm_res,4)}\ \%}}{{100}}"
            fr" = {fmt(frac_mm_res,6)}"
        )
        st.latex(r"kg/ha = \text{fração} \times M_{solo}")
        st.latex(
            fr"{fmt(frac_mm_res,6)} \times {fmt(massa_solo,2)}\ \text{{kg}}"
            fr" = {fmt(kg_ha,2)}\ \text{{kg/ha}}"
        )

        st.divider()

        st.subheader("2) kg/ha → t/ha")
        st.latex(r"t/ha = \frac{kg/ha}{1000}")
        st.latex(
            fr"t/ha = \frac{{{fmt(kg_ha,2)}}}{1000} = {fmt(t_ha,4)}"
        )

        st.divider()

        st.subheader("3) Volume de solo")
        st.latex(r"V_{solo} = 10\,000 \times profundidade")
        st.latex(
            fr"V_{{solo}} = 10\,000 \times {fmt(prof,2)}"
            fr" = {fmt(volume_solo,2)}\ \text{{m³}}"
        )

        st.divider()

        st.subheader("4) Volume/volume")
        volume_bio = kg_ha / dens_bio
        st.latex(r"V_{bio} = \frac{kg/ha}{\rho_{bio}}")
        st.latex(
            fr"V_{{bio}} = \frac{{{fmt(kg_ha,2)}\ \text{{kg}}}}{{{fmt(dens_bio,2)}\ \text{{kg/m³}}}}"
            fr" = {fmt(volume_bio,4)}\ \text{{m³}}"
        )
        st.latex(r"\text{fração v/v} = \frac{V_{bio}}{V_{solo}}")
        st.latex(
            fr"\frac{{{fmt(volume_bio,4)}\ \text{{m³}}}}{{{fmt(volume_solo,2)}\ \text{{m³}}}}"
            fr" = {fmt(frac_vv,6)}"
        )
        st.latex(r"\text{v/v (\%)} = \text{fração v/v} \times 100")
        st.latex(
            fr"{fmt(frac_vv,6)} \times 100 = {fmt(perc_vv,4)}\ \%"
        )

        st.divider()

        st.subheader("5) Massa/volume")
        st.latex(r"\text{massa/volume} = \frac{kg/ha}{V_{solo}}")
        st.latex(
            fr"\frac{{{fmt(kg_ha,2)}\ \text{{kg/ha}}}}{{{fmt(volume_solo,2)}\ \text{{m³/ha}}}}"
            fr" = {fmt(mvol_res,4)}\ \text{{kg/m³}}"
        )

    # ============================================================
    # ENTRADA ORIGINAL EM volume/volume (%)
    # ============================================================
    elif unidade == "volume/volume (%)":

        st.subheader("1) v/v (%) → fração e kg/ha")
        st.latex(r"\text{fração v/v} = \frac{\text{v/v (\%)}}{100}")
        st.latex(
            fr"\text{{fração v/v}} = \frac{{{fmt(perc_vv,4)}\ \%}}{{100}}"
            fr" = {fmt(frac_vv,6)}"
        )
        st.latex(r"kg/ha = \text{fração v/v} \times V_{solo} \times \rho_{bio}")
        st.latex(
            fr"{fmt(frac_vv,6)} \times {fmt(volume_solo,2)}\ \text{{m³}}"
            fr" \times {fmt(dens_bio,2)}\ \text{{kg/m³}}"
            fr" = {fmt(kg_ha,2)}\ \text{{kg/ha}}"
        )

        st.divider()

        st.subheader("2) kg/ha → t/ha")
        st.latex(r"t/ha = \frac{kg/ha}{1000}")
        st.latex(
            fr"t/ha = \frac{{{fmt(kg_ha,2)}}}{1000} = {fmt(t_ha,4)}"
        )

        st.divider()

        st.subheader("3) Volume de solo")
        st.latex(r"V_{solo} = 10\,000 \times profundidade")
        st.latex(
            fr"V_{{solo}} = 10\,000 \times {fmt(prof,2)}"
            fr" = {fmt(volume_solo,2)}\ \text{{m³}}"
        )

        st.divider()

        st.subheader("4) Massa/massa")
        st.latex(r"\text{fração massa/massa} = \frac{kg/ha}{M_{solo}}")
        st.latex(
            fr"\frac{{{fmt(kg_ha,2)}\ \text{{kg}}}}{{{fmt(massa_solo,2)}\ \text{{kg}}}}"
            fr" = {fmt(frac_mm_res,6)}"
        )
        st.latex(r"\text{massa/massa (\%)} = \text{fração massa/massa} \times 100")
        st.latex(
            fr"{fmt(frac_mm_res,6)} \times 100 = {fmt(perc_mm_res,4)}\ \%"
        )

        st.divider()

        st.subheader("5) Massa/volume")
        st.latex(r"\text{massa/volume} = \frac{kg/ha}{V_{solo}}")
        st.latex(
            fr"\frac{{{fmt(kg_ha,2)}\ \text{{kg/ha}}}}{{{fmt(volume_solo,2)}\ \text{{m³/ha}}}}"
            fr" = {fmt(mvol_res,4)}\ \text{{kg/m³}}"
        )

    # ============================================================
    # ENTRADA ORIGINAL EM massa/volume
    # ============================================================
    elif unidade == "massa/volume":

        st.subheader("1) massa/volume → kg/ha")
        st.latex(r"kg/ha = \text{massa/volume} \times V_{solo}")
        st.latex(
            fr"kg/ha = {fmt(mvol_res,4)}\ \text{{kg/m³}}"
            fr" \times {fmt(volume_solo,2)}\ \text{{m³/ha}}"
            fr" = {fmt(kg_ha,2)}\ \text{{kg/ha}}"
        )

        st.divider()

        st.subheader("2) kg/ha → t/ha")
        st.latex(r"t/ha = \frac{kg/ha}{1000}")
        st.latex(
            fr"t/ha = \frac{{{fmt(kg_ha,2)}}}{1000} = {fmt(t_ha,4)}"
        )

        st.divider()

        st.subheader("3) Volume de solo")
        st.latex(r"V_{solo} = 10\,000 \times profundidade")
        st.latex(
            fr"V_{{solo}} = 10\,000 \times {fmt(prof,2)}"
            fr" = {fmt(volume_solo,2)}\ \text{{m³}}"
        )

        st.divider()

        st.subheader("4) Massa/massa")
        st.latex(r"\text{fração massa/massa} = \frac{kg/ha}{M_{solo}}")
        st.latex(
            fr"\frac{{{fmt(kg_ha,2)}\ \text{{kg}}}}{{{fmt(massa_solo,2)}\ \text{{kg}}}}"
            fr" = {fmt(frac_mm_res,6)}"
        )
        st.latex(r"\text{massa/massa (\%)} = \text{fração massa/massa} \times 100")
        st.latex(
            fr"{fmt(frac_mm_res,6)} \times 100 = {fmt(perc_mm_res,4)}\ \%"
        )

        st.divider()

        st.subheader("5) Volume/volume")
        volume_bio = kg_ha / dens_bio
        st.latex(r"V_{bio} = \frac{kg/ha}{\rho_{bio}}")
        st.latex(
            fr"V_{{bio}} = \frac{{{fmt(kg_ha,2)}\ \text{{kg}}}}{{{fmt(dens_bio,2)}\ \text{{kg/m³}}}}"
            fr" = {fmt(volume_bio,4)}\ \text{{m³}}"
        )
        st.latex(r"\text{fração v/v} = \frac{V_{bio}}{V_{solo}}")
        st.latex(
            fr"\frac{{{fmt(volume_bio,4)}\ \text{{m³}}}}{{{fmt(volume_solo,2)}\ \text{{m³}}}}"
            fr" = {fmt(frac_vv,6)}"
        )
        st.latex(r"\text{v/v (\%)} = \text{fração v/v} \times 100")
        st.latex(
            fr"{fmt(frac_vv,6)} \times 100 = {fmt(perc_vv,4)}\ \%"
        )
