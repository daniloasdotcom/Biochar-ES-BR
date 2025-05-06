import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Função para carregar o arquivo Excel
def load_data():
    file_path = "data/cinzas.xlsx"
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        st.error("O arquivo 'cinzas.xlsx' não foi encontrado no diretório do projeto.")
        return None


# Função para exibir texto explicativo
def show_explanatory_text01():
    explicativo_texto = """
    <div style="text-align: justify;">
    A temperatura de carbonização e o tipo de material de origem (feedstock) são fatores cruciais na determinação das propriedades dos biochars, definindo, por exemplo, o conteúdo de nutrientes, sua disponibilidade, a quantidade de cargas e grupos funcionais presentes no biocarvão, sua recalcitrância e também a alcalinidade do biocarvões.

    No que se refere a alcalinidade dos biochars, é essencial para seu uso como condicionador de solo, pois influencia diretamente a capacidade de neutralizar a acidez de solo ácidos, promovendo um ambiente mais propício para o crescimento das culturas agrícolas. Além disso, a alcalinidade está relacionada à capacidade de troca catiônica, que é crucial para a retenção e disponibilização de nutrientes para as plantas. Desta forma o uso de biochars deve levar em conta sua capacidade de mudar o pH do solo para que seu uso adequado sem sistemas agrícolas.

    Fidel et al., (2017)  divide as fontes de alcalinidade dos biocarvões em quatro categorias principais: grupos funcionais orgânicos de baixa acidez, compostos orgânicos solúveis, carbonatos e outros alcalis inorgânicos.  (Fidel et al., 2017). No que se refere ao carbonatos e outro alcalis inorgânicos, estes estão presentes no conteúdo cinzas do biocarvões.

    Sendo assim era de se esperar que quanto maior o conteúdo de cinzas mais seria a alcalinidade dos biocarvão. Contudo nem sempre é isso que observamos

    </div>
    """
    st.markdown(explicativo_texto, unsafe_allow_html=True)


def show_explanatory_text02():
    explicativo_texto = """
    <div style="text-align: justify;">
    Ao olharmos para o gráfico acima, percebemos que mesmo materiais altamente lignificados (pontos verdes), que possuem menor teor de cinzas (pontos mais concentrados no lado esquerdo do gráfico), apresentam variações significativas de pH (entre 4 e 10), indicando que o conteúdo de cinzas não possui necessariamente um boa correlação com a alcalinidade dos biochar.
    <br>
    </div>
    """
    st.markdown(explicativo_texto, unsafe_allow_html=True)


def show_explanatory_text03():
    explicativo_texto = """
    <div style="text-align: justify;">
    Isto se deve ao fato que a alcalinidade está ligada, sobretudo, às espécies químicas formadas após a carbonização.
    <br>
    </div>
    """
    st.markdown(explicativo_texto, unsafe_allow_html=True)


# Função para exibir o gráfico com a citação verticalizada
def plot_graph(df, x_col, y_col, title, x_label, y_label, selected_option, color_map):
    plt.style.use("seaborn-v0_8-poster")
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plotando os dados com base na seleção
    if selected_option == "Conjunto completo":
        for classification, group_data in df.groupby("Classificação"):
            ax.scatter(
                group_data[x_col],
                group_data[y_col],
                label=classification,
                color=color_map.get(classification, "gray"),
                alpha=0.8,
                s=100
            )
    else:
        group_data = df[df["Classificação"] == selected_option]
        ax.scatter(
            group_data[x_col],
            group_data[y_col],
            label=selected_option,
            color=color_map.get(selected_option, "gray"),
            alpha=0.8,
            s=100
        )

    # Configurações do eixo e estilo
    ax.set_title(title, fontsize=18, fontweight="bold")
    ax.set_xlabel(x_label, fontsize=14)
    ax.set_ylabel(y_label, fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.legend(title="Classificação", fontsize=12, title_fontsize=14, loc='lower right')
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Adicionando a citação no gráfico na posição desejada com orientação vertical
    ax.text(
        1.05, 0.5,  # Posição relativa no gráfico (x: fora da área de plotagem, y: meio vertical)
        "Fonte de dados: UCD BIOCHAR DATABASE, 2024",
        transform=ax.transAxes,  # Coordenadas relativas ao eixo
        fontsize=10,  # Tamanho da fonte
        color="gray",  # Cor do texto
        ha="left",  # Alinhamento horizontal à esquerda
        va="center",  # Alinhamento vertical no centro
        rotation=90  # Rotação do texto (90 graus para verticalizar)
    )

    return fig


# Função principal para exibir os gráficos e a análise
def main():
    st.title("pH e o conteúdo inorgânico de biocarvões")

    # Exibir texto explicativo01
    show_explanatory_text01()

    # Carregar os dados
    df_cinzas = load_data()

    if df_cinzas is not None:
        options = ["Conjunto completo", "Pouco lignificado", "Moderadamente lignificado", "Altamente lignificado"]
        color_map = {
            "Pouco lignificado": "#1f77b4",
            "Moderadamente lignificado": "#ff7f0e",
            "Altamente lignificado": "#2ca02c"
        }

        # Gráfico: Cinzas vs pH
        layout = st.columns([4, 7])
        with layout[0]:
            selected_option = st.radio("Selecione a classificação:", options, index=0, key="cinzas_ph")
        with layout[1]:
            fig = plot_graph(df_cinzas, "Cinzas", "pH", "Cinzas vs pH", "Cinzas (%)", "pH", selected_option, color_map)
            st.pyplot(fig)

        # Adicionar expander explicativo com fundo cinza no conteúdo
        with st.expander(
                "💡 Por que adicionamos no gráfico acima as categorias 'pouco', 'moderadamente' e 'altamente' lignificados?"):
            st.markdown("""
            <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
            A ideia de nossa classificação é que quanto maior o conteúdo orgânico resistente ao processo de oxidação, menor é a sua capacidade de gerar cinzas. Neste sentido, lhe convido a observar o gráfico, também nestas categorias separadamente.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

    # Exibir texto explicativo02
    show_explanatory_text02()

    st.markdown("<br>", unsafe_allow_html=True)

    # Exibir texto explicativo03
    show_explanatory_text03()

    st.markdown("<br>", unsafe_allow_html=True)

    # Referência
    st.markdown("""
    <div style="text-align: left;">
    <strong>Referências</strong>: <br>
    Fidel, R.B., Laird, D.A., Thompson, M.L., & Lawrinenko, M. (2017). Characterization and quantification of biochar alkalinity. 
    <em>Chemosphere, 167</em>, 367-373. Disponível em: <a href="https://doi.org/10.1016/j.chemosphere.2016.09.151" target="_blank">https://doi.org/10.1016/j.chemosphere.2016.09.151</a>.
    <br>
    UCD BIOCHAR DATABASE. Biochar Database. University of California, Davis, 2024. Disponível em: <a href="https://biochar.ucdavis.edu" target="_blank">https://biochar.ucdavis.edu</a>. Acesso em: 4 dez. 2024.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
