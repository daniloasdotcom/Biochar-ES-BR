import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pages.others.sidebar_utils import configure_sidebar


# Função para gerar o gráfico de K e K2O por tonelada de biocarvão
def plot_k_k2o_and_ca_levels(dose, k_levels, ca_levels):
    # Cálculos para Potássio
    k_per_b1 = dose * k_levels[0]  # Para o biocarvão palha de Café 350º
    k_per_b2 = dose * k_levels[1]  # Para o biocarvão palha de Café 600º
    k_per_b3 = dose * k_levels[2]  # Para o biocarvão Casca de Eucalipto 350º
    k_per_b4 = dose * k_levels[3]  # Para o biocarvão Casca de Eucalipto 600º

    # Conversão de K para K2O
    k2o_per_b1 = k_per_b1 * 1.205
    k2o_per_b2 = k_per_b2 * 1.205
    k2o_per_b3 = k_per_b3 * 1.205
    k2o_per_b4 = k_per_b4 * 1.205

    # Cálculos para Cálcio
    ca_per_b1 = dose * ca_levels[0]  # Para o biocarvão palha de Café 350º
    ca_per_b2 = dose * ca_levels[1]  # Para o biocarvão palha de Café 600º
    ca_per_b3 = dose * ca_levels[2]  # Para o biocarvão Casca de Eucalipto 350º
    ca_per_b4 = dose * ca_levels[3]  # Para o biocarvão Casca de Eucalipto 600º

    biocarvoes = ['PC350ºC', 'PC600ºC', 'CE350ºC', 'CE600ºC']
    values_k = [k_per_b1, k_per_b2, k_per_b3, k_per_b4]
    values_k2o = [k2o_per_b1, k2o_per_b2, k2o_per_b3, k2o_per_b4]
    values_ca = [ca_per_b1, ca_per_b2, ca_per_b3, ca_per_b4]

    background_color = "#F0F2F6"  # Cor de fundo do aplicativo

    # Gráfico de K
    fig_k, ax_k = plt.subplots(figsize=(6, 4))
    fig_k.patch.set_facecolor(background_color)  # Definir a cor de fundo do gráfico
    ax_k.set_facecolor(background_color)  # Definir a cor de fundo do eixo
    ax_k.bar(biocarvoes, values_k, color='#3498DB', edgecolor='black', linewidth=1.2)
    ax_k.set_ylabel('Quantidade de Potássio (K) (kg)', fontsize=14, weight='bold', color='#333333')
    ax_k.set_xlabel('Tipo de Biocarvão', fontsize=14, weight='bold', color='#333333')
    ax_k.set_ylim(0, 3000)  # Limite fixo de 3000 para K
    ax_k.set_title('Quantidade de Potássio (K)\n(Dose: {} t de biocarvão)'.format(dose), fontsize=16, weight='bold', color='#333333',
                   pad=20)
    ax_k.spines['right'].set_visible(False)
    ax_k.spines['top'].set_visible(False)
    for i, v in enumerate(values_k):
        ax_k.text(i, v + 30, f'{v:.2f}', ha='center', fontsize=12, color='#555555')

    # Gráfico de K2O
    fig_k2o, ax_k2o = plt.subplots(figsize=(6, 4))
    fig_k2o.patch.set_facecolor(background_color)  # Definir a cor de fundo do gráfico
    ax_k2o.set_facecolor(background_color)  # Definir a cor de fundo do eixo
    ax_k2o.bar(biocarvoes, values_k2o, color='#1ABC9C', edgecolor='black', linewidth=1.2)
    ax_k2o.set_ylabel('Equivalente em K₂O (kg)', fontsize=14, weight='bold', color='#333333')
    ax_k2o.set_xlabel('Tipo de Biocarvão', fontsize=14, weight='bold', color='#333333')
    ax_k2o.set_ylim(0, 4000)  # Limite fixo de 4000 para K2O
    ax_k2o.set_title('Equivalente em K₂O\n(Dose: {} t de biocarvão)'.format(dose), fontsize=16, weight='bold',
                     color='#333333', pad=20)
    ax_k2o.spines['right'].set_visible(False)
    ax_k2o.spines['top'].set_visible(False)
    for i, v in enumerate(values_k2o):
        ax_k2o.text(i, v + 30, f'{v:.2f}', ha='center', fontsize=12, color='#555555')

    # Gráfico de Cálcio
    fig_ca, ax_ca = plt.subplots(figsize=(6, 4))
    fig_ca.patch.set_facecolor(background_color)  # Definir a cor de fundo do gráfico
    ax_ca.set_facecolor(background_color)  # Definir a cor de fundo do eixo
    ax_ca.bar(biocarvoes, values_ca, color='#E74C3C', edgecolor='black', linewidth=1.2)
    ax_ca.set_ylabel('Quantidade de Cálcio (Ca) (kg)', fontsize=14, weight='bold', color='#333333')
    ax_ca.set_xlabel('Tipo de Biocarvão', fontsize=14, weight='bold', color='#333333')
    ax_ca.set_ylim(0, 2000)  # Limite fixo de 2000 para Ca
    ax_ca.set_title('Quantidade de Cálcio (Ca)\n(Dose: {} t de biocarvão)'.format(dose), fontsize=16, weight='bold',
                    color='#333333', pad=20)
    ax_ca.spines['right'].set_visible(False)
    ax_ca.spines['top'].set_visible(False)
    for i, v in enumerate(values_ca):
        ax_ca.text(i, v + 30, f'{v:.2f}', ha='center', fontsize=12, color='#555555')

    return fig_k, fig_k2o, fig_ca


