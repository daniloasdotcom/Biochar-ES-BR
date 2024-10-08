import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Função para gerar o gráfico de K e K2O por tonelada de biocarvão
def plot_k_and_k2o_levels(dose, k_levels):
    k_per_b1 = dose * k_levels[0]  # Para o biocarvão palha de Café 350º
    k_per_b2 = dose * k_levels[1]  # Para o biocarvão palha de Café 600º
    k_per_b3 = dose * k_levels[2]  # Para o biocarvão Casca de Eucalipto 350º
    k_per_b4 = dose * k_levels[3]  # Para o biocarvão Casca de Eucalipto 600º

    # Conversão de K para K2O
    k2o_per_b1 = k_per_b1 * 1.205
    k2o_per_b2 = k_per_b2 * 1.205
    k2o_per_b3 = k_per_b3 * 1.205
    k2o_per_b4 = k_per_b4 * 1.205

    biocarvoes = ['PC350ºC', 'PC600ºC', 'CE350ºC', 'CE600ºC']
    values_k = [k_per_b1, k_per_b2, k_per_b3, k_per_b4]
    values_k2o = [k2o_per_b1, k2o_per_b2, k2o_per_b3, k2o_per_b4]

    # Gráfico de K
    fig_k, ax_k = plt.subplots(figsize=(6, 4))
    ax_k.bar(biocarvoes, values_k, color='#3498DB', edgecolor='black', linewidth=1.2)
    ax_k.set_ylabel('Quantidade de Potássio (K) (kg)', fontsize=14, weight='bold', color='#333333')
    ax_k.set_xlabel('Tipo de Biocarvão', fontsize=14, weight='bold', color='#333333')
    ax_k.set_ylim(0, 300)  # Limite fixo de 300 para K
    ax_k.set_title('Quantidade de Potássio (K)\n(Dose: {} t)'.format(dose), fontsize=16, weight='bold', color='#333333',
                   pad=20)
    ax_k.spines['right'].set_visible(False)
    ax_k.spines['top'].set_visible(False)
    for i, v in enumerate(values_k):
        ax_k.text(i, v + 5, f'{v:.2f}', ha='center', fontsize=12, color='#555555')

    # Gráfico de K2O
    fig_k2o, ax_k2o = plt.subplots(figsize=(6, 4))
    ax_k2o.bar(biocarvoes, values_k2o, color='#1ABC9C', edgecolor='black', linewidth=1.2)
    ax_k2o.set_ylabel('Quantidade de K₂O (kg)', fontsize=14, weight='bold', color='#333333')
    ax_k2o.set_xlabel('Tipo de Biocarvão', fontsize=14, weight='bold', color='#333333')
    ax_k2o.set_ylim(0, 400)  # Limite fixo de 400 para K2O
    ax_k2o.set_title('Quantidade de K₂O\n(Dose: {} t)'.format(dose), fontsize=16, weight='bold', color='#333333',
                     pad=20)
    ax_k2o.spines['right'].set_visible(False)
    ax_k2o.spines['top'].set_visible(False)
    for i, v in enumerate(values_k2o):
        ax_k2o.text(i, v + 5, f'{v:.2f}', ha='center', fontsize=12, color='#555555')

    return fig_k, fig_k2o


# Função para gerar o gráfico 3D de colunas representando o volume da cova de plantio
def plot_3d_volume(profundidade, largura, comprimento):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Definir a posição da barra 3D
    x = [0]  # Posição X inicial
    y = [0]  # Posição Y inicial
    z = [0]  # Posição Z inicial
    dx = [largura]  # Largura da barra
    dy = [comprimento]  # Comprimento da barra
    dz = [profundidade]  # Altura da barra

    # Criar a barra 3D com cor marrom
    ax.bar3d(x, y, z, dx, dy, dz, color='brown', alpha=0.7)

    # Ajustar os rótulos dos eixos com labelpad mais curto para aproximar
    ax.set_xlabel('Largura (cm)', labelpad=5)
    ax.set_ylabel('Comprimento (cm)', labelpad=5)
    ax.set_zlabel('Profundidade (cm)', labelpad=5)

    # Ajustar as margens do gráfico para garantir que os rótulos fiquem visíveis
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    ax.set_title('Volume da Cova de Plantio', fontsize=14, weight='bold')

    return fig


