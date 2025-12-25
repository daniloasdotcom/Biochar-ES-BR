import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# --- Dicionário de Dados do Artigo (Gaurav et al., 2025) ---
DATA_MAP = {
    "T1 (Controle)": {
        "biochar_depth": 0,
        "root_length_pct": 1.00,
        "root_angle": 56.7,
        "root_volume_pct": 1.00,
        "desc": "Solo sem tratamento. Raízes mais curtas e espalhadas lateralmente."
    },
    "T2 (Biochar 0-5cm) 1,0 g/dm³": {
        "biochar_depth": 5,
        "root_length_pct": 1.12,
        "root_angle": 50.8,
        "root_volume_pct": 1.13,
        "desc": "Alta concentração de Biochar em camada fina. Leve melhoria."
    },
    "T3 (Biochar 0-10cm) 0,5 g/dm³": {
        "biochar_depth": 10,
        "root_length_pct": 1.24,
        "root_angle": 47.4,
        "root_volume_pct": 1.26,
        "desc": "Biochar em profundidade média."
    },
    "T4 (Biochar 0-15cm) 0,33 g/dm³": {
        "biochar_depth": 15,
        "root_length_pct": 1.40,
        "root_angle": 40.8,
        "root_volume_pct": 1.41,
        "desc": "Biochar profundo, mas mais diluído. Raízes longas."
    },
    "T5 (Biochar 0-20cm) 0,25 g/dm³": {
        "biochar_depth": 20,
        "root_length_pct": 1.48,
        "root_angle": 39.0,
        "root_volume_pct": 1.42,
        "desc": "Melhor resultado. Biochar muito diluído, mas em grande volume de solo."
    }
}

def gerar_perfil_raiz(length_factor, angle_degrees, steps=100):
    # Profundidade base de 18 cm para caber na escala de 30cm
    base_depth = 18
    max_depth = base_depth * length_factor
    
    y = np.linspace(0, -max_depth, steps)
    
    # O ângulo define o "Cone" de espalhamento.
    spread_factor = np.tan(np.radians(angle_degrees)) * 0.5
    
    x = [0]
    current_x = 0
    for _ in range(steps - 1):
        desvio = np.random.normal(0, spread_factor)
        current_x += desvio
        x.append(current_x)
        
    return np.array(x), y

# --- Interface Streamlit ---
st.set_page_config(page_title="Simulação Biochar Maize (Caule Melhorado)", layout="wide")

st.title("🌽 Simulação de Raízes: Visualização de Caule Melhorada")
st.markdown("""
Visualização em escala de 30 cm com representação aprimorada do caule do milho.
""")

col_controls, col_graph = st.columns([1, 3])

with col_controls:
    st.subheader("Tratamento")
    treatment = st.radio("Nível de Aplicação:", list(DATA_MAP.keys()))
    data = DATA_MAP[treatment]
    
    st.info(data["desc"])
    
    st.markdown("### Dados Físicos:")
    st.metric("Zona de Aplicação", f"0 - {data['biochar_depth']} cm")
    st.metric("Ângulo de Crescimento", f"{data['root_angle']}°")
    
    if data['biochar_depth'] > 0:
        densidade_relativa = 100 / (data['biochar_depth'] / 5)
        st.metric("Densidade Estimada", f"{densidade_relativa:.0f}% (ref. T2)")

with col_graph:
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Cor do solo
    ax.set_facecolor("#5D4037") 
    
    # Fundo Branco acima de zero (Ar)
    air_rect = patches.Rectangle((-25, 0), 50, 6, linewidth=0, facecolor='#E3F2FD', zorder=1) # Um azul céu muito claro
    ax.add_patch(air_rect)

    np.random.seed(42) 

    # --- Biochar ---
    FIXED_PARTICLE_COUNT = 400 

    if data['biochar_depth'] > 0:
        depth_limit = -data['biochar_depth']
        biochar_x = np.random.uniform(-20, 20, FIXED_PARTICLE_COUNT)
        biochar_y = np.random.uniform(0, depth_limit, FIXED_PARTICLE_COUNT)
        
        ax.scatter(biochar_x, biochar_y, color='black', s=8, alpha=0.7, zorder=2)
        ax.axhline(depth_limit, color='black', linestyle=':', alpha=0.4, linewidth=1, zorder=2)
        ax.text(-19, depth_limit + 0.5, f"Limite ({data['biochar_depth']}cm)", color='white', fontsize=9, zorder=3)

    # --- Raízes ---
    num_roots = int(40 * data['root_volume_pct'])
    for i in range(num_roots):
        var_length = data['root_length_pct'] * np.random.uniform(0.9, 1.1)
        rx, ry = gerar_perfil_raiz(var_length, data['root_angle'])
        ax.plot(rx, ry, color="#FFEE58", alpha=0.6, linewidth=1.5, zorder=3)

    # --- Estética Final & CAULE MELHORADO ---
    
    # Linha do solo
    ax.axhline(0, color='#3E2723', linewidth=2, zorder=4)
    
    # === DESENHO DO CAULE ESTILIZADO ===
    stalk_center_x = 0
    stalk_height = 4.8
    
    # 1. Camada base do caule (verde escuro, mais grosso)
    ax.plot([stalk_center_x, stalk_center_x], [-0.2, stalk_height], 
             color='#2E7D32', linewidth=8, zorder=5, solid_capstyle='butt')
    
    # 2. Camada de "luz" central (verde mais claro, mais fino para dar volume)
    ax.plot([stalk_center_x, stalk_center_x], [0, stalk_height-0.1], 
             color='#66BB6A', linewidth=4, zorder=6, solid_capstyle='round')
    
    # 3. Adicionando "nós" (segmentação do caule)
    # Desenhamos pequenas linhas horizontais escuras para simular os nós do milho
    nodes_y = [1.5, 3.0] # Alturas onde os nós aparecem
    for node_y in nodes_y:
        ax.plot([-0.5, 0.5], [node_y, node_y], 
                 color='#1B5E20', linewidth=2.5, zorder=7)
        
    # ===================================
    
    # Ajustes de Eixos (Escala 30cm)
    ax.set_ylim(-30, 6)
    ax.set_xlim(-20, 20)
    
    ax.set_ylabel("Profundidade (cm)", fontsize=12, color='#3E2723')
    ax.set_xlabel("Distância Lateral (cm)", fontsize=12, color='#3E2723')
    
    # Grid e Borda
    ax.grid(True, which='major', axis='y', linestyle='--', alpha=0.3, color='white', zorder=2)
    for spine in ax.spines.values():
        spine.set_visible(False) # Remove todas as bordas quadradas
        
    # Recoloca apenas a espinha da esquerda (eixo Y) de forma mais sutil
    ax.spines['left'].set_visible(True)
    ax.spines['left'].set_color('#3E2723')
    ax.tick_params(axis='x', colors='#3E2723')
    ax.tick_params(axis='y', colors='#3E2723')
    
    st.pyplot(fig)