# Função para gerar o gráfico 3D de colunas representando o volume da cova de plantio
def plot_3d_volume(profundidade, largura, comprimento):
    background_color = "#F0F2F6"  # Cor de fundo do aplicativo

    fig = plt.figure(figsize=(6, 6))
    fig.patch.set_facecolor(background_color)  # Definir a cor de fundo da figura
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

    # Ajustar o fundo dos eixos para a mesma cor de fundo
    ax.set_facecolor(background_color)

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
    background_color = "#F0F2F6"  # Cor de fundo do aplicativo

    fig = plt.figure(figsize=(6, 6))
    fig.patch.set_facecolor(background_color)  # Definir a cor de fundo da figura
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
    ax.scatter(x_points, y_points, z_points, color='black', edgecolors='white',
               s=50)  # s=50 aumenta o tamanho dos pontos

    # Ajustar o fundo dos eixos para a mesma cor de fundo
    ax.set_facecolor(background_color)

    # Ajustar os rótulos dos eixos com labelpad mais curto para aproximar
    ax.set_xlabel('Largura (cm)', labelpad=5)
    ax.set_ylabel('Comprimento (cm)', labelpad=5)
    ax.set_zlabel('Profundidade (cm)', labelpad=5)

    # Ajustar as margens do gráfico para garantir que os rótulos fiquem visíveis
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    ax.set_title(f'Distribuição de biocarvões\nna Cova com {int(pontos_por_cova)}g de Biocarvão', fontsize=14,
                 weight='bold')

    return fig