# Função para gerar o gráfico 3D do volume com pontos representando biocarvão
def plot_3d_biocarvao_with_points(profundidade, largura, comprimento, dose_por_cova):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Cada ponto preto representa 1 grama de biocarvão com 2 cm³
    volume_por_ponto = 2  # cm³ por ponto
    num_points = int(dose_por_cova)  # Número de pontos (1 ponto = 1 grama de biocarvão)

    # Calcular número de pontos baseado no volume da cova e volume ocupado por ponto
    total_volume_cova_cm3 = profundidade * largura * comprimento  # Volume total em cm³
    pontos_por_cova = min(num_points, total_volume_cova_cm3 // volume_por_ponto)  # Limitar ao volume da cova

    # Distribuir pontos uniformemente dentro da cova
    x_points = np.random.uniform(0, largura, int(pontos_por_cova))
    y_points = np.random.uniform(0, comprimento, int(pontos_por_cova))
    z_points = np.random.uniform(0, profundidade, int(pontos_por_cova))

    # Aumentar o tamanho dos pontos para 50 e aplicar arestas visíveis
    ax.scatter(x_points, y_points, z_points, color='black', edgecolors='white', s=50)  # s=50 aumenta o tamanho dos pontos

    # Ajustar os rótulos dos eixos com labelpad mais curto para aproximar
    ax.set_xlabel('Largura (cm)', labelpad=5)
    ax.set_ylabel('Comprimento (cm)', labelpad=5)
    ax.set_zlabel('Profundidade (cm)', labelpad=5)

    # Ajustar as margens do gráfico para garantir que os rótulos fiquem visíveis
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    ax.set_title(f'Distribuição de biocarvões\nna Cova com {int(pontos_por_cova)}g de Biocarvão', fontsize=14, weight='bold')

    return fig


# Função do gráfico de potássio
def grafico_potassio():
    # Adicionar um botão para voltar à página do blog
    if st.button("Voltar para o Blog"):
        # Alterar o estado da página para "blog"
        st.session_state['page'] = 'blog'

    st.title("Impacto do Biocarvão no Teor de Potássio (K) por Dose Aplicada")

    st.write("""
        Aqui estão detalhes sobre a quantidade de potássio e K₂O nos diferentes tipos de biocarvão, 
        com base na dose selecionada (em toneladas). Ajuste a dose e veja o impacto!
    """)

    # Dados de teores de potássio para os biocarvões
    biocarvoes_data = {
        "Biocarvão": ['Palha de Café', 'Palha de Café', 'Casca de Eucalipto', 'Casca de Eucalipto'],
        "Temperatura": ['350ºC', '600ºC', '350ºC', '600ºC'],
        "Teor de K (g/kg)": [4.457, 5.657, 0.566, 0.701]
    }

    # Criar dataframe
    df = pd.DataFrame(biocarvoes_data)

    # Exibir a tabela centralizada com o CSS definido
    st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)

    # Exibir gráficos de K e K2O em colunas
    col_k, col_k2o = st.columns(2)

    dose = st.slider('Selecione a quantidade de biocarvão (t)', 0, 50, 1)
    k_levels = [4.457, 5.657, 0.566, 0.701]  # Correspondente a B1, B2, B3, B4
    fig_k, fig_k2o = plot_k_and_k2o_levels(dose, k_levels)

    # Exibir os gráficos 2D de K e K2O em colunas
    with col_k:
        st.pyplot(fig_k)
    with col_k2o:
        st.pyplot(fig_k2o)

    # Organizar entrada e saída dos gráficos 3D em três colunas
    col_input, col_volume, col_biocarvao = st.columns(3)

    with col_input:
        # Caixa de entrada para Profundidade, Largura e Comprimento
        st.subheader("Dimensões da cova de plantio")
        profundidade = st.number_input("Profundidade (cm)", min_value=1, value=40)
        largura = st.number_input("Largura (cm)", min_value=1, value=40)
        comprimento = st.number_input("Comprimento (cm)", min_value=1, value=40)

    # Calcular volume da cova (P x L x C)
    volume_cova = (profundidade * largura * comprimento) / 1000  # Convertido para dm³
    dose_por_cova = ((dose * volume_cova) / 2_000_000) * 1000000  # Convertido para gramas

    with col_volume:
        # Exibir gráfico 3D de colunas do volume da cova
        fig_volume = plot_3d_volume(profundidade, largura, comprimento)
        st.pyplot(fig_volume)

        # Adicionar texto centralizado informando o volume da cova
        st.markdown(f"<div style='text-align: center;'><strong>Volume da cova:</strong> {volume_cova:.2f} dm³</div>", unsafe_allow_html=True)

    with col_biocarvao:
        # Exibir gráfico 3D com pontos pretos representando biocarvão
        fig_biocarvao = plot_3d_biocarvao_with_points(profundidade, largura, comprimento, dose_por_cova)
        st.pyplot(fig_biocarvao)

        # Adicionar texto centralizado informando a quantidade de biocarvão por cova
        st.markdown(f"<div style='text-align: center;'><strong>Quantidade de biocarvão por cova:</strong> {dose_por_cova:.2f} g</div>", unsafe_allow_html=True)


# Executar a função de exibição
grafico_potassio()

