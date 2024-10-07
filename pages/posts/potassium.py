import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


# Função para gerar o gráfico de K por tonelada de biocarvão
def plot_k_levels(dose, k_levels):
    k_per_b1 = dose * k_levels[0]  # Para o biocarvão palha de Café 350º
    k_per_b2 = dose * k_levels[1]  # Para o biocarvão palha de Café 600º
    k_per_b3 = dose * k_levels[2]  # Para o biocarvão Casca de Eucalipto 350º
    k_per_b4 = dose * k_levels[3]  # Para o biocarvão Casca de Eucalipto 600º

    biocarvoes = ['PC350ºC', 'PC600ºC', 'CE350ºC', 'CE600ºC']
    values = [k_per_b1, k_per_b2, k_per_b3, k_per_b4]

    y_lim_max = max(values) * 1.1

    fig, ax = plt.subplots()
    ax.bar(biocarvoes, values, color=['black', 'black', 'black', 'black'])
    ax.set_ylabel('Quantidade de Potássio (K) (kg)')
    ax.set_xlabel('Tipo de Biocarvão')
    ax.set_ylim(0, y_lim_max)
    ax.set_title(f'Quantidade de Potássio (K) em cada biocarvão (Dose: {dose} t)')

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    for i, v in enumerate(values):
        ax.text(i, v + y_lim_max * 0.02, f'{v:.2f}', ha='center')

    return fig


# Função do gráfico de potássio
def grafico_potassio():
    # Adicionar um botão para voltar à página do blog
    if st.button("Voltar para o Blog"):
        # Alterar o estado da página para "blog"
        st.session_state['page'] = 'blog'

    st.title("Impacto do Biocarvão no Teor de Potássio (K) por Dose Aplicada")

    st.write("""
        Aqui estão detalhes sobre a quantidade de potássio nos diferentes tipos de biocarvão, 
        com base na dose selecionada (em toneladas). Ajuste a dose e veja o impacto!
    """)

    # Dados de teores de potássio para os biocarvões
    biocarvoes_data = {
        "Biocarvão": ['PC350ºC', 'PC600ºC', 'CE350ºC', 'CE600ºC'],
        "Teor de K (g/kg)": [4.457, 5.657, 0.566, 0.701]
    }

    # Criar dataframe
    df = pd.DataFrame(biocarvoes_data)

    # CSS para centralizar a tabela
    st.markdown("""
           <style>
           .center-table {
               display: block;
               margin-left: auto;
               margin-right: auto;
               width: 30%; /* Ajuste a largura conforme necessário */
           }
           </style>
           """, unsafe_allow_html=True)

    # Centralizar título e tabela
    st.markdown("<h3 style='text-align: center;'>Teores de Potássio (K) nos Biocarvões</h3>", unsafe_allow_html=True)

    # Exibir a tabela centralizada
    st.markdown(f"<div class='center-table'>{df.to_html(index=False)}</div>", unsafe_allow_html=True)

    # Aplicar margens laterais e centralização
    col1, col2, col3 = st.columns([1, 3, 1])

    # Exibir a tabela e o gráfico dentro da coluna centralizada
    with col2:

        # Controle de dose de biocarvão
        dose = st.slider('Selecione a quantidade de biocarvão (t)', 0, 50, 1)
        k_levels = [4.457, 5.657, 0.566, 0.701]  # Correspondente a B1, B2, B3, B4

        # Gerar o gráfico
        fig = plot_k_levels(dose, k_levels)
        st.pyplot(fig)


# Executar a função de exibição
grafico_potassio()