# Função do gráfico de potássio
def grafico_potassio():
    configure_sidebar()  # Chama a função para configurar a barra lateral

    # Adicionar CSS personalizado
    st.markdown("""
            <style>
            .slider-label {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: -20px;
            }
            .justified-text {
                text-align: justify;
            }
            </style>
            """, unsafe_allow_html=True)

    # Adicionar um botão para voltar à página do blog
    if st.button("Voltar para o Blog"):
        # Alterar o estado da página para "blog"
        st.session_state['page'] = 'blog'

    st.title("Biocarvões carregam nutrientes")

    st.write("""
             <p class="justified-text">Biocarvões quando aplicados ao solo também levam consigo nutrientes essenciais \
             para a nutrição de plantas. De forma geral, quanto maior o conteúdo de cinza, maior é a quantidade de \
             nutrientes presentes nos biocarvões. \
             \nAlém disso, a matéria prima e temperatura final de produção dos biocarvão são outros dois fatores \
             fundamentais na definição do conteúdo de nutrientes presente nos biocarvões. Podemos observar isto na tabela \
              apresentada abaixo:</p>
        """, unsafe_allow_html=True)

    # Dados de teores de potássio e cálcio para os biocarvões
    biocarvoes_data = {
        "Biocarvão": ['Palha de Café', 'Palha de Café', 'Casca de Eucalipto', 'Casca de Eucalipto'],
        "Temperatura": ['350ºC', '600ºC', '350ºC', '600ºC'],
        "Teor de K (g/kg)": [44.57, 56.57, 5.66, 7.01],
        "Teor de Ca (g/kg)": [16.70, 23.23, 26.36, 33.11]  # Adicionando o teor de cálcio
    }

    # Criar dataframe
    df = pd.DataFrame(biocarvoes_data)

    # Exibir a tabela centralizada com o CSS definido
    st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)

    st.write("""
                    <p class="justified-text">A tabela, aponta que biocarvões de palha de café possuem maior conteúdo \
                    de potássio quando comparado com os biocarvões de casca de Eucalipto. Já a casca de Eucalipto \
                    contém mais Cálcio comparado aos biocarvões de palha de café. Estas diferenças entre os teores \
                    destes nutrientes nos dois materiais estão relacionamento a aspectos bioquímicos que explico no \
                    post em meu site sobre bioquimica.</p>
                   """, unsafe_allow_html=True)
    st.write("""
                        <p class="justified-text">Também podemos observar diferenças quanto à temperatura. Onde \
                        temperatura mais elevadas concentram mais nurientes que temperaturas mais baixas. Este \
                        fenômeno esta relacionada com as perdas do conteúdo orgânico e preservação do conteúdo \
                        mas vamos tratar disto em outro post. Gostaria observar com você a capacidade dos biocarvões \
                        de palha de café em carregar consigo quantidade de K sóluvel para o solo</p>
                       """, unsafe_allow_html=True)

    st.write("""
                            <p class="justified-text">A nossa tabela aponta que cada tonelada de biocarvão de palha \
                            de café contém entre 40 e 60 kg de potássio. Mova o slider abaixo dos gráficos para ver \
                            quanto K cada tonelada de biocarvão de palha de café carrega. Coloquei ao lado um gráfico \
                            com os valores equivalentes em K<sub>2</sub>O como parâmetro de comparação já que as \
                            recomendações de fertilizantes potássicos são expressa em K<sub>2</sub>O.</p>
                           """, unsafe_allow_html=True)

    # Exibir gráficos de K, K2O e Ca em colunas
    (col_k, col_k2o) = st.columns(2)

    # Usar st.markdown para exibir um texto estilizado acima do slider
    st.markdown('<p class="slider-label">Selecione a quantidade de biocarvão (t)</p>', unsafe_allow_html=True)

    # Slider
    dose = st.slider('', 0, 50, 1, format="%d t")  # Mantendo o texto vazio para evitar repetição
    k_levels = [44.57, 56.57, 5.66, 7.01]  # Correspondente a B1, B2, B3, B4 (Potássio)
    ca_levels = [16.70, 23.23, 26.36, 33.11]  # Correspondente a B1, B2, B3, B4 (Cálcio)
    fig_k, fig_k2o, fig_ca = plot_k_k2o_and_ca_levels(dose, k_levels, ca_levels)

    # Exibir os gráficos 2D de K, K2O e Ca em colunas
    with col_k:
        st.pyplot(fig_k)
    with col_k2o:
        st.pyplot(fig_k2o)
    #with col_ca:
    #    st.pyplot(fig_ca)

    st.write("""
                       <p class="justified-text">1 tonelada de biocarvão de palha de café pode ser considerada uma \
                       quantidade complicada para transportar e aplicar. Contudo estes valores reduzem já que \
                       o produtor não irá aplicar em área total. Neste caso, para fins de adubação, uma tonelada de \
                       biocarvão pode adicionar o equivalente a 50 e 70 kg/ha de K2O e para isto são necessárias \
                       32 gramas por plantas misturadas em uma cova de 40 cm x 40 cm x 40 cm.</p>
                   """, unsafe_allow_html=True)

    st.write("""
                        <p class="justified-text">Experimente novamente mover o slider acima e as dimensões da cova \
                        de plantio abaixo e veja como a quantidade de biocarvões por cova se altera.</p>
                   """, unsafe_allow_html=True)

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

    st.write("""
                       <p class="justified-text">A produção de biocarvões de palha de café é dependente da produtividade do café no campo. Lembrando \
                       que o grão que é colhido no campo está exportando K para fora da lavoura. Sendo assim a palha de \
                       café quando retornada ao campo contribui para a economia de fertilizantes.</p>
                   """, unsafe_allow_html=True)

# Executar a função de exibição
grafico_potassio()